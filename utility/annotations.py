import functools
from utility.exceptions import EndpointNotSpecifiedError
from utility.enumerations import MediaEndpointType


def media_endpoint(endpoint_type: MediaEndpointType = MediaEndpointType.NOT_SPECIFIED):
    def endpoint_decorator(func):
        @functools.wraps(func)
        def function_wrapper(since, until, asset_id, window):
            if endpoint_type == MediaEndpointType.NOT_SPECIFIED:
                raise EndpointNotSpecifiedError
            f = func(endpoint_type, since, until, asset_id, window)
            return f
        return function_wrapper
    return endpoint_decorator




