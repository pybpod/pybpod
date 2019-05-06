.. _gui_explained-label:

*************
GUI explained
*************




.. note::

    **Quick rationale**

    There are a lot of things going on under the hood when you run the **PyBpod GUI**.
    We will try to resume the basic concepts here but keep in mind that it is a lot of information so don't get frustrated if you don't get it at first.
    There were a lot of man-hours involved in this project and we strongly believe that dividing code in modules and libraries, though it seems more complicated at first, greatly improves code reusability and low-coupling.

==============================
Libraries that make up the GUI
==============================

Qt and PyQt
-----------

First, **PyBpod GUI** relies on `PyQt <https://riverbankcomputing.com/software/pyqt/intro>`_, a set of Python v2 and v3 bindings for `The Qt Company's <https://www.qt.io>`_ Qt application framework which runs on all platforms supported by Qt including Windows, OS X, Linux, iOS and Android.
Qt is more than a GUI toolkit. It includes abstractions of network sockets, threads, Unicode, regular expressions, SQL databases, SVG, OpenGL, XML, a fully functional web browser, a help system, a multimedia framework, as well as a rich collection of GUI widgets.

https://riverbankcomputing.com/software/pyqt/intro

PyForms
-------
Because developing complex applications with PyQt can be hard to maintain, we rely on **Pyforms**, a Python 2.7.x and 3.x cross-enviroment framework for developing GUI applications, which promotes modular software design and code reusability with minimal effort.

https://github.com/UmSenhorQualquer/pyforms

PyformsGenericEditor
--------------------

But we got even far, and since several GUI applications share the same concepts, we have developed **PyformsGenericEditor**, which allows for quickly bootstrapping a GUI application with file menus, project trees, form fields, etc.
It also abstracts the concepts of creating, saving and deleting projects. This generic editor can then be adapted for specific use cases by providing plugins which define how projects are saved on filesystem, how to populate the project tree, which options show up in the menus and so on.

Thus **PyBpod GUI** is itself a plugin for the **PyformsGenericEditor**.

.. image:: /_images/advanced/pge_overview_annotated.png
    :scale: 100 %

PyBpod API
----------
**Pybpod API** is a Python library that enables communication with the latest Bpod device version. It is responsible for translating the protocols you write into a state matrix array and send it to the Bpod device.

http://pybpod-api.readthedocs.io/en/latest/


Confapp
----------
Python library to provide settings files for modular applications.

https://github.com/UmSenhorQualquer/confapp


Pybranch
--------
Library that offers multiprocessing communication.

https://bitbucket.org/fchampalimaud/pybranch


Logging-bootstrap
-----------------
Library that provides simple methods for bootstrapping a logger with default settings.

https://bitbucket.org/fchampalimaud/logging-bootstrap