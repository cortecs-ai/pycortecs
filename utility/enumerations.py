from enum import IntEnum


class MediaEndpointType(IntEnum):
    TWITTER = 1
    NEWS = 2
    REDDIT = 3
    NOT_SPECIFIED = -1

class MediaSignalType(IntEnum):
    SENTIMENT = 1
    VOLUME = 2
    BALANCE = 3
    DOMINANCE = 4
    NOT_SPECIFIED = -1

class StatusCode(IntEnum):
    OK = 1
    ERROR = 2
    RETRY = 3
