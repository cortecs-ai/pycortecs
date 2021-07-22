from enum import IntEnum, Enum


class ExtendedEnum(Enum):

    @classmethod
    def as_list(cls):
        return list(map(lambda c: c.value, cls))


class EndpointType(ExtendedEnum):
    TWITTER = 'twitter'
    NEWS = 'news'
    REDDIT = 'reddit'


class StatusCode(IntEnum):
    OK = 1
    ERROR = 2
    RETRY = 3
