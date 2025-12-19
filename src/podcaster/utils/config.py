"""Configuration management utilities."""

from pathlib import Path
from typing import Any, Optional, Dict
import json
import yaml

# TODO: Add environment-specific configs (dev, staging, prod)
# TODO: Add configuration validation using schemas
# TODO: Add configuration hot-reloading


class ConfigManager:
    """
    Configuration manager for podcast application.
    
    Handles loading, saving, and accessing configuration settings.
    """
    
    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize configuration manager.
        
        Args:
            config_path: Path to configuration file
        """
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        
        if config_path and config_path.exists():
            self.load_config(config_path)
        
        # TODO: Add default configuration fallbacks
        # TODO: Add configuration encryption for sensitive data
        # TODO: Add configuration change notifications
    
    def load_config(self, config_path: Path) -> None:
        """
        Load configuration from file.
        
        Args:
            config_path: Path to config file (JSON or YAML)
        """
        self.config_path = config_path
        
        with open(config_path, "r", encoding="utf-8") as f:
            if config_path.suffix == ".json":
                self.config = json.load(f)
            elif config_path.suffix in [".yaml", ".yml"]:
                self.config = yaml.safe_load(f)
            else:
                raise ValueError(f"Unsupported config format: {config_path.suffix}")
        
        # TODO: Add config validation after loading
        # TODO: Add config merging (base + overrides)
        # TODO: Add error handling for malformed configs
    
    def save_config(self, config_path: Optional[Path] = None) -> None:
        """
        Save configuration to file.
        
        Args:
            config_path: Path to save config (uses loaded path if None)
        """
        path = config_path or self.config_path
        if not path:
            raise ValueError("No config path specified")
        
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, "w", encoding="utf-8") as f:
            if path.suffix == ".json":
                json.dump(self.config, f, indent=2)
            elif path.suffix in [".yaml", ".yml"]:
                yaml.dump(self.config, f, default_flow_style=False)
        
        # TODO: Add atomic writes to prevent corruption
        # TODO: Add backup before overwriting
        # TODO: Add validation before saving
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            key: Configuration key (supports dot notation, e.g., 'llm.model')
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        keys = key.split(".")
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
        
        # TODO: Add type casting based on expected type
        # TODO: Add environment variable substitution
        # TODO: Add config value interpolation
    
    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value.
        
        Args:
            key: Configuration key (supports dot notation)
            value: Value to set
        """
        keys = key.split(".")
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        
        # TODO: Add validation when setting values
        # TODO: Add change tracking/audit log
        # TODO: Add notification on value changes
    
    def get_all(self) -> Dict[str, Any]:
        """
        Get all configuration.
        
        Returns:
            dict: Full configuration dictionary
        """
        return self.config.copy()
        
        # TODO: Add config export in different formats
        # TODO: Add config documentation generation
        # TODO: Add config diff between versions
