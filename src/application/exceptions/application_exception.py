class ApplicationException(Exception):

    def __init__(self,
                 detail: str,
                 *args):
        super().__init__(*args)
        self._detail = detail

    @property
    def detail(self):
        return self._detail


class NotFound(ApplicationException):

    def __init__(self, detail: str = 'Not Found', *args):
        super().__init__(detail, *args)


class Conflict(ApplicationException):

    def __init__(self, detail: str = 'Conflict', *args):
        super().__init__(detail, *args)
