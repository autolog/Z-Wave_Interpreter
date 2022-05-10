#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_THERMOSTAT_FAN_STATE_GET = 0x02
ZW_THERMOSTAT_FAN_STATE_REPORT = 0x03

ZW_THERMOSTAT_FAN_STATE_IDLE_OFF = 0x00
ZW_THERMOSTAT_FAN_STATE_RUNNING_RUNNING_LOW = 0x01
ZW_THERMOSTAT_FAN_STATE_RUNNING_HIGH = 0x02
ZW_THERMOSTAT_FAN_STATE_RUNNING_MEDIUM = 0x03
ZW_THERMOSTAT_FAN_STATE_CIRCULATION_MODE = 0x04
ZW_THERMOSTAT_FAN_STATE_HUMIDITY_CIRCULATION_MODE = 0x05
ZW_THERMOSTAT_FAN_STATE_RIGHT_LEFT_CIRCULATION_MODE = 0x06
ZW_THERMOSTAT_FAN_STATE_UP_DOWN_CIRCULATION_MODE = 0x07
ZW_THERMOSTAT_FAN_STATE_QUIET_CIRCULATION_MODE = 0x08


class ZwaveThermostatFanState:
    """
    Z-Wave Command Class: Thermostat Fan State "0x45" [Decimal 69]

    """

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_THERMOSTAT_FAN_STATE] = dict()
            self.command_classes[ZW_THERMOSTAT_FAN_STATE][ZW_IDENTIFIER] = "Thermostat Fan State"
            self.command_classes[ZW_THERMOSTAT_FAN_STATE][ZW_COMMANDS] = dict()
            self.command_classes[ZW_THERMOSTAT_FAN_STATE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_STATE_GET] = "Get"
            self.command_classes[ZW_THERMOSTAT_FAN_STATE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_STATE_REPORT] = "Report"

            self.zw_thermostat_modes = dict()
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_STATE_IDLE_OFF] = "Idle / Off"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_STATE_RUNNING_RUNNING_LOW] = "Running / Running Low"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_STATE_RUNNING_HIGH] = "Running High"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_STATE_RUNNING_MEDIUM] = "Running Medium"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_STATE_CIRCULATION_MODE] = "Circulation Mode"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_STATE_HUMIDITY_CIRCULATION_MODE] = "Humidity Circulation Mode"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_STATE_RIGHT_LEFT_CIRCULATION_MODE] = "Right - Left Circulation Mode"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_STATE_UP_DOWN_CIRCULATION_MODE] = "Up - Down Circulation Mode"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_STATE_QUIET_CIRCULATION_MODE] = "Quiet Circulation Mode"

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_FAN_STATE_GET:
                self._interpret_get()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_FAN_STATE_REPORT:
                self._interpret_report()
                return

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
            fan_operating_state = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00011111
            self.zw_interpretation[ZW_FAN_MODE] = fan_operating_state
            self.zw_interpretation[ZW_FAN_MODE_UI] = self.zw_thermostat_modes[fan_operating_state]

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Fan Operating State: '{self.zw_interpretation[ZW_FAN_MODE_UI]}'")

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
