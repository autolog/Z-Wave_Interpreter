#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *


ZW_THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET = 0x01  # noqa [Duplicated code fragment!]
ZW_THERMOSTAT_OPERATING_STATE_GET = 0x02
ZW_THERMOSTAT_OPERATING_STATE_REPORT = 0x03
ZW_THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_REPORT = 0x04
ZW_THERMOSTAT_OPERATING_STATE_LOGGING_GET = 0x05
ZW_THERMOSTAT_OPERATING_STATE_LOGGING_REPORT = 0x06

ZW_THERMOSTAT_OPERATING_STATE_IDLE = 0x00
ZW_THERMOSTAT_OPERATING_STATE_HEATING = 0x01
ZW_THERMOSTAT_OPERATING_STATE_COOLING = 0x02
ZW_THERMOSTAT_OPERATING_STATE_FAN_ONLY = 0x03
ZW_THERMOSTAT_OPERATING_STATE_PENDING_HEAT = 0x04
ZW_THERMOSTAT_OPERATING_STATE_PENDING_COOL = 0x05
ZW_THERMOSTAT_OPERATING_STATE_VENT_ECONOMIZER = 0x06
ZW_THERMOSTAT_OPERATING_STATE_AUX_HEATING = 0x07
ZW_THERMOSTAT_OPERATING_STATE_2ND_STAGE_HEATING = 0x08
ZW_THERMOSTAT_OPERATING_STATE_2ND_STAGE_COOLING = 0x09
ZW_THERMOSTAT_OPERATING_STATE_2ND_STAGE_AUX_HEAT = 0x0A
ZW_THERMOSTAT_OPERATING_STATE_3RD_STAGE_AUX_HEAT = 0x0B


ZW_THERMOSTAT_OPERATING_STATE_SCALE_CELSIUS = 0x00
ZW_THERMOSTAT_OPERATING_STATE_SCALE_FAHRENHEIT = 0x01


class ZwaveThermostatOperatingState:
    """
    Z-Wave Command Class: Thermostat Operating State "0x42" [Decimal 66]

    """

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE] = dict()
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_IDENTIFIER] = "Thermostat Operating State"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS] = dict()
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET] = "Logging Supported Get"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_GET] = "Get"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_REPORT] = "Report"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_REPORT] = "Logging Supported Report"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_LOGGING_GET] = "Logging Get"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_LOGGING_REPORT] = "Logging Report"

            self.zw_operating_states = dict()
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_IDLE] = "Idle"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_HEATING] = "Heating"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_COOLING] = "Cooling"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_FAN_ONLY] = "Fan Only"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_PENDING_HEAT] = "Pending Heat"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_PENDING_COOL] = "Pending Cool"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_VENT_ECONOMIZER] = "Vent/Economizer"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_AUX_HEATING] = "Aux Heating"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_2ND_STAGE_HEATING] = "2nd Stage Heating"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_2ND_STAGE_COOLING] = "2nd Stage Cooling"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_2ND_STAGE_AUX_HEAT] = "2nd Stage Aux Heat"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_3RD_STAGE_AUX_HEAT] = "3rd Stage Aux Heat"

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_OPERATING_STATE_GET:
                self._interpret_state_get()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_OPERATING_STATE_REPORT:
                self._interpret_state_report()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_REPORT:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_OPERATING_STATE_LOGGING_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_OPERATING_STATE_LOGGING_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message
    
        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_state_get(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}'")
    
            self.zw_interpretation[ZW_INTERPRETED] = True
    
        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_state_report(self):
        try:
            operating_state = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00001111
            self.zw_interpretation[ZW_OPERATING_STATE] = operating_state
            self.zw_interpretation[ZW_OPERATING_STATE_UI] = self.zw_operating_states[operating_state]

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Operating State: '{self.zw_interpretation[ZW_OPERATING_STATE_UI]}'")
    
            self.zw_interpretation[ZW_INTERPRETED] = True
    
        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
