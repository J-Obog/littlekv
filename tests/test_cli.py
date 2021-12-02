import subprocess
import time
import signal
import os
import sys

def test_bad_arity():
   server_proc = subprocess.Popen(['lkv-server'])
   time.sleep(1)
   cli_proc = subprocess.Popen(['lkv-cli', 'ping', 'foobar'], stdout=subprocess.PIPE)
   exit_code = cli_proc.wait()
   if sys.platform == 'win32' or sys.platform == 'win64':
      os.kill(server_proc.pid, signal.CTRL_C_EVENT)
   else:
      os.kill(server_proc.pid, signal.SIGINT)
   time.sleep(1)
   cli_out = cli_proc.communicate()[0].decode('utf')
   assert exit_code == 0
   assert cli_out.find('Wrong number of arguments') != -1

def test_no_connection():
   cli_proc = subprocess.Popen(['lkv-cli', 'ping'], stdout=subprocess.PIPE)
   exit_code = cli_proc.wait()
   cli_out = cli_proc.communicate()[0].decode('utf')
   assert exit_code == 0
   assert cli_out.find('Unable to connect') != -1

def test_no_command():
   server_proc=subprocess.Popen(['lkv-server'])
   time.sleep(1)
   cli_proc = subprocess.Popen(['lkv-cli', 'cheese'], stdout=subprocess.PIPE)
   exit_code = cli_proc.wait()
   if sys.platform == 'win32' or sys.platform == 'win64':
      os.kill(server_proc.pid, signal.CTRL_C_EVENT)
   else:
      os.kill(server_proc.pid, signal.SIGINT)
   time.sleep(1)
   cli_out = cli_proc.communicate()[0].decode('utf')
   assert exit_code == 0
   assert cli_out.find('Unknown command') != -1