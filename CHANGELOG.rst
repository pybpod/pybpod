
Changelog
=========

v1.7.3 (2019/05/08)
-------------------
- Fixed problem with wrong pybpod-alyx-module version (now it is v1.1)

v1.7.2 (2019/05/03)
-------------------
- Python base version changed to v3.6.6
- Conda environment files are now more coherent between Windows and Linux
- pybpod-api (updated to v1.6.3)
    - Data from interrupted trials are ignored
    - Added new trigger_input message to manually override inputs and trigger events
    - Fixed manual override of output channels
    - Fixed problem with GlobalTimers that were writing to the wrong indexes
    - Added new 'message' options to send serial messages to the modules connected to BPod's State Machine
- pybpod-gui-api (updated to v1.2.2)
    - Setups ran through a subject are now ran correctly
    - Added PYBPODGUI_API_AUTO_SAVE_PROJECT_ON_RUN option to user_settings
    - ScriptCmds are now executed as subprocesses
- pybpod-gui-plugin (updated to v1.6.1)
    - Fixed bug when subject were added to setups when canceling the confirmation dialog
    - Subject window now works properly and with the same options as within the setup (run, pause, detach from GUI option)
    - Fixed path problem in Pre and Post commands on Windows that prevented to run Pre and Post commands properly.
- pyforms-gui (updated to v4.9.2)
    - Code Editor now is presented properly on Windows
    - Normalized font labels size
- pybpod-alyx-module (updated to v1.1)
    - Import of Alyx subjects now allows to ignore all existing subject or replace all
    - Subjects that are dead, are now removed automatically from the list
- New modules and plugins
    - pybpod-soundcard-module (v0.1.4). More details on this module in: https://pybpod-soundcard-module.readthedocs.io/
    - pybpod-gui-plugin-emulator (v0.1) More details on this module in: https://pybpod-gui-plugin-emulator.readthedocs.io/en/v0.1.0/

