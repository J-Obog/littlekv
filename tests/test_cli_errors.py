from tests.helpers import (
   launch_client_proc,
   launch_server_proc,
   kill_server_proc
)

def test_bad_arity():
   spid = launch_server_proc('lkv-server')
   _, c, o = launch_client_proc('lkv-cli ping foobar')
   assert c == 0
   assert o.find('Wrong number of arguments') != -1
   kill_server_proc(spid)

def test_no_command():
   spid = launch_server_proc('lkv-server')
   _, c, o = launch_client_proc('lkv-cli cheese')
   assert c == 0
   assert o.find('Unknown command') != -1
   kill_server_proc(spid)

def test_no_errs():
   spid = launch_server_proc('lkv-server')
   _, c, o = launch_client_proc('lkv-cli ping')
   assert c == 0
   assert o.find('ERROR') == -1
   assert o.find('PONG') != -1
   kill_server_proc(spid)

def test_no_connection():
   _, c, o = launch_client_proc('lkv-cli ping')
   assert c == 0
   assert o.find('Unable to connect') != -1