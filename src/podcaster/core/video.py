from moviepy import VideoFileClip, AudioFileClip
from moviepy.video.fx.Loop import Loop


def fit_video_to_audio(video_path: str, audio_path: str, out_path: str):
    """
    Fit the video duration to match the audio duration by trimming or looping the video.
    
    Args:
        video_path (str): Path to the input video file
        audio_path (str): Path to the input audio file
        out_path (str): Path to save the output video file
    """
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    if video.duration >= audio.duration:
        fitted = video.subclipped(0, audio.duration)
    else:
        fitted = video.with_effects([Loop(duration=audio.duration)])

    final = fitted.with_audio(audio)

    final.write_videofile(
        out_path,
        codec="libx264",
        audio_codec="aac",
    )

    video.close()
    audio.close()
    final.close()
