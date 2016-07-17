Hotswappy
=========

Contents:

.. toctree::
   :maxdepth: 2


Preface
-------

Hotswappy lets you reload modified Python source files on demand.



Tutorial
--------

Create a new directory tree for the project:

.. code-block:: bash

   demo/
   |    main.py
   |    plugins/
        |    __init__.py
        |    test_plugin.py


Install hotswappy with pip:

.. code-block:: python

   pip install hotswappy

Create ``main.py``:

.. code-block:: python

   import hotswappy
   import plugins

   hotswap = hotswappy.Controller(plugins)
   hotswap.load()

   while True:
       print '\n', hotswap.plugins['test_plugin'].hello_world
       response = raw_input('>>> Press Enter to reload (Y to quit): ')
       if response.lower() == 'y': break
       hotswap.hotswap()

Create ``plugins/__init__.py``:

.. code-block:: python

   from test_plugin import *

Create ``plugins/test_plugin.py``:

.. code-block:: python

   from hotswappy import Plugin

   class TestPlugin(Plugin):
       name = 'test_plugin'
       hello_world = 'Hello world!'

Run ``python main.py``:

.. code-block:: python

   [tay@taybird example]$ python main.py

   Hello world!
   >>> Press Enter to reload (Y to quit):

Open an editor and change the ``hello_world`` attribute in
``plugins.test_plugin``. Go back to the running Python process and
press Enter to see the change:

.. code-block:: bash

   [tay@taybird example]$ python main.py

   Hello world!
   >> Press Enter to reload (Y to quit):

   Hello world! I changed this!


API
---

Controller
~~~~~~~~~~

.. autoclass:: hotswappy.Controller
   :members:

Plugin
~~~~~~

.. autoclass:: hotswappy.Plugin
   :members:
