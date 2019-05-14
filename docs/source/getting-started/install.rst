.. _installing-label:

***********************
Installing and updating
***********************

.. note::

  Linux
    * Make sure your user has permissions to access the serial ports.
    * Execute the next command:

      .. code::

        sudo usermod -a -G dialout [your username]

    * Restart the computer.


User installation
_________________

1. Install Python 3.6.
2. Install PyBpod from PyPi:

.. code::

  pip install pybpod

3. Execute PyBpod:

.. code::

  start-pybpod

.. note::

  On the first execution a user_settings.py file will be created on the User system folder.



Installation for developers
___________________________


1. Download & install `Anaconda <https://www.anaconda.com/download/>`_ or `Miniconda <https://conda.io/miniconda.html>`_.

.. warning::

  Windows
    * On windows if you install Anaconda/Miniconda for all the users, you should make sure you run the "Anaconda Prompt" as administrator.
    * To avoid issues, make sure you install Anaconda/Miniconda only for your user.

2. Download the environment configuration file for your Operating System and create a virtual environment with it by
executing the following commands in the "Anaconda Prompt".

   Windows 10: `environment-windows-10.yml <https://bitbucket.org/fchampalimaud/pybpod/raw/248b05a43c2d6059187fa33b609e425e0ef76026/utils/environment-windows-10.yml>`_ (right click->Save Link as):

   .. code::

      conda env create -f utils/environment-windows-10.yml

   Ubuntu 17.10 and up: `environment-ubuntu-17.10.yml <https://bitbucket.org/fchampalimaud/pybpod/raw/248b05a43c2d6059187fa33b609e425e0ef76026/utils/environment-ubuntu-17.10.yml>`_ (right click->Save Link as):

   .. code::

      conda env create -f utils/environment-ubuntu-17.10.yml

   Mac OSx: `environment-macOSx.yml <https://bitbucket.org/fchampalimaud/pybpod/raw/248b05a43c2d6059187fa33b609e425e0ef76026/utils/environment-macOSx.yml>`_ (right click->Save Link as):

   .. code::

      conda env create -f utils/environment-macOSx.yml

3. Activate the environment you just created.

.. code::

  activate pybpod-environment

4. Clone the PyBpod repository and initialize all the submodules.

.. code::

  git clone https://bitbucket.org/fchampalimaud/pybpod.git
  git submodule update --init
  
5. Access the created repository folder.

.. code::

  cd pybpod

6. Run the "install.py" script to install all necessary dependencies.

.. code::

  python utils/install.py

7. Run the PyBpod application.

.. code::

  start-pybpod


Execute PyBpod
______________

1. Open "Anaconda Prompt" and activate the "pybpod-environment".

.. code::

  activate pybpod-environment

2. Run the application, in your pybpod directory.

.. code::

  start-pybpod


Update PyBpod
_____________

1. Open the "Anaconda Prompt" and activate the "pybpod-environment".

.. code::

  activate pybpod-environment

2. Execute the next commands in your pybpod directory.

.. code::

  git pull
  git submodule update --recursive --remote
