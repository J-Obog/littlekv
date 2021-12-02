from tests.helpers import run_command_suite

def test_set_and_get():
   t = [('clear', 'OK'), ('set john doe', 'OK'), ('get john', 'doe')]
   run_command_suite('lkv-server', 'lkv-cli', t)


def test_set_and_del():
   t = [('clear', 'OK'), ('set foo bar', 'OK'), ('del foo', 'OK'), ('get foo', '<None>')]
   run_command_suite('lkv-server', 'lkv-cli', t)


def test_set_and_count():
   t = [('clear', 'OK')]

   for i in range(5):
      t.append((f'set key-{i} somevalue', 'OK'))

   t.append(('count', '5'))

   run_command_suite('lkv-server', 'lkv-cli', t)


def test_set_and_clear():
   t = [('clear', 'OK')]

   for i in range(10):
      t.append((f'set key-{i} somevalue', 'OK'))

   t.extend((('clear', 'OK'), ('count', '0')))
   
   run_command_suite('lkv-server', 'lkv-cli', t)
