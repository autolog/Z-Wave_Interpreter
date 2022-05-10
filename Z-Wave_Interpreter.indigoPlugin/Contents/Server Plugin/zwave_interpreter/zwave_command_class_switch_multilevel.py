#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_SWITCH_MULTILEVEL_SET = 0x01
ZW_SWITCH_MULTILEVEL_GET = 0x02
ZW_SWITCH_MULTILEVEL_REPORT = 0x03
ZW_SWITCH_MULTILEVEL_START_LEVEL_CHANGE = 0x04
ZW_SWITCH_MULTILEVEL_STOP_LEVEL_CHANGE = 0x05
ZW_SWITCH_MULTILEVEL_SUPPORTED_GET = 0x06
ZW_SWITCH_MULTILEVEL_SUPPORTED_REPORT = 0x07


class ZwaveSwitchMultilevel:
    """
    Z-Wave Command Class: Switch Multilevel "0x20" [Decimal 32]

    """

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_SWITCH_MULTILEVEL] = dict()
            self.command_classes[ZW_SWITCH_MULTILEVEL][ZW_IDENTIFIER] = "Multilevel Switch"
            self.command_classes[ZW_SWITCH_MULTILEVEL][ZW_COMMANDS] = dict()
            self.command_classes[ZW_SWITCH_MULTILEVEL][ZW_COMMANDS][ZW_SWITCH_MULTILEVEL_SET] = "Set"
            self.command_classes[ZW_SWITCH_MULTILEVEL][ZW_COMMANDS][ZW_SWITCH_MULTILEVEL_GET] = "Get"
            self.command_classes[ZW_SWITCH_MULTILEVEL][ZW_COMMANDS][ZW_SWITCH_MULTILEVEL_REPORT] = "Report"
            self.command_classes[ZW_SWITCH_MULTILEVEL][ZW_COMMANDS][ZW_SWITCH_MULTILEVEL_START_LEVEL_CHANGE] = "Start Level Change"
            self.command_classes[ZW_SWITCH_MULTILEVEL][ZW_COMMANDS][ZW_SWITCH_MULTILEVEL_STOP_LEVEL_CHANGE] = "Stop Level Change"
            self.command_classes[ZW_SWITCH_MULTILEVEL][ZW_COMMANDS][ZW_SWITCH_MULTILEVEL_SUPPORTED_GET] = "Supported Get"
            self.command_classes[ZW_SWITCH_MULTILEVEL][ZW_COMMANDS][ZW_SWITCH_MULTILEVEL_SUPPORTED_REPORT] = "Supported Report"

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_SWITCH_MULTILEVEL_SET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SWITCH_MULTILEVEL_GET:
                self._interpret_get()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SWITCH_MULTILEVEL_REPORT:
                self._interpret_report()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SWITCH_MULTILEVEL_START_LEVEL_CHANGE:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SWITCH_MULTILEVEL_STOP_LEVEL_CHANGE:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SWITCH_MULTILEVEL_SUPPORTED_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_SWITCH_MULTILEVEL_SUPPORTED_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_get(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = ("Class: '{0} [{1}]', Command: '{2}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_report(self):
        try:
            value, value_bool, value_ui = self.utility.evaluate_value(self.zw_interpretation[ZW_COMMAND_DETAIL][0])  # noqa [Duplicated code fragment!]

            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_BOOL] = value_bool
            self.zw_interpretation[ZW_VALUE_UI] = value_ui

            self.zw_interpretation[ZW_INTERPRETATION_UI] = ("Class: '{0} [{1}]', Command: '{2}', value: '{3}' | {4} | '{5}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_VALUE],
                                                                    self.zw_interpretation[ZW_VALUE_BOOL],
                                                                    self.zw_interpretation[ZW_VALUE_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
