
Changelog
=========
v1.7.7 (2019/06/03)
-------------------
- Fixed problem with pybpod-gui-plugin-waveplayer.

v1.7.6 (2019/06/03)
-------------------
- Requirements for PyBpod now point to specific package versions to ease upgrades
- pybpod-api (updated to v1.6.4)
    - Fixed problem with bad indexing when accessing modules in _bpodcom_module_write
- pybpod-gui-plugin-waveplayer (v1.0)
    - Corrected version number in the package and PyPi

v1.7.5 (2019/05/15)
-------------------
- pybpod-gui-plugin (updated to v1.6.2)
    - Fixed png that was creating a warning on PyBpod initialization
    - Now it points correctly to the master branch
- pyforms-gui (updated to v4.901.2)
    - Version update so that PyPI considers a new version and the updates mentioned in v1.7.2 release are applied.
- pybpod-alyx-module (updated to v1.1.1)
    - Removed unnecessary requests package requirement
- pybpod-gui-plugin-emulator (v0.1.3)
    - Fixed override messages not being sent properly on Windows
    - Fix for pause not working
- pybpod-rotaryencoder-module (v0.1.1)
    - Fix for version override which would present always as version 0
- pybpod-soundcard-module (v0.1.5)
    - Added bumpversion support to this module

v1.7.4 (2019/05/08)
-------------------
- The pybpodgui_plugin_session_history is now pointing to the master branch as it should (v1.4.1)

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
    - pybpod-gui-plugin-emulator (v0.1). More details on this module in: https://pybpod-gui-plugin-emulator.readthedocs.io/en/v0.1.0/

