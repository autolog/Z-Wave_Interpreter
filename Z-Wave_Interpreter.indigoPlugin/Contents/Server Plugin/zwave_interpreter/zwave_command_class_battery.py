#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_BATTERY_GET = 0x02
ZW_BATTERY_REPORT = 0x03
ZW_BATTERY_HEALTH_GET = 0x04
ZW_BATTERY_HEALTH_REPORT = 0x05


class ZwaveBattery:
    """
    Z-Wave Command Class: Battery "0x80" [Decimal 128]

    """

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_BATTERY] = dict()
            self.command_classes[ZW_BATTERY][ZW_IDENTIFIER] = "Battery"
            self.command_classes[ZW_BATTERY][ZW_COMMANDS] = dict()
            self.command_classes[ZW_BATTERY][ZW_COMMANDS][ZW_BATTERY_GET] = "Get"
            self.command_classes[ZW_BATTERY][ZW_COMMANDS][ZW_BATTERY_REPORT] = "Report"
            self.command_classes[ZW_BATTERY][ZW_COMMANDS][ZW_BATTERY_HEALTH_GET] = "Health Get Command"
            self.command_classes[ZW_BATTERY][ZW_COMMANDS][ZW_BATTERY_HEALTH_REPORT] = "Report Command"

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_BATTERY_GET:
                self._interpret_get()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_BATTERY_REPORT:
                self._interpret_report()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_BATTERY_HEALTH_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_BATTERY_HEALTH_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_get(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}'")

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_report(self):
        try:
            battery_level = int(self.zw_interpretation[ZW_COMMAND_DETAIL][0])
            if battery_level > 100:
                battery_level = 255
            self.zw_interpretation[ZW_BATTERY_LEVEL] = battery_level
            if battery_level == 255:
                self.zw_interpretation[ZW_BATTERY_LEVEL_UI] = "Low"
            else:
                self.zw_interpretation[ZW_BATTERY_LEVEL_UI] = f"{battery_level}%"
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Battery Level: {self.zw_interpretation[ZW_BATTERY_LEVEL_UI]}")

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
