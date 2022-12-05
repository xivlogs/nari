Overview
========

nari revolves around 3 core concepts:

1. Events
2. Readers, which generate those events
3. Writers, which consume those events

Events
~~~~~~

The core of nari is its abstract events - events which represent various events
that happen in the game. While nari's core focuses on combat-focused events,
nothing stops a developer from subclassing Event and adding event types for
any type of action in the game (crafting, gathering, retainer actions, etc)

Readers
~~~~~~~

For a basic example of using readers, look at the `act extension <https://github.com/xivlogs/nari-act>`_:

.. code-block:: python

    from nari.ext.act import ActLogReader

    for event in ActLogReader('/path/to/act.log'):
        print(event)

All readers are iterators inherently, so you can use it in any python
function/method that consumes iterators.

.. caution::

    Some readers, like nari-act, can only consume the data one time before
    creating another instance; double-check the reader documentation before
    trying to use other iterator features (like slices)

Writers
~~~~~~~

Writers are as straightforward as readers in that they consume an iterator
which returns an event. You *could* hook up a reader directly to a writer in
order to change file formats, for example:

.. code-block:: python

    from nari.ext.act import ActLogReader
    from nari.io.writer.pickle import PickleWriter

    PickleWriter(ActLogReader('/path/to/act.log')).write()

You could also hand generate events and write those using a writer:

.. code-block:: python

    from nari.types.event import Event
    from nari.io.writer.pickle import PickleWriter

    events = [Event(timestamp=1), Event(timestamp=2), Event(timestamp=3)]
    PickleWriter(events).write()
