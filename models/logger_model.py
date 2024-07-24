from dataclasses import dataclass
from enum import Enum
from typing import List


@dataclass
class LogLevel(Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

    def __str__(self):
        return self.value


@dataclass
class LoggerModel:
    logger_name: str
    base_level: str
    fmt: str
    datefmt: str
    log_file_path: str
    handlers: List[str]

    @staticmethod
    def _validate_base_level(v):
        if v.upper() not in LogLevel.__members__:
            raise ValueError(
                f"Invalid log level: {v}. Valid levels are {', '.join(LogLevel.__members__)}")
        return v.upper()

