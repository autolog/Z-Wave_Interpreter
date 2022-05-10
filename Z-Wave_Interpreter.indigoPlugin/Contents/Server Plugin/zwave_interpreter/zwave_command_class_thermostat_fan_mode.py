#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_THERMOSTAT_FAN_MODE_SET = 0x01  # noqa [Duplicated code fragment!]
ZW_THERMOSTAT_FAN_MODE_GET = 0x02
ZW_THERMOSTAT_FAN_MODE_REPORT = 0x03
ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET = 0x04
ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT = 0x05

ZW_THERMOSTAT_FAN_MODE_AUTO_LOW = 0x00
ZW_THERMOSTAT_FAN_MODE_LOW = 0x01
ZW_THERMOSTAT_FAN_MODE_AUTO_HIGH = 0x02
ZW_THERMOSTAT_FAN_MODE_HIGH = 0x03
ZW_THERMOSTAT_FAN_MODE_AUTO_MEDIUM = 0x04
ZW_THERMOSTAT_FAN_MODE_MEDIUM = 0x05
ZW_THERMOSTAT_FAN_MODE_CIRCULATION = 0x06
ZW_THERMOSTAT_FAN_MODE_HUMIDITY_CIRCULATION = 0x07
ZW_THERMOSTAT_FAN_MODE_LEFT_AND_RIGHT = 0x08
ZW_THERMOSTAT_FAN_MODE_UP_AND_DOWN = 0x09
ZW_THERMOSTAT_FAN_MODE_QUIET = 0x0A
ZW_THERMOSTAT_FAN_MODE_EXTERNAL_CIRCULATION = 0x0B


class ZwaveThermostatFanMode:
    """
    Z-Wave Command Class: Thermostat Mode "0x44" [Decimal 68]

    """

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_THERMOSTAT_FAN_MODE] = dict()
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_IDENTIFIER] = "Thermostat Fan Mode"
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS] = dict()
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_MODE_SET] = "Set"
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_MODE_GET] = "Get"
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_MODE_REPORT] = "Report"
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET] = "Supported Get"
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT] = "Supported Report"

            self.zw_thermostat_modes = dict()
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_AUTO_LOW] = "Auto Low"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_LOW] = "Low"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_AUTO_HIGH] = "Auto High"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_HIGH] = "High"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_AUTO_MEDIUM] = "Auto Medium"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_MEDIUM] = "Medium"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_CIRCULATION] = "Circulation"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_HUMIDITY_CIRCULATION] = "Humidity Circulation"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_LEFT_AND_RIGHT] = "Left & Right"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_UP_AND_DOWN] = "Up & Down"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_QUIET] = "Quiet"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_EXTERNAL_CIRCULATION] = "External Circulation"

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_FAN_MODE_SET:  # noqa [Duplicated code fragment!]
                self._interpret_set()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_FAN_MODE_GET:
                self._interpret_get()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_FAN_MODE_REPORT:
                self._interpret_report()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_set(self):
        try:
            fan_mode = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00011111  # noqa [Duplicated code fragment!]
            self.zw_interpretation[ZW_FAN_MODE] = fan_mode
            self.zw_interpretation[ZW_FAN_MODE_UI] = self.zw_thermostat_modes[fan_mode]

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Fan Mode: '{self.zw_interpretation[ZW_FAN_MODE_UI]}'")

            self.zw_interpretation[ZW_INTERPRETED] = True

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
            fan_mode = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00011111  # noqa [Duplicated code fragment!]
            self.zw_interpretation[ZW_FAN_MODE] = fan_mode
            self.zw_interpretation[ZW_FAN_MODE_UI] = self.zw_thermostat_modes[fan_mode]

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Fan Mode: '{self.zw_interpretation[ZW_FAN_MODE_UI]}'")

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
