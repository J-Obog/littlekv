# Little KV

![Travis CI Badge](https://app.travis-ci.com/J-Obog/littlekv.svg?branch=main)

Little KV (LKV) is a lightweight key-value store (think Redis, Couchbase on a much smaller scale) written in Python that leverages in-memory storage to minimize read/write times. LKV also uses websocketing for client-server communication in order to minimize latency.

Full list of supported commands: [commands.md](/docs/commands.md)

## Setup

#### Cloning the repo

Make sure that you have the latest version of [Python](https://www.python.org/downloads/) installed on your machine. To download the source code, run:

```
git clone https://github.com/J-Obog/littlekv.git
```

#### Pipenv

This project uses pipenv for dependency management and creating virtual environments. To install pipenv, run:

```
pip install pipenv
```

The required packages are listed in the Pipfile. To install those dependencies, run:

```
pipenv install
```

## Running LKV

#### Default configurations

The [lkv.config](/lkv.config) toml file holds informations regarding the project environment such the default host and port for the server to run on.
You can edit the content and provide your own custom default settings.

#### Running the server

To run the LKV server with the default configurations, simply run:

```
lkv-server
```

You can also pass in additional parameters through the command line:

```
usage: lkv-server [-h HOST] [-p PORT] [-d KV_DIR] [-s KV_SRC] [-H]

LittleKV Server

optional arguments:
  -h HOST, --host HOST  host server should run on
  -p PORT, --port PORT  port server should run on
  -d KV_DIR, --dir KV_DIR
                        directory of target kv file
  -s KV_SRC, --src KV_SRC
                        name of target kv file
  -H, --help            show this help message and exit
```

Example usage:

```
$ lkv-server
Server listening @ 127.0.0.1 on port 9876
```

#### Running the CLI

LittleKV comes equipped with a command line interface that you can use to run commands.
To run the LKV CLI with the default configurrations, simply run:

```
lkv-cli
```

You can also pass in additional parameters through the command line:

```
usage: lkv-cli [-h HOST] [-p PORT] [-H] command [command ...]

LittleKV CLI

positional arguments:
  command               lkv commands

optional arguments:
  -h HOST, --host HOST  host client should connect to
  -p PORT, --port PORT  port client should connect to
  -H, --help            show this help message and exit
```

Example usage:

```
$ lkv-cli ping
PONG
$ lkv-cli set foo bar
OK
$ lkv-cli get foo
bar
$ lkv-cli clear
OK
$ lkv-cli count
0
```
