# NARI

[![Tests](https://github.com/xivlogs/nari/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/xivlogs/nari/actions/workflows/test.yml)
[![Docs](https://github.com/xivlogs/nari/workflows/Docs/badge.svg?branch=master)](https://xivlogs.github.io/nari)
[![Discord](https://img.shields.io/discord/811093167290056735?color=7289da&label=Discord&logo=discord)](https://discord.gg/bdYYMSTxPg)

The Nonowazu ACT Reference Implementation (NARI) is a Python library to parse Final Fantasy XIV game data from network
logs in ACT in an abstract form more suited towards programmatic processing. The goals of this project are threefold:

1. Provide a clean set of documentation around parsed FFXIV network events structures and ACT logs
2. Provide an easy to use a programmatic interface to interact with this data
3. Provide a clean 'reference implementation' to hopefully standardise data analysis pipelines

To that end, nari operates on 'streams' of data – most of the core code operates on this concept either generating,
transforming, or receiving events.


## Installation and Use

nari has no runtime dependencies, you can use it on any recent version of Python.

### Prerequisites

* Python 3.10
* A newish version of setuptools

Clone the repo and install with `python setup.py install` (or `python setup.py develop`)

### Example

A simple example might be loading an ACT network log and viewing only the actions used in-game. To do that, set up an
appropriate reader and filter, and then you can interact with the data:

```python
from nari.io.reader.actlog import ActLogReader # To read ACT network logs

# set up an act log reader
reader = ActLogReader('/path/to/your/reader.log')
# iterate through the events and handle them in interesting ways!
for event in reader:
    print(event)
```


## Contributing

Anyone can contribute, so long as contributions are keeping with the goals of the project. PRs are welcome, but make
sure your code lints (with `pylint`), has 3.7-style type annotations, and unit tests. To view the docs locally or lint the project,
run `pip install .[docs]` or `pip install .[dev]` and run either `pdoc --html -f -o docs nari` or `pylint nari`

For further details on what we expect of contributors and how you can do so, please read our [contributors guide](https://github.com/xivlogs/nari/blob/master/.github/CONTRIBUTING.md).
