Usage
=====

.. _installation:

Installation
------------

To install nari using pip:

.. code-block:: console

    (env) $ pip install nari

To install nari from the github repo:

.. code-block:: console

    (env) $ pip install git+https://github.com/xivlogs/nari.git@master#egg=nari

Basic Usage
-----------

The simplest usage for nari is to iterate through events with a reader

.. code-block:: python3

    from nari.ext.act import ActLogReader

    for event in ActLogReader('/path/to/log/file'):
        print(event)
