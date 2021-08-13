#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2021
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *


ZW_THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET = 0x01
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

    def __init__(self, logger, utility, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE] = dict()
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_IDENTIFIER] = u"Thermostat Operating State"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS] = dict()
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET] = u"Logging Supported Get"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_GET] = u"Get"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_REPORT] = u"Report"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_REPORT] = u"Logging Supported Report"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_LOGGING_GET] = u"Logging Get"
            self.command_classes[ZW_THERMOSTAT_OPERATING_STATE][ZW_COMMANDS][ZW_THERMOSTAT_OPERATING_STATE_LOGGING_REPORT] = u"Logging Report"

            self.zw_operating_states = dict()
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_IDLE] = u"Idle"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_HEATING] = u"Heating"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_COOLING] = u"Cooling"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_FAN_ONLY] = u"Fan Only"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_PENDING_HEAT] = u"Pending Heat"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_PENDING_COOL] = u"Pending Cool"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_VENT_ECONOMIZER] = u"Vent/Economizer"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_AUX_HEATING] = u"Aux Heating"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_2ND_STAGE_HEATING] = u"2nd Stage Heating"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_2ND_STAGE_COOLING] = u"2nd Stage Cooling"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_2ND_STAGE_AUX_HEAT] = u"2nd Stage Aux Heat"
            self.zw_operating_states[ZW_THERMOSTAT_OPERATING_STATE_3RD_STAGE_AUX_HEAT] = u"3rd Stage Aux Heat"

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatOperatingState' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

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
    
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatOperatingState' Class, 'interpret' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_state_get(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI]))
    
            self.zw_interpretation[ZW_INTERPRETED] = True
    
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatOperatingState' Class, '_interpret_get' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_state_report(self):
        try:
            operating_state = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00001111
            self.zw_interpretation[ZW_OPERATING_STATE] = operating_state
            self.zw_interpretation[ZW_OPERATING_STATE_UI] = self.zw_operating_states[operating_state]

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Operating State: '{3}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_OPERATING_STATE_UI]))
    
            self.zw_interpretation[ZW_INTERPRETED] = True
    
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatOperatingState' Class, '_interpret_report' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
