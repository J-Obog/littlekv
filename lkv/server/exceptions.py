class LKVError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__('ERROR => ' + msg)

class NoCommandProvidedError(LKVError):
    def __init__(self) -> None:
        super().__init__(f'Command must be provided in request payload')

class NoParamsProvidedError(LKVError):
    def __init__(self) -> None:
        super().__init__(f'Parameters must be provided in request payload')

class NoCommandError(LKVError):
    def __init__(self, cmd: str) -> None:
        super().__init__(f'Unknown command {cmd}')

class BadArityError(LKVError):
    def __init__(self, cmd: str, given: int, expected: int) -> None:
        super().__init__(f'Wrong number of arguments to command {cmd} ({given} given, expected {expected})')

class ConnError(LKVError):
    def __init__(self, host: str, port: int) -> None:
        super().__init__(f'Unable to connect to {host} on port {port}')