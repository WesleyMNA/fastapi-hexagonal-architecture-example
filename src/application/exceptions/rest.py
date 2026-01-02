class RestException(Exception):

    def __init__(self,
                 title: str,
                 status_code: int,
                 detail: str,
                 *args):
        super().__init__(*args)
        self._title = title
        self._status_code = status_code
        self._detail = detail

    @property
    def content(self) -> dict:
        return {
            'title': self._title,
            'status': self._status_code,
            'detail': self._detail,
        }

    @property
    def status_code(self) -> int:
        return self._status_code


class NotFound(RestException):

    _DEFAULT_TITLE = 'Not Found'

    def __init__(self, detail: str = _DEFAULT_TITLE, title: str = _DEFAULT_TITLE, *args):
        super().__init__(title, 404, detail, *args)


class Conflict(RestException):

    _DEFAULT_TITLE = 'Conflict'

    def __init__(self, detail: str = _DEFAULT_TITLE, title: str = _DEFAULT_TITLE, *args):
        super().__init__(title, 409, detail, *args)
