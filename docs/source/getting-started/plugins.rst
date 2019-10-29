.. _plugins-label:

*******
Plugins
*******

PyBpod GUI can be enhanced with plugins. This way you can easily adapt the GUI for your needs.

You can use plugins for:

    * extending or overwriting basic PyBpod functionalities
    * creating new visualization tools for PyBpod sessions (e.g., plots, message filters)
    * adding new windows, tools or any other GUI-related functionality

For detailed information on how to develop plugins please see :ref:`Developing PyBpod GUI plugins <developing_plugins-label>`.

=================
Available Plugins
=================

PyBpod has several plugins and modules for different purposes.
The ones developed by our team are:

* Session history (`GitHub <https://github.com/pybpod/pybpod-gui-plugin-session-history>`_)
* Trial timeline (`GitHub <https://github.com/pybpod/pybpod-gui-plugin-trial-timeline>`_)
* Wave player (`GitHub <https://github.com/pybpod/pybpod-gui-plugin-waveplayer>`_)
* Alyx module (`GitHub <https://github.com/pybpod/pybpod-gui-plugin-alyx>`_)
* Rotary encoder module (`Documentation <https://pybpod-api-rotary-encoder-module.readthedocs.io/>`_, `GitHub <https://github.com/pybpod/pybpod-gui-plugin-rotaryencoder>`_)
* Harp Sound card module (`Documentation <https://pybpod-soundcard-module.readthedocs.io/>`_, `GitHub <https://github.com/pybpod/pybpod-gui-plugin-soundcard>`_)
* Emulator module (`Documentation <https://pybpod-gui-plugin-emulator.readthedocs.io/>`_, `GitHub <https://github.com/pybpod/pybpod-gui-plugin-emulator>`_)

More information can be found at the PyBpod's page in GitHub `here <https://github.com/pybpod>`_.

Community made plugins
----------------------

There are also some plugins developed by the PyBpod's community.
The following plugins were developed by the *de la Rocha* lab:

* Water calibration (`BitBucket <https://bitbucket.org/delaRochaLab/water-calibration-plugin/>`_)
* Graphics Trend plugin for 2FC tasks (`BitBucket <https://bitbucket.org/delaRochaLab/trend-2fc-plugin/src/master-3A/>`_)
* Raster plot visualization of live or recorded sessions (`BitBucket <https://bitbucket.org/delaRochaLab/raster-plugin/>`_)
* Sound calibration (`BitBucket <https://bitbucket.org/delaRochaLab/sound-calibration-plugin/src/master-3A/>`_)

.. warning::
    These plugins might not work with the latest PyBpod version. Please check their respective documentation to confirm for which PyBpod version they were developed.


======================
How to install plugins
======================

Installing plugins only takes 3 steps.

First, you will need to edit your user settings. On the top menu, go to **Options > Edit user settings**.
Then, locate the following labels:

    * :py:class:`GENERIC_EDITOR_PLUGINS_PATH` -> this variable expects a string value which should correspond to a filesystem folder path where your plugins are located
    * :py:class:`﻿GENERIC_EDITOR_PLUGINS_LIST` -> this variable expects a list of strings which are the names of the plugins to be loaded when the GUI starts up

.. warning::
    If you are using Windows OS, you must use double slash for paths. Example: GENERIC_EDITOR_PLUGINS_PATH =  'C:\\\\\\Users\\\\\\YOUR_NAME\\\\\\bpod_plugins'.

.. image:: /_images/basic-usage/user_settings_plugins.png
    :scale: 100 %

Second, download the plugin folder you want and place it on the "plugins" folder you have just indicated before.

Finally, restart the GUI. Depending on the kind of plugin, you will see a new option on the top menu or by right-clicking a node in the project tree.

.. note::
    If you are developing plugins and you already installed them with PIP, you may leave the :py:class:`GENERIC_EDITOR_PLUGINS_PATH = None` because they will be already on the Python path.

=============================
Examples of available plugins
=============================

Session history
---------------

This plugin allows you to display session data in a table view and you can order events by column.

https://github.com/pybpod/pybpod-gui-plugin-session-history

.. image:: /_images/basic-usage/session_history.png
    :scale: 100 %


Session timeline
----------------

This plugin displays trial states in a bar plot.

https://github.com/pybpod/pybpod-gui-plugin-timeline

.. image:: /_images/basic-usage/session_timeline.png
    :scale: 100 %
