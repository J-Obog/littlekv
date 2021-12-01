import subprocess
import os
import signal

def test_no_connection():
   cli_proc = subprocess.Popen(['lkv-cli', 'ping'])
   exit_code = cli_proc.wait()
   assert exit_code == 737

def test_bad_arity():
   server_proc = subprocess.Popen(['lkv-server'], shell=True)
   cli_proc = subprocess.Popen(['lkv-cli', 'get', 'chicken', 'noodle', 'soup'])
   exit_code = cli_proc.wait()
   os.kill(server_proc.pid, signal.SIGTERM)
   assert exit_code == 990

def test_no_command():
   server_proc = subprocess.Popen(['lkv-server'], shell=True)
   cli_proc = subprocess.Popen(['lkv-cli', 'cheese'])
   exit_code = cli_proc.wait()
   os.kill(server_proc.pid, signal.SIGTERM)
   assert exit_code == 798