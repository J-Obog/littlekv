from typing import Tuple
import subprocess
import time
import os
import signal
import sys

def launch_client_proc(cmd: str, conn_delay: int = 0.25) -> Tuple[int, int, str]:
    time.sleep(conn_delay)
    client_proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    exit_code = client_proc.wait()
    output = client_proc.communicate()[0].decode('utf-8').strip()
    return (client_proc.pid, exit_code, output)

def launch_server_proc(cmd: str) -> Tuple[int]:
    server_proc = subprocess.Popen(cmd.split())
    return server_proc.pid

def kill_server_proc(pid: str, timeout: int = 0.25):
    if sys.platform[:-2] == 'win':
        os.kill(pid, signal.CTRL_C_EVENT)
    else:
        os.kill(pid, signal.SIGINT)
    time.sleep(timeout)