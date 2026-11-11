


class AppException(Exception):
    pass


class AppInputError(AppException):
    pass


class EnvironmentVariablesError(AppException):
    def __init__(self, var_name: str | None = None, *args):
        super().__init__(*args)
        self.var_name = var_name
