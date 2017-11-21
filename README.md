# PyBpod #

PyBpod is a GUI application that enables interaction with the Bpod device from [Sanworks](https://sanworks.io/).

This project is maintained by a team of SW developers at the Champalimaud Foundation. 

### Install PyBpod project ###

1. Download & install [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://conda.io/miniconda.html) project.

2. Download the environment configuration file for your Operating System ( [Windows 10](https://bitbucket.org/fchampalimaud/pybpod/raw/e6c1c8da96c240ae638309359a97b28a2d36ca55/environment-windows-10.yml) ) and create a virtual environment with it by executing the following commands in the "Anaconda Prompt".
```
conda env create -f environment-windows-10.yml
```

3. Activate the environment you just created.
```
activate pybpod-environment
```
4. Clone the PyBpod repository.
```
git clone https://UmSenhorQualquer@bitbucket.org/fchampalimaud/pybpod.git
```
5. Run the install script to install all necessary dependencies.
```
python install.py
```
6. Run the PyBpod application.
```
python -m pybpodgui_plugin
```

### Execute PyBpod GUI ###

1. Open "Anaconda Prompt" and activate the "pybpod-environment".
```
activate pybpod-environment
```
2. Run the application.
```
python -m pybpodgui_plugin
```

### Update PyBpod GUI ###

1. Open the "Anaconda Prompt" and activate the "pybpod-environment".
```
activate pybpod-environment
```
2. Execute the script "update.py".
```
python update.py
```