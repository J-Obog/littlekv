# Little KV

![Travis CI Badge](https://app.travis-ci.com/J-Obog/littlekv.svg?branch=main)

Little KV (LKV) is a lightweight, key-value store (think Redis, Couchbase on a much smaller scale) written in Python that leverages in-memory storage to minimize read/write times. LKV also uses websocketing for client-server communication in order to minimize latency.

![LKV Architecture](/assets/lkv_architecture.svg)

## Setup

#### Installation

Make sure that you have the latest version of [Python](https://www.python.org/downloads/) installed on your machine.

You can clone this repository, install the requisite dependencies and run it on your machine like so:

```
git clone https://github.com/J-Obog/littlekv.git
cd littlekv
pipenv install
```
