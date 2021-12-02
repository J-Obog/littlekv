from tests.helpers import (
   launch_client_proc,
   launch_server_proc,
   kill_server_proc
)

def test_bad_arity():
   spid = launch_server_proc('lkv-server')
   _, ex_code, out = launch_client_proc('lkv-cli ping foobar')
   kill_server_proc(spid)
   assert ex_code == 0
   assert out.find('Wrong number of arguments') != -1

def test_no_connection():
   _, ex_code, out = launch_client_proc('lkv-cli ping')
   assert ex_code == 0
   assert out.find('Unable to connect') != -1

def test_no_command():
   spid = launch_server_proc('lkv-server')
   _, ex_code, out = launch_client_proc('lkv-cli cheese')
   kill_server_proc(spid)
   assert ex_code == 0
   assert out.find('Unknown command') != -1