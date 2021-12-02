from typing import Tuple, List
import subprocess
import time
import os
import signal
import sys

def launch_client_proc(cmd: str, conn_delay: int = 0.01) -> Tuple[int, int, str]:
    time.sleep(conn_delay)
    client_proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    exit_code = client_proc.wait()
    output = client_proc.communicate()[0].decode('utf-8')
    return (client_proc.pid, exit_code, output)

def launch_server_proc(cmd: str) -> Tuple[int]:
    server_proc = subprocess.Popen(cmd.split())
    return server_proc.pid

def kill_server_proc(pid: str, timeout: int = 0.01):
    if sys.platform[:-2] == 'win':
        os.kill(pid, signal.CTRL_C_EVENT)
    else:
        os.kill(pid, signal.SIGINT)
    time.sleep(timeout)


def run_command_suite(cmd_s: str, cmd_c: str, tests: List[Tuple[str, str]], verbose: bool = False):
    spid = launch_server_proc(cmd_s)

    for test in tests:
        try:
            _, exit_code, output = launch_client_proc(cmd_c + ' ' + test[0])
            
            if verbose:
                print((exit_code, output))

            assert exit_code == 0
            assert output.find(test[1]) != -1
        except AssertionError as err:
            kill_server_proc(spid)
            raise err

    kill_server_proc(spid)