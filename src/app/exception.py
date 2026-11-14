


class AppException(Exception):

    def __init__(self, message: str, code: int, code_str: str, *args):
        super().__init__(*args)

        self.code_str = code_str
        self.message = message
        self.code = code

    def __str__(self):
        return self.message


class AppInputError(AppException):
    pass


class AppLLMResponseNotJSON(AppException):
    def __init__(self, message, *args):
        super().__init__(
            message=message,
            code=500,
            code_str='JSON_LLM_RESPONSE_ERROR',
            *args
        )


class AppLLMTimeOut(AppException):
    def __init__(self, message, *args):
        super().__init__(
            message=message,
            code=500,
            code_str='LLM_TIMEOUT_ERROR',
            *args
        )


class AppLLMServiceUnavailable(AppException):
    def __init__(self, message, *args):
        super().__init__(
            message=message,
            code=500,
            code_str='LLM_SERVICE_UNAVAILABLE',
            *args
        )


class EnvironmentVariablesError(AppException):
    def __init__(self, var_name: str | None = None, *args):
        super().__init__(*args)
        self.var_name = var_name
