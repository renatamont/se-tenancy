class ErrorFetchingData(Exception):
    def __init__(self, msg="Error on Fetching Data", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InvalidParams(Exception):
    def __init__(self, msg="Error: You should insert valid query params", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class ForbiddenError(Exception):
    def __init__(self, msg="Forbidden", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class BadRequestError(Exception):
    def __init__(self, msg="Bad request", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class InternalServerError(Exception):
    def __init__(self, msg="Internal server", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class UnauthorizedError(Exception):
    def __init__(self, msg="Unauthorized", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)