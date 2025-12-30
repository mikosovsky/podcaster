from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Dict
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from moviepy import VideoFileClip, CompositeVideoClip
from moviepy.video.VideoClip import VideoClip


@dataclass(frozen=True)
class WordSpan:
    text: str
    start: float
    end: float


@dataclass(frozen=True)
class SegmentSpan:
    start: float
    end: float
    words: Tuple[WordSpan, ...]


@dataclass(frozen=True)
class TwoLineSegment:
    start: float
    end: float
    words: Tuple[WordSpan, ...]
    cut_index: int  # section between line 1 and line 2


@dataclass
class WordAccumulator:
    """Helper class to accumulate characters into words."""

    buf: List[str] = field(default_factory=list)
    start: Optional[float] = None
    end: Optional[float] = None

    def add_char(self, ch: str, st: float, en: float) -> None:
        """Function to add a character to the accumulator.
        Args:
            ch (str): The character to add.
            st (float): The start time of the character.
            en (float): The end time of the character.
        """
        if self.start is None:
            self.start = float(st)
        self.buf.append(ch)
        self.end = float(en)

    def flush_to(self, out: List[WordSpan]) -> None:
        """Function to flush the accumulated characters as a word to the output list.
        Args:
            out (List[WordSpan]): The list to append the word to.
        """
        if self.buf and self.start is not None and self.end is not None:
            out.append(WordSpan("".join(self.buf), self.start, self.end))
        self.buf.clear()
        self.start = None
        self.end = None


def alignment_to_words(
    chars: List[str], starts: List[float], ends: List[float]
) -> List[WordSpan]:
    """Convert character-level alignment to word-level alignment.
    Args:
        chars (List[str]): List of characters.
        starts (List[float]): List of start times for each character.
        ends (List[float]): List of end times for each character.
    Returns:
        List[WordSpan]: List of word-level alignments.
    """
    if not (len(chars) == len(starts) == len(ends)):
        raise ValueError("characters / starts / ends muszą mieć tę samą długość")

    out: List[WordSpan] = []
    acc = WordAccumulator()

    for ch, st, en in zip(chars, starts, ends):
        if ch.isspace():
            acc.flush_to(out)
        else:
            acc.add_char(ch, st, en)

    acc.flush_to(out)
    return out


def words_to_segments(
    words: List[WordSpan], max_chars: int = 60, max_duration: float = 2.8
) -> List[SegmentSpan]:
    """Split words into segments based on max characters and max duration.
    Args:
        words (List[WordSpan]): List of word-level alignments.
        max_chars (int): Maximum number of characters per segment.
        max_duration (float): Maximum duration of each segment in seconds.
    Returns:
        List[SegmentSpan]: List of segments.
    """
    segments: List[SegmentSpan] = []
    cur: List[WordSpan] = []
    cur_len = 0
    seg_start = None
    seg_end = None

    def flush():
        nonlocal cur, cur_len, seg_start, seg_end
        if cur and seg_start is not None and seg_end is not None:
            segments.append(SegmentSpan(seg_start, seg_end, tuple(cur)))
        cur, cur_len, seg_start, seg_end = [], 0, None, None

    for w in words:
        add_len = (1 if cur else 0) + len(w.text)
        if seg_start is None:
            seg_start = w.start

        prospective_len = cur_len + add_len
        prospective_dur = w.end - seg_start

        if cur and (prospective_len > max_chars or prospective_dur > max_duration):
            flush()
            seg_start = w.start
            cur = [w]
            cur_len = len(w.text)
            seg_end = w.end
            continue

        cur.append(w)
        cur_len = prospective_len
        seg_end = w.end

    flush()
    return segments


def _joined_len(ws: Tuple[WordSpan, ...]) -> int:
    """Function to calculate the length of joined words including spaces.
    Args:
        ws (Tuple[WordSpan, ...]): Tuple of WordSpan objects.
    Returns:
        int: The total length of the joined words including spaces.
    """
    if not ws:
        return 0
    return sum(len(w.text) for w in ws) + (len(ws) - 1)


def split_to_two_lines(
    seg: SegmentSpan, max_chars_per_line: int = 32
) -> TwoLineSegment:
    """Split a segment into two lines for karaoke display.
    Args:
        seg (SegmentSpan): The segment to split.
        max_chars_per_line (int): Maximum characters allowed per line.
    Returns:
        TwoLineSegment: The segment split into two lines.
    """
    words = seg.words
    n = len(words)

    if n <= 1:
        return TwoLineSegment(seg.start, seg.end, words, cut_index=n)

    best_cut = 1
    best_score = float("inf")

    for cut in range(1, n):
        l1 = _joined_len(words[:cut])
        l2 = _joined_len(words[cut:])

        penalty = 0
        if l1 > max_chars_per_line:
            penalty += (l1 - max_chars_per_line) * 10
        if l2 > max_chars_per_line:
            penalty += (l2 - max_chars_per_line) * 10

        score = abs(l1 - l2) + penalty
        if score < best_score:
            best_score = score
            best_cut = cut

    return TwoLineSegment(seg.start, seg.end, words, cut_index=best_cut)


def segments_to_two_lines(
    segments: List[SegmentSpan], max_chars_per_line: int = 32
) -> List[TwoLineSegment]:
    """Function to convert segments to two-line segments.
    Args:
        segments (List[SegmentSpan]): List of segments.
        max_chars_per_line (int): Maximum characters allowed per line.
    Returns:
        List[TwoLineSegment]: List of two-line segments."""
    return [split_to_two_lines(s, max_chars_per_line) for s in segments]


class ImageCache:
    """Class for caching rendered images."""

    def __init__(self):
        self._cache: Dict[Tuple, np.ndarray] = {}

    def get(self, key: Tuple) -> Optional[np.ndarray]:
        """Function to get a cached image.
        Args:
            key (Tuple): The key for the cached image.
        Returns:
            Optional[np.ndarray]: The cached image or None if not found."""
        return self._cache.get(key)

    def set(self, key: Tuple, value: np.ndarray) -> None:
        """Function to set a cached image.
        Args:
            key (Tuple): The key for the cached image.
            value (np.ndarray): The image to cache.
        """
        self._cache[key] = value


def render_two_line_image(
    words: Tuple[str, ...],
    cut_index: int,
    highlight_index: int,
    canvas_w: int,
    font_path: str,
    font_size: int,
    cache: ImageCache,
    padding: int = 18,
    line_gap: int = 10,
    stroke: int = 4,
    min_font_size: int = 12,
) -> np.ndarray:
    """Render a two-line karaoke image with highlighted word.
    Args:
        words (Tuple[str, ...]): Tuple of words to render.
        cut_index (int): Index to split words into two lines.
        highlight_index (int): Index of the word to highlight.
        canvas_w (int): Width of the canvas.
        font_path (str): Path to the font file.
        font_size (int): Initial font size.
        cache (ImageCache): Cache for rendered images.
        padding (int): Padding around the text.
        line_gap (int): Gap between the two lines.
        stroke (int): Stroke width for text outline.
        min_font_size (int): Minimum font size to use.
    Returns:
        np.ndarray: The rendered image as a NumPy array.
    """
    # cache key MUST depend on font_size (it will be auto-changed)
    key = (
        words,
        cut_index,
        highlight_index,
        canvas_w,
        font_path,
        font_size,
        padding,
        line_gap,
        stroke,
    )
    cached = cache.get(key)
    if cached is not None:
        return cached

    line1 = words[:cut_index]
    line2 = words[cut_index:]

    # Always render at full video width - no positioning surprises
    img_w = int(canvas_w)

    def measure(font, ws):
        if not ws:
            return 0.0, []
        space_w = float(font.getlength(" "))
        widths = [float(font.getlength(w)) for w in ws]
        total = sum(widths) + space_w * (len(ws) - 1)
        return total, widths, space_w

    # Auto-fit: if any line is too wide (with stroke margin), decrease font size
    fs = int(font_size)
    while True:
        font = ImageFont.truetype(font_path, fs)
        w1, widths1, space_w1 = measure(font, line1)
        w2, widths2, space_w2 = measure(font, line2)

        # available width: padding + stroke margin on both sides
        available = img_w - 2 * padding - 2 * stroke - 2

        if max(w1, w2) <= available or fs <= min_font_size:
            break
        fs -= 1  # decrease gradually; stable and predictable

    ascent, descent = font.getmetrics()
    text_h = ascent + descent

    img_h = int(text_h * (2 if line2 else 1) + padding * 2 + (line_gap if line2 else 0))

    img = Image.new("RGBA", (img_w, img_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    def draw_line(ws, widths, space_w, y, offset):
        if not ws:
            return
        total_line_w = sum(widths) + space_w * (len(ws) - 1)
        x = (img_w - total_line_w) / 2.0  # centered within the full width

        for i, word in enumerate(ws):
            gi = offset + i
            color = (
                (255, 235, 59, 255) if gi == highlight_index else (255, 255, 255, 255)
            )
            draw.text(
                (x, y),
                word,
                font=font,
                fill=color,
                stroke_width=stroke,
                stroke_fill=(0, 0, 0, 255),
            )
            x += widths[i] + space_w

    y = padding
    draw_line(line1, widths1, space_w1, y, 0)
    if line2:
        draw_line(line2, widths2, space_w2, y + text_h + line_gap, cut_index)

    arr = np.array(img)
    cache.set(key, arr)
    return arr


def make_segment_karaoke_clip(
    seg: TwoLineSegment,
    video_w: int,
    y_pos: int,
    font_path: str,
    font_size: int,
    cache: ImageCache,
    fps: float,
    safety_pad: float = 0.0,  # set e.g. 1/fps
):
    """Function to create a karaoke clip for a segment.
    Args:
        seg (TwoLineSegment): The segment to create the clip for.
        video_w (int): Width of the video.
        y_pos (int): Vertical position of the clip.
        font_path (str): Path to the font file.
        font_size (int): Font size for rendering text.
        cache (ImageCache): Cache for rendered images.
        fps (float): Frames per second of the video.
        safety_pad (float): Safety padding to avoid edge cases.
    Returns:
        VideoClip: The created karaoke clip with mask.
    """
    texts = tuple(w.text for w in seg.words)
    words = seg.words

    state = {"hi": -1, "rgba": None}

    def pick_highlight(abs_t: float) -> int:
        for i, w in enumerate(words):
            if w.start <= abs_t < w.end:
                return i

        if abs_t < words[0].start:
            return 0
        if abs_t >= words[-1].end:
            return len(words) - 1

        last = 0
        for i, w in enumerate(words):
            if abs_t >= w.start:
                last = i
            else:
                break
        return last

    def ensure_rgba(abs_t: float) -> None:
        hi = pick_highlight(abs_t)
        if hi != state["hi"] or state["rgba"] is None:
            state["hi"] = hi
            state["rgba"] = render_two_line_image(
                texts,
                seg.cut_index,
                hi,
                video_w,
                font_path,
                font_size,
                cache,
            )

    def make_frame_rgb(t: float):
        abs_t = seg.start + t
        ensure_rgba(abs_t)
        return state["rgba"][..., :3]

    def make_frame_rgba(t: float):
        abs_t = seg.start + t
        ensure_rgba(abs_t)
        return state["rgba"]

    dur = (seg.end - seg.start) + safety_pad

    # RGB Clip
    clip = (
        VideoClip(make_frame_rgb, duration=dur)
        .with_start(seg.start)
        .with_position(("center", y_pos))
    )

    # RGBA Clip converted to Mask
    rgba_clip = (
        VideoClip(make_frame_rgba, duration=dur)
        .with_start(seg.start)
        .with_position(("center", y_pos))
    )
    mask = rgba_clip.to_mask()

    return clip.with_mask(mask)


def burn_karaoke_moviepy(
    video_path: str,
    alignment_obj,
    output_path: str,
    font_path: str,
    max_segment_chars: int = 60,
    max_segment_duration: float = 2.8,
    max_chars_per_line: int = 20,
    y_pos_ratio: float = 0.5,
    font_size_ratio: float = 0.06,
):
    """Function to burn karaoke subtitles onto a video using MoviePy.
    Args:
        video_path (str): Path to the input video file.
        alignment_obj: Alignment object containing character-level alignment data.
        output_path (str): Path to save the output video file.
        font_path (str): Path to the font file for rendering subtitles.
        max_segment_chars (int): Maximum characters per segment.
        max_segment_duration (float): Maximum duration of each segment in seconds.
        max_chars_per_line (int): Maximum characters per line.
        y_pos_ratio (float): Vertical position ratio for subtitles.
        font_size_ratio (float): Font size ratio relative to video height.
    Example:
        burn_karaoke_moviepy(
            video_path="video.mp4",
            alignment_obj=normalized_alignment,
            output_path="video_karaoke.mp4",
            font_path="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        )
    """
    video = VideoFileClip(video_path)

    words = alignment_to_words(
        alignment_obj.characters,
        alignment_obj.character_start_times_seconds,
        alignment_obj.character_end_times_seconds,
    )

    segments = words_to_segments(words, max_segment_chars, max_segment_duration)
    two_lines = segments_to_two_lines(segments, max_chars_per_line)

    font_size = max(18, int(video.h * font_size_ratio))
    y_pos = int(video.h * y_pos_ratio)

    cache = ImageCache()
    clips = []

    fps = float(getattr(video, "fps", 30)) or 30.0
    safety_pad = 1.0 / fps  # removing edge cases with timing

    for seg in two_lines:
        clips.append(
            make_segment_karaoke_clip(
                seg=seg,
                video_w=video.w,
                y_pos=y_pos,
                font_path=font_path,
                font_size=font_size,
                cache=cache,
                fps=fps,
                safety_pad=safety_pad,
            )
        )

    final = CompositeVideoClip([video, *clips])
    final.write_videofile(output_path, audio_codec="aac", fps=int(round(fps)))
