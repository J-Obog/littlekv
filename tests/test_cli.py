import subprocess

def test_no_connection():
   cli_proc = subprocess.Popen(['lkv-cli', 'ping'])
   exit_code = cli_proc.wait()
   assert exit_code == 737

def test_bad_arity():
   server_proc = subprocess.Popen(['lkv-server'])
   cli_proc = subprocess.Popen(['lkv-cli', 'get', 'chicken', 'noodle', 'soup'])
   exit_code = cli_proc.wait()
   server_proc.terminate()
   assert exit_code == 990

def test_no_command():
   server_proc = subprocess.Popen(['lkv-server'])
   cli_proc = subprocess.Popen(['lkv-cli', 'cheese'])
   exit_code = cli_proc.wait()
   server_proc.terminate()
   assert exit_code == 798