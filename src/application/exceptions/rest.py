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

    def __init__(self, detail: str = 'Not Found', title: str = 'Not Found', *args):
        super().__init__(title, 404, detail, *args)
