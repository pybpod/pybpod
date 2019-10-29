.. _developing_plugins-label:

******************
Developing plugins
******************

============================
What is a PyBpod GUI plugin?
============================

**PyBpod** relies on a generic GUI framework, called **PyformsGenericEditor** which offers a basic user interface and can be extended to provide specific functionality through the installation of plugins.

You can use plugins for:
    * extending or overwriting PyBpod core concepts (e.g., experiments, subjects, boxes);
    * creating new visualization tools for PyBpod sessions (e.g., plots, message filters);
    * adding new windows, tools or any other UI-related functionality;

Each plugin will be associated with a specific element of **PyformsGenericEditor** (e.g., project tree node, menu option, workspace area, etc).

==================================
Session history plugin, an example
==================================

This plugin allows you to display session data in a table view and you can order events by column.

https://github.com/pybpod/pybpod-gui-plugin-session-history

.. image:: /_images/basic-usage/session_history.png
    :scale: 100 %

Quick review on sessions
------------------------
Each time you run a Bpod protocol on a subject, a new session is created. The GUI collects output from the PyBpod API and processes these events on a list (which we call session history).
Besides being on memory, this history is automatically saved on a text file, so you never loose Bpod data.

If you navigate to your project on the filesystem, and locate the desired subject, you should find several files:

    * CSV and JSON are default outputs from the pybpod-api (for example, you can open CSV on excel and quickly produce some plots)
    * Plain text file is the output from the GUI

.. image:: /_images/basic-usage/session_data_filesystem.png
    :scale: 100 %

Let's take a look at a plain text file which was output from running a protocol on the GUI.

.. code-block:: text

    print_statement, 2017-05-23T15:41:29.638353, Trial:
    print_statement, 2017-05-23T15:41:29.654188, Waiting for poke. Reward:
    event_occurrence, 2017-05-23T15:41:33.672094, 50, Port2In, 2017-05-23 15:41:33.672094
    event_occurrence, 2017-05-23T15:41:33.771925, 88, Tup, 2017-05-23 15:41:33.771925
    state_entry, 2017-05-23T15:41:41.324848, 3, WaitForResponse, 4.1312, 4.3405
    state_entry, 2017-05-23T15:41:41.324861, 4, Punish, 4.3405, 11.6663
    state_entry, 2017-05-23T15:41:41.324908, 5, Reward, nan, nan
    state_change, 2017-05-23T15:41:41.324930, 1, Port2In, 4.0312
    state_change, 2017-05-23T15:41:41.324939, 2, Tup, 4.1312
    state_change, 2017-05-23T15:41:41.324947, 2, Tup, 11.6663
    print_statement, 2017-05-23T15:41:42.317543, Current trial info: {'Bpod start timestamp': 0.011, 'States timestamps': {'WaitForPort2Poke': [(0, 4.0312)], 'FlashStimulus': [(4.0312, 4.1312)], 'WaitForResponse': [(4.1312, 4.3405)], 'Punish': [(4.3405, 11.6663)], 'Reward': [(nan, nan)]}, 'Events timestamps': {'Port2In': [4.0312], 'Tup': [4.1312, 11.6663], 'Port2Out': [4.3405], 'Port3In': [8.6663], 'Port3Out': [8.8762]}}
    print_statement, 2017-05-23T15:41:42.322411, Trial:
    print_statement, 2017-05-23T15:41:42.325805, Waiting for poke. Reward:
    event_occurrence, 2017-05-23T15:41:48.035732, 48, Port1In, 2017-05-23 15:41:48.035732
    event_occurrence, 2017-05-23T15:41:48.136440, 88, Tup, 2017-05-23 15:41:48.136440
    state_entry, 2017-05-23T15:41:48.160769, 3, WaitForResponse, 3.2538, 3.4102
    state_entry, 2017-05-23T15:41:48.160775, 4, Reward, 3.4102, 5.8133
    state_entry, 2017-05-23T15:41:48.160781, 5, Punish, nan, nan
    state_change, 2017-05-23T15:41:48.160791, 1, Port2In, 3.1538
    state_change, 2017-05-23T15:41:48.160804, 3, Port2Out, 3.4102
    state_change, 2017-05-23T15:41:48.160808, 4, Port1In, 5.7133
    print_statement, 2017-05-23T15:41:49.142529, Current trial info: {'Bpod start timestamp': 12.689, 'States timestamps': {'WaitForPort2Poke': [(0, 3.1538)], 'FlashStimulus': [(3.1538, 3.2538)], 'WaitForResponse': [(3.2538, 3.4102)], 'Reward': [(3.4102, 5.8133)], 'Punish': [(nan, nan)]}, 'Events timestamps': {'Port2In': [3.1538], 'Tup': [3.2538, 5.8133], 'Port2Out': [3.4102], 'Port1In': [5.7133]}}
    print_statement, 2017-05-23T15:41:49.147563, Trial:
    print_statement, 2017-05-23T15:41:49.151724, Waiting for poke. Reward:
    event_occurrence, 2017-05-23T15:41:52.731798, 50, Port2In, 2017-05-23 15:41:52.731798
    event_occurrence, 2017-05-23T15:41:53.845332, 48, Port1In, 2017-05-23 15:41:53.845332
    event_occurrence, 2017-05-23T15:41:53.946396, 88, Tup, 2017-05-23 15:41:53.946396
    state_entry, 2017-05-23T15:41:53.974354, 1, WaitForPort2Poke, 0, 3.5869
    state_entry, 2017-05-23T15:41:53.974475, 5, Punish, nan, nan
    state_change, 2017-05-23T15:41:53.974495, 1, Port2In, 3.5869
    state_change, 2017-05-23T15:41:53.974536, 3, Port2Out, 3.8881
    state_change, 2017-05-23T15:41:53.974545, 4, Port1In, 4.7007
    print_statement, 2017-05-23T15:41:54.955371, Current trial info: {'Bpod start timestamp': 19.513, 'States timestamps': {'WaitForPort2Poke': [(0, 3.5869)], 'FlashStimulus': [(3.5869, 3.6869)], 'WaitForResponse': [(3.6869, 3.8881)], 'Reward': [(3.8881, 4.8007)], 'Punish': [(nan, nan)]}, 'Events timestamps': {'Port2In': [3.5869], 'Tup': [3.6869, 4.8007], 'Port2Out': [3.8881], 'Port1In': [4.7007]}}

What is going on here? Each line is a new message, where the first column identifies the type of an event on the session history: it can be a bpod state change, state entry, a user print, etc.
These events represent messages that were sent from the Bpod and processed by the GUI.

Parsing board messages
----------------------

Currently, PyBpod GUI supports the following events from Bpod board:

=================================================================================  ===========================  ====================================================================================================
Session History Event Type                                                         Occurs during trial run?     Description
=================================================================================  ===========================  ====================================================================================================
:ref:`Event occurrence <api_reference_event_occurrence-label>`                     YES                          Any Bpod event during trial run
:ref:`State change <api_reference_state_change-label>`                             NO                           Events detected by Bpod’s inputs can be set to trigger transitions between specific states.
:ref:`State entry <api_reference_state_entry-label>`                               NO                           State entered during the state matrix run
:ref:`Print statement <api_reference_print_statement-label>`                       YES                          User defined print messages on protocol
=================================================================================  ===========================  ====================================================================================================

All these classes represent board messages and inherit a generic class :ref:`BoardMessage <api_reference_board_message-label>`.
For more information on how the GUI parses these messages, see :ref:`Message factory <api_reference_msg_factory-label>`.


Register plugin on the GUI
--------------------------

The first thing you need to do is to register your plugin. For that, edit your user settings. From the top menu, go to **Options > Edit user settings**.
Edit the :py:class:`GENERIC_EDITOR_PLUGINS_PATH` variable as this:

.. code-block:: python

        GENERIC_EDITOR_PLUGINS_LIST = [
        'pybpodgui_plugin',
        'pybpodgui_plugin_session_history',
    ]


For the GUI to be able to detect the plugin source code you have 2 options:
    1. Download the plugin folder you want and place it on the "plugins" folder you have just indicated before (useful when you run pybpod GUI as an executable)
    2. Install the plugin with PIP (only applies if you are running the GUI from source code).

On this example, we will assume option #2 since we will be developing a plugin from the source code.
In that case, you may leave the :py:class:`GENERIC_EDITOR_PLUGINS_PATH = None` because the plugin will be already on the Python path.
**But don't forget! Every time you make changes to the plugin you have to install it with PIP again (unless your IDE does that for you).**

Finally, restart the GUI. The Session History plugin is a type of plugin that will be connected to a session and extend its behavior.
Thus, after installing this plugin, you will see a new option by right-clicking a session node in the project tree. But how this works?

Connecting the plugin with a session node
-----------------------------------------

Every node on the project tree node has a window assigned to it.
In order to plugins show up on a project tree node, we need to extend the corresponing node window behavior.
For example:

    * an experiment node is connected to the :py:class:`pybpodgui_api.models.experiment.experiment_treenode.ExperimentTreeNode` class
    * a board node is connected to the :py:class:`pybpodgui_api.models.board.board_treenode.BoardTreeNode` class
    * a session node is connected to the :py:class:`pybpodgui_api.models.session.session_treenode.SessionTreeNode` class

The **PyformsGenericEditor** enables that all these classes may be extended by looking for classes on plugins that have the same name and path.

On the Session History plugin, since we want to override session behavior we need to have the following structrure:

.. image:: /_images/advanced/module_session_treenode.png
    :scale: 100 %

On the *models.session.__init__.py* module, you must define the class that will override the original SessionTreeNode class.
If you inspect the *__init__.py* you will find this:

::

    from pybpodgui_plugin_session_history.models.session.session_treenode import SessionTreeNode as Session

By using Python inheritance, **PyformsGenericEditor** discovers that *SessionTreeNode* will match the original class from the GUI.

On the *session_treenode.py* file on our plugin, one can now redefine the behavior of the desired methods. In this case, we are overriding the
*create_treenode* method to add a new option when the user right-clicks the project tree node.
We also override other methods to personalize details such as window title or double-clicking.


.. code-block:: python

    (...)

    from pybpodgui_plugin_session_history.session_history import SessionHistory

    (...)

    class SessionTreeNode(object):
        def create_treenode(self, tree):
            """
            Extends create_treenode behavior by calling the parent and adding a new option
            when user right-clicks the node.

            See also: pybpodgui_api.models.session.session_treenode.SessionTreeNode.create_treenode

            """
            node = super(SessionTreeNode, self).create_treenode(tree)

            tree.add_popup_menu_option('History', self.open_session_history_plugin, item=self.node,
                                       icon=QIcon(conf.SESSIONLOG_PLUGIN_ICON))

            return node

        def node_double_clicked_event(self):
            super(SessionTreeNode, self).node_double_clicked_event()
            self.open_session_history_plugin()

        def open_session_history_plugin(self):
            if not hasattr(self, 'session_history_plugin'):
                self.session_history_plugin = SessionHistory(self)
                self.session_history_plugin.show()
                self.session_history_plugin.subwindow.resize(*conf.SESSIONLOG_PLUGIN_WINDOW_SIZE)
            else:
                self.session_history_plugin.show()

        def remove(self):
            if hasattr(self, 'session_history_plugin'): self.mainwindow.mdi_area -= self.session_history_plugin
            super(SessionTreeNode, self).remove()

        @property
        def name(self):
            return super(SessionTreeNode, self.__class__).name.fget(self)

        @name.setter
        def name(self, value):
            super(SessionTreeNode, self.__class__).name.fset(self, value)
            if hasattr(self, 'session_history_plugin'): self.session_history_plugin.title = value


This should be the final result:

.. image:: /_images/advanced/session_node_history.png
    :scale: 100 %



Handling session history from the plugin
----------------------------------------

On the previous section, we defined a new action for the session node.
We have done that by linking the "History" menu option to the method *open_session_history_plugin*.
Inside this method we invoke a class from the *session_history.py* module.

The *session_history.py* is responsible for creating a new window that shows up in the GUI workspace.
This window must inherit from *BaseWidget* in order to make use of the necessary PyForms controls.

Since the GUI holds session history on memory, a list of board messages, session plugins can easily access to this list and process the events as needed.
In our window, we will define a ControlList to list all the session history events. We will then define a timer that fires periodically to check for new messages and update the list.


.. code-block:: python

    (...)

    from pyforms.basewidget import BaseWidget
    from pyforms.controls import ControlProgress
    from pyforms.controls import ControlList

    (...)

    from pybpodgui_plugin.com.messaging import ErrorMessage
    from pybpodgui_plugin.com.messaging import PrintStatement
    from pybpodgui_plugin.com.messaging import StateChange
    from pybpodgui_plugin.com.messaging import StateEntry
    from pybpodgui_plugin.com.messaging import EventOccurrence

    (...)

    class SessionHistory(BaseWidget):
        """ Plugin main window """

        def __init__(self, session):
            (...)

            self._log = ControlList()

            self._formset = [
                '_log',
            ]

            self._history_index = 0
            self._log.readonly = True
            self._log.horizontal_headers = ['#', 'Type', 'Name', 'Channel Id', 'Start', 'End', 'PC timestamp']
            self._log.set_sorting_enabled(True)

            (...)

            self._timer = QTimer()
            self._timer.timeout.connect(self.read_message_queue)

        (...)

        def read_message_queue(self, update_gui=False):
            """ Update board queue and retrieve most recent messages """
            messages_history = self.session.messages_history
            recent_history = messages_history[self._history_index:]

            if update_gui:
                self._progress.show()
                self._progress.value = 0
            try:
                for message in recent_history:

                    table_line = None
                    if issubclass(type(message), StateChange):
                        table_line = (self._history_index, message.MESSAGE_TYPE_ALIAS, message.event_name,
                                      '-', message.board_timestamp, message.board_timestamp, str(message.pc_timestamp))

                    if issubclass(type(message), StateEntry):
                        table_line = (self._history_index, message.MESSAGE_TYPE_ALIAS, message.state_name,
                                      '-', message.start_timestamp, message.end_timestamp, str(message.pc_timestamp))

                    if issubclass(type(message), EventOccurrence):
                        table_line = (self._history_index, message.MESSAGE_TYPE_ALIAS, message.event_name,
                                      message.event_id, '-', '-', str(message.pc_timestamp))

                    if table_line:
                        self._log += table_line
                        QEventLoop()

                        if update_gui:
                            self._progress += 1
                            if self._progress.value >= 99: self._progress.value = 0

                    self._history_index += 1

            except Exception as err:
                if hasattr(self, '_timer'):
                    self._timer.stop()
                logger.error(str(err), exc_info=True)
                QMessageBox.critical(self, "Error",
                                     "Unexpected error while loading session history. Pleas see log for more details.")

            if update_gui:
                self._progress.hide()

        (...)


This should be the final result:

.. image:: /_images/advanced/session_history_window_closeup.png
    :scale: 100 %


..
    [5:06]
    let’s go straight to the point

    [5:06]
    line 82

    [5:06]
    you have a for cycle

    [5:06]
    where we iterate recent_history structure

    [5:07]
    messages_history -> all messages from the beguinning

    [5:07]
    recent_history -> all messages not read yet

    Boaz Mohar [5:08 PM]
    Yep, got it

    Carlos Mão de Ferro [5:08 PM]
    so now

    [5:08]
    this is a list of messages that can have several “types”

    [5:08]
    so we must check

    [5:08]
    the type we want

    [5:08]
    if issubclass(type(message), StateChange):

    [5:08]
    is it a state change?

    [5:08]
    if issubclass(type(message), StateEntry):

    [5:08]
    or a state entry?

    [5:08]
    for example..

    [5:09]
    if it is a state change

    [5:09]
    `table_line = (self._history_index, message.MESSAGE_TYPE_ALIAS, message.event_name,'-',message.board_timestamp, message.board_timestamp, str(message.pc_timestamp))` (edited)

    [5:10]
    we can access event name

    [5:10]
    and board_timestamp



