# NARI

![Test](https://github.com/nonowazu/nari/workflows/Test/badge.svg?branch=master) ![Docs](https://github.com/nonowazu/nari/workflows/Docs/badge.svg?branch=master)

The Nonowazu ACT Reference Implementation (NARI) is a Python library to parse Final Fantasy XIV game data from network logs in ACT in an abstract form more suited towards programmatic processing. The goals of this project are threefold:

1. Provide a clean set of documentation around the parsed events from ACT logs.
2. Provide an easy to use programmatic interface to interact with this data.
3. Provide a clean 'reference implementation' to hopefully standardise processing pipelines

To that end, nari operates on 'streams' of data – most of the core code operates on this concept either generating, transforming, or receiving events.

## Installation and Use

### Prerequisites

* Python 3.8 (untested at current, but should work with python 3.7)
* A newish version of setuptools

Clone the repo and install with `python setup.py install` (or `python setup.py develop`)

### Example

A simple example might be loading an ACT network log and viewing only the actions used in-game. To do that, set up an appropriate reader and filter, and then you can interact with the data:

```python
from nari.io.actlog import ActLogReader # To read ACT network logs
from nari.parser.normaliser import Normaliser # To filter ACT log data
from nari.types.event import Type as EventType # To aid with filtering

class ActionFilter(Normaliser):
    def on_event(self, event):
        # This allows you to filter, transform, or generate events.
        # Here, we're using it to filter only to the events we care about
        if event.id == EventType.networkability:
            return event
        return None # Returning none removes it from the stream

# set up an act log reader
reader = ActLogReader('/path/to/your/reader.log')
# A normalizer takes a stream of events – which ActLogReader provides
action_events = ActionFilter(reader)
# iterate through the events and handle them in interesting ways!
for action_event in action_events:
    print(action_event)
```

## Contributing

Anyone can contribute, so long as contributions are keeping with the goals of the project. PRs are welcome, but make sure your code lints (with `pylint`) and has 3.7-style annotations. To view the docs locally or lint the project, run `pip install .[docs]` or `pip install .[dev]` and run either `pdoc --html -f -o docs nari` or `pylint nari`