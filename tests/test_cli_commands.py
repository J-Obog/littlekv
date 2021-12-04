from tests.helpers import (
   launch_client_proc,
   launch_server_proc,
   kill_server_proc
)

def test_set_and_get():
   spid = launch_server_proc('lkv-server')
   _, c, o = launch_client_proc('lkv-cli clear')
   assert c == 0
   assert o == 'OK'

   _, c, o = launch_client_proc('lkv-cli set foo bar')
   assert c == 0
   assert o == 'OK'

   _, c, o = launch_client_proc('lkv-cli get foo')
   assert c == 0
   assert o == 'bar'
   kill_server_proc(spid)


def test_set_and_del():
   spid = launch_server_proc('lkv-server')
   _, c, o = launch_client_proc('lkv-cli clear')
   assert c == 0
   assert o == 'OK'

   _, c, o = launch_client_proc('lkv-cli set foo bar')
   assert c == 0
   assert o == 'OK'

   _, c, o = launch_client_proc('lkv-cli del foo')
   assert c == 0
   assert o == 'OK'

   _, c, o = launch_client_proc('lkv-cli get foo')
   assert c == 0
   assert o == '<None>'
   kill_server_proc(spid)


def test_set_and_count():
   spid = launch_server_proc('lkv-server')
   _, c, o = launch_client_proc('lkv-cli clear')
   assert c == 0
   assert o == 'OK'

   _, c, o = launch_client_proc('lkv-cli count')
   assert c == 0
   assert o == '0'

   for i in range(5):
      _, c, o = launch_client_proc(f'lkv-cli set key-{i} somevalue')
      assert c == 0
      assert o == 'OK'

   _, c, o = launch_client_proc('lkv-cli count')
   assert c == 0
   assert o == '5'
   kill_server_proc(spid)

def test_matching_keys():
   spid = launch_server_proc('lkv-server')
   _, c, o = launch_client_proc('lkv-cli clear')
   assert c == 0
   assert o == 'OK'

   for i in range(5):
      kt = f'{i}2' if i % 2 == 0 else i
      _, c, o = launch_client_proc(f'lkv-cli set key-{kt} foobar')
      assert c == 0
      assert o == 'OK'

   _, c, o = launch_client_proc('lkv-cli keys .*2')
   assert c == 0
   assert o.find('key-02') != -1
   assert o.find('key-22') != -1
   assert o.find('key-42') != -1
   kill_server_proc(spid)
