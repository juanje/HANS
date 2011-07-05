

import os

import ActionSelectorDialog
from . import (DeviceEntry, InterfaceEntry)
from actions import *

class ActionLauncher:

    def __init__(self, interface_entry):
        self._interface_entry = interface_entry
        self._action_list = interface_entry.get_actions()

    def execute(self, action_list):

        for action_name in action_list:

            if not action_name in self._action_list:
                continue

            try:
                action_entry = self._action_list[action_name]
                action_instance = self._get_action_instance(action_entry)
                action_instance.execute(self._interface_entry)

            except Exception, e:
                raise e

    def _get_action_instance(self, action_entry):

        try:
            action_name = action_entry.getName() + 'Action'
            action_module = globals()[action_name]

        except KeyError, e:
            action_name = 'DefaultAction'
            action_module = globals()[action_name]

        action = None

        try:
            action = action_module.get_instance(action_entry)

        except Exception, e:
            raise e

        return action