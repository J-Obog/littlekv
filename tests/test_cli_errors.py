from tests.helpers import run_command_suite

def test_bad_arity():
   run_command_suite('lkv-server', 'lkv-cli', [('ping foobar', 'Wrong number of arguments')])

def test_no_command():
   run_command_suite('lkv-server', 'lkv-cli', [('cheese', 'Unknown command')])

def test_no_errs():
   run_command_suite('lkv-server', 'lkv-cli', [('ping', 'PONG')])