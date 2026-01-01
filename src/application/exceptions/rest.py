class RestException(Exception):

    def __init__(self,
                 status_code: int,
                 detail: str,
                 *args):
        super().__init__(*args)
        self.status_code = status_code
        self.detail = detail


class NotFound(RestException):

    def __init__(self, detail: str = 'Not Found', *args):
        super().__init__(404, detail, *args)
