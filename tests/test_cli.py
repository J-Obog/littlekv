import subprocess
import time
import signal
import os
import sys

def test_bad_arity():
   server_proc = subprocess.Popen(['lkv-server'])
   time.sleep(1)
   cli_proc = subprocess.Popen(['lkv-cli', 'ping', 'foobar'])
   exit_code = cli_proc.wait()
   if sys.platform == 'win32' or sys.platform == 'win64':
      os.kill(server_proc.pid, signal.CTRL_C_EVENT)
   else:
      os.kill(server_proc.pid, signal.SIGINT)
   time.sleep(1)
   assert exit_code == 990

def test_no_connection():
   cli_proc = subprocess.Popen(['lkv-cli', 'ping'])
   exit_code = cli_proc.wait()
   assert exit_code == 737

def test_no_command():
   server_proc=subprocess.Popen(['lkv-server'])
   time.sleep(1)
   cli_proc = subprocess.Popen(['lkv-cli', 'cheese'])
   exit_code = cli_proc.wait()
   if sys.platform == 'win32' or sys.platform == 'win64':
      os.kill(server_proc.pid, signal.CTRL_C_EVENT)
   else:
      os.kill(server_proc.pid, signal.SIGINT)
   time.sleep(1)
   assert exit_code == 798