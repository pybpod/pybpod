.. pybpodapi documentation master file, created by
   sphinx-quickstart on Wed Jan 18 09:35:10 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _installing-label:

**********
Installing
**********


1. Download & install `Anaconda <https://www.anaconda.com/download/>`_ or `Miniconda <https://conda.io/miniconda.html>`_.
2. Download the environment configuration file for your Operating System ( `Windows 10 <https://bitbucket.org/fchampalimaud/pybpod/raw/e6c1c8da96c240ae638309359a97b28a2d36ca55/environment-windows-10.yml>`_, `Ubuntu 17.10 <https://bitbucket.org/fchampalimaud/pybpod/raw/9573598048ff6513fa22a6502f21dbb0111ebd1e/environment-ubuntu-17.10.yml>`_, `Mac OSx <https://bitbucket.org/fchampalimaud/pybpod/raw/8044a7903c0418a8b2b8579632a64125eaad6788/environment-macOSx.yml>`_ ) and create a virtual environment with it by executing the following commands in the "Anaconda Prompt".

.. code::

  conda env create -f utils/environment-windows-10.yml
  or 
  conda env create -f utils/environment-ubuntu-17.10.yml
  or 
  conda env create -f utils/environment-macOSx.yml

.. note::

  Windows
    * On windows if you install Anaconda/Miniconda for all the users, you should make sure you run the "Anaconda Prompt" as administrator.  
    * To avoid issues, make sure you install Anaconda/Miniconda only for your user.
  Linux
    * Make sure your user has permissions to access the serial ports.
    * Execute the next command:

      .. code::

        sudo usermod -a -G dialout [your username]

    * Restart the computer.


3. Activate the environment you just created.

.. code::

  activate pybpod-environment

4. Clone the PyBpod repository.

.. code::

  git clone https://bitbucket.org/fchampalimaud/pybpod.git

5. Access the created repository folder.

.. code::

  cd pybpod


6. Run the "install.py" script to install all necessary dependencies.

.. code::

  python utils/install.py

7. Run the PyBpod application.

.. code::

  start-pybpod


********************
Execute PyBpod GUI
********************

1. Open "Anaconda Prompt" and activate the "pybpod-environment".

.. code::

  activate pybpod-environment

2. Run the application, in your pybpod directory.

.. code::

  start-pybpod


*******************
Update PyBpod GUI
*******************

1. Open the "Anaconda Prompt" and activate the "pybpod-environment".

.. code::

  activate pybpod-environment

2. Execute the next commands in your pybpod directory.

.. code::

  git pull
  git submodule update --init
  git pull --recurse-submodules
  git submodule update --recursive