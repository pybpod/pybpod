.. _writing-protocols-label:

***************************
Writing a protocol for Bpod
***************************

What is a Bpod protocol?
========================

To use Bpod, you must first program a behavioral protocol. The following guide is based on the original version for `Bpod Matlab <https://sites.google.com/site/bpoddocumentation/bpod-user-guide/protocol-writing>`_.


Protocol example explained
==========================

First, you will need to import Bpod modules.

.. code-block:: python
    :linenos:
    :lineno-start: 1

        # Bpod main module and State machine module
        from pybpodapi.protocol import Bpod, StateMachine 

Then, initialize Bpod. The GUI will automatically set the serial port based on the serial port selected for the board and the workspace will be the subject folder.

.. code-block::python
    :linenos:
    :lineno-start: 5

        ﻿my_bpod = Bpod()


You can run several trials for each Bpod execution. In this example, we will use 5 trials. Each trial can be of type1 (rewarded left) or type2 (rewarded right).

.. code-block:: python
    :linenos:
    :lineno-start: 6

        nTrials = 5
        trialTypes = [1, 2]  # 1 (rewarded left) or 2 (rewarded right)

        for i in range(nTrials):  # Main loop
            print('Trial: ', i+1)
            thisTrialType = random.choice(trialTypes)  # Randomly choose trial type =
            if thisTrialType == 1:
                stimulus = 'PWM1'  # set stimulus channel for trial type 1
                leftAction = 'Reward'
                rightAction = 'Punish'
                rewardValve = 1
            elif thisTrialType == 2:
                stimulus = 'PWM3'  # set stimulus channel for trial type 1
                leftAction = 'Punish'
                rightAction = 'Reward'
                rewardValve = 3


Now, inside the loop, we will create and configure a state machine for each trial.
A state machine has *state name*, *state timer*, *names of states to enter if certain events occur* and *output actions*.
Please see :ref:`State Machine API <api_state_machine-label>` for detailed information about state machine design.

.. code-block:: python
    :linenos:
    :lineno-start: 22

            sma = StateMachine(my_bpod.hardware)

            sma.add_state(
                state_name='WaitForPort2Poke',
                state_timer=1,
                state_change_conditions={'Port2In': 'FlashStimulus'},
                output_actions=[(OutputChannel.PWM2, 255)])
            sma.add_state(
                state_name='FlashStimulus',
                state_timer=0.1,
                state_change_conditions={'Tup': 'WaitForResponse'},
                output_actions=[(stimulus, 255)])
            sma.add_state(
                state_name='WaitForResponse',
                state_timer=1,
                state_change_conditions={'Port1In': leftAction, 'Port3In': rightAction},
                output_actions=[])
            sma.add_state(
                state_name='Reward',
                state_timer=0.1,
                state_change_conditions={'Tup': 'exit'},
                output_actions=[('Valve', rewardValve)])  # Reward correct choice
            sma.add_state(
                state_name='Punish',
                state_timer=3,
                state_change_conditions={'Tup': 'exit'},
                output_actions=[('LED', 1), ('LED', 2), ('LED', 3)])  # Signal incorrect choice


After configuring the state machine, we send it to the Bpod device by calling the method *send_state_machine*. We are then ready to run the next trial, by calling the *run_state_machine* method.
On run completion, we can print the data available for the current trial including events and states.

.. code-block:: python
    :linenos:
    :lineno-start: 49

            my_bpod.send_state_machine(sma)  # Send state machine description to Bpod device

            print("Waiting for poke. Reward: ", 'left' if thisTrialType == 1 else 'right')

            my_bpod.run_state_machine(sma)  # Run state machine

            print("Current trial info: ", my_bpod.session.current_trial())



Finally, after the loop finishes, we can stop Bpod execution.

.. code-block:: python
    :linenos:
    :lineno-start: 56

        my_bpod.close()  # Disconnect Bpod and perform post-run actions

.. seealso::

    `PyBpod API <http://pybpod-api.readthedocs.io/en/latest/>`_

