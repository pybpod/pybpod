.. pybpodapi documentation master file, created by
   sphinx-quickstart on Wed Jan 18 09:35:10 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

**************************************
Welcome to PyBpod's documentation!
**************************************

.. note::

   All examples and Bpod's state machine and communication logic were based on the original version made available by `Josh Sanders (Sanworks) <https://github.com/sanworks>`_.

What is PyBpod?
===================

.. image:: /_images/bpod_gui_sample.png

**PyBpod** is a GUI application that enables interaction with the latest `Bpod device <https://sanworks.io/shop/viewproduct?productID=1011>`_ version.

This project is maintained by a team of SW developers at the `Champalimaud Foundation <http://research.fchampalimaud.org>`_. Please find more information on section :ref:`Project Info <project-info-label>`.

What is Bpod?
-------------

.. image:: /_images/pybpodapi-logo.png


**Bpod** is a system from `Sanworks <https://sanworks.io/index.php>`_ for precise measurement of small animal behavior.
It is a family of open source hardware devices which includes also software and firmware to control these devices. The software was originally developed in Matlab providing retro-compatibility with the `BControl <http://brodywiki.princeton.edu/bcontrol/index.php/Main_Page>`_ system.

.. seealso::

    Bpod device: https://sanworks.io/shop/viewproduct?productID=1011

    Bpod on Github: https://github.com/sanworks/Bpod

    Bpod Wiki: https://sites.google.com/site/bpoddocumentation/

    BControl project: http://brodywiki.princeton.edu/bcontrol/index.php/Main_Page/


Why a Python port?
------------------
Python is one of the most popular programming languages today `[1] <https://pypl.github.io/PYPL.html>`_. This is special true for the science research community because it is an open language, easy to learn, with a strong support community and with a lot of libraries available.

Questions?
==========
If you have any questions or want to report a problem with this library please fill in an issue `here <https://bitbucket.org/fchampalimaud/pybpod-api/issues>`_.

Contents
========

.. high level toc tree

.. toctree::
   :maxdepth: 2
   :includehidden:
   :caption: Getting started

   Introduction <self>
   getting-started/install
   getting-started/basic-usage
   getting-started/writing-protocols
   getting-started/plugins

.. toctree::
   :maxdepth: 2
   :includehidden:
   :caption: Developers

   developers/gui_explained
   developers/gui_windows
   developers/bpod_interaction
   developers/developing_plugins
   developers/contributing

.. toctree::
   :maxdepth: 4
   :includehidden:
   :caption: API reference

   PyBpod API <https://pybpod-api.readthedocs.io/>
   
.. toctree::
   :maxdepth: 4
   :includehidden:
   :caption: About

   about/about
   about/changelog

.. toctree::
   :hidden:
   :maxdepth: 2
   :includehidden:
   :caption: Contents

   contents

