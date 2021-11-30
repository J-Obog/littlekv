
class CliError(Exception):
    def __init__(self, msg: str, code: int) -> None:
        super().__init__('ERROR => ' + msg)
        self.code = code

class NoCommandError(CliError):
    def __init__(self, cmd: str) -> None:
        super().__init__(f'Unknown command {cmd}', 798)

class WrongArityError(CliError):
    def __init__(self, cmd: str) -> None:
        super().__init__(f'Wrong number of arguments to {cmd} command', 990)

class ConnError(CliError):
    def __init__(self, host: str, port: int) -> None:
        super().__init__(f'Unable to connect to {host} on port {port}', 737)