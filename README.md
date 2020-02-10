# PyBpod #

**version:** 1.8.2

PyBpod is a GUI application that enables interaction with the Bpod device from [Sanworks](https://sanworks.io/).

This project is maintained by a team of SW developers at the Champalimaud Foundation.

## Install PyBpod ##

1. Download & install [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://conda.io/miniconda.html) to your user.

2. After the installation, open "Anaconda Prompt"

3. Create a virtual environment for running PyBpod with Python 3.6

    ```bash
    conda create -n pybpod-environment python=3.6
    ```

4. Activate the environment you just created

    ```bash
    activate pybpod-environment
    ```

5. Install PyBpod through PyPI

    ```bash
    pip install pybpod
    ```

6. Run the application.

    ```bash
    start-pybpod
    ```

## Install PyBpod (for developers) ##

1. Download & install [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://conda.io/miniconda.html) .

    **Note:**
    On windows if you install Anaconda/Miniconda for all the users, you should make sure you run the "Anaconda Prompt" as administrator.
    To avoid issues, make sure you install Anaconda/Miniconda only for your user.

2. Create a virtual environment for running PyBpod with Python 3.6

    ```bash
    conda create -n pybpod-environment python=3.6
    ```

3. Activate the environment you just created.

    ```bash
    activate pybpod-environment
    ```

4. Clone the PyBpod repository.

    ```bash
    git clone https://github.com/pybpod/pybpod.git
    ```

5. Access the created repository folder.

    ```bash
    cd pybpod
    ```

6. Run the "install.py" script to install all necessary dependencies.

    ```bash
    python utils\install.py
    ```

7. Run the PyBpod application.

    ```bash
    start-pybpod
    ```

## Documentation ##

Documentation is available at ReadTheDocs: <https://pybpod.readthedocs.io/>

## Acknowledgments ##

PyVmMonitor is being used to support the development of this open source software. For more information please see [PyVmMonitor's web site](http://pyvmmonitor.com)
