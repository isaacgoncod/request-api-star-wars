class HttpRequestError(Exception):
    '''
      Http Request Exception
    '''

    def __init__(self, message: str, status_code: str) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
