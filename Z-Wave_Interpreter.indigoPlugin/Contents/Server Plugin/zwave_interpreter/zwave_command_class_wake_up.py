#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_WAKE_UP_INTERVAL_SET = 0x04
ZW_WAKE_UP_INTERVAL_GET = 0x05
ZW_WAKE_UP_INTERVAL_REPORT = 0x06
ZW_WAKE_UP_NOTIFICATION = 0x07
ZW_WAKE_UP_NO_MORE_INFORMATION = 0x08
ZW_WAKE_UP_INTERVAL_CAPABILITIES_GET = 0x09
ZW_WAKE_UP_INTERVAL_CAPABILITIES_REPORT = 0x0A


class ZwaveWakeUp:
    """
    Z-Wave Command Class: Wake Up "0x84" [Decimal 132]

    """

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_WAKE_UP] = dict()
            self.command_classes[ZW_WAKE_UP][ZW_IDENTIFIER] = "Wakeup"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS] = dict()
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_INTERVAL_SET] = "Interval Set"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_INTERVAL_GET] = "Interval Get"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_INTERVAL_REPORT] = "Interval Report"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_NOTIFICATION] = "Notification"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_NO_MORE_INFORMATION] = "No More Information"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_INTERVAL_CAPABILITIES_GET] = "Interval Capabilities Get"
            self.command_classes[ZW_WAKE_UP][ZW_COMMANDS][ZW_WAKE_UP_INTERVAL_CAPABILITIES_REPORT] = "Interval Capabilities Report"

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_INTERVAL_SET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_INTERVAL_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_INTERVAL_REPORT:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_NOTIFICATION:
                self._interpret_wake_up_notification()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_NO_MORE_INFORMATION:
                self._interpret_wake_up_no_more_information()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_INTERVAL_CAPABILITIES_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_WAKE_UP_INTERVAL_CAPABILITIES_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_wake_up_no_more_information(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}'")

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_wake_up_notification(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}'")

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
