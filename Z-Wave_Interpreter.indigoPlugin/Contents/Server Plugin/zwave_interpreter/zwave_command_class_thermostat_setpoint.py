#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *


ZW_THERMOSTAT_SETPOINT = 0x43
ZW_THERMOSTAT_SETPOINT_SET = 0x01
ZW_THERMOSTAT_SETPOINT_GET = 0x02
ZW_THERMOSTAT_SETPOINT_REPORT = 0x03
ZW_THERMOSTAT_SETPOINT_SUPPORTED_GET = 0x04
ZW_THERMOSTAT_SETPOINT_SUPPORTED_REPORT = 0x05
ZW_THERMOSTAT_SETPOINT_CAPABILITIES_GET = 0x09
ZW_THERMOSTAT_SETPOINT_CAPABILITIES_REPORT = 0x0A

ZW_THERMOSTAT_SETPOINT_TYPE_NOT_AVAILABLE = 0x00
ZW_THERMOSTAT_SETPOINT_TYPE_HEATING = 0x01
ZW_THERMOSTAT_SETPOINT_TYPE_COOLING = 0x02
ZW_THERMOSTAT_SETPOINT_TYPE_FURNACE = 0x07
ZW_THERMOSTAT_SETPOINT_TYPE_DRY_AIR = 0x08
ZW_THERMOSTAT_SETPOINT_TYPE_MOIST_AIR = 0x09
ZW_THERMOSTAT_SETPOINT_TYPE_AUTO_CHANGEOVER = 0x0A
ZW_THERMOSTAT_SETPOINT_TYPE_ENERGY_SAVE_HEATING = 0x0B
ZW_THERMOSTAT_SETPOINT_TYPE_ENERGY_SAVE_COOLING = 0x0C
ZW_THERMOSTAT_SETPOINT_TYPE_AWAY_HEATING = 0x0D
ZW_THERMOSTAT_SETPOINT_TYPE_AWAY_COOLING = 0x0E
ZW_THERMOSTAT_SETPOINT_TYPE_FULL_POWER = 0x0F

ZW_THERMOSTAT_SETPOINT_SCALE_CELSIUS = 0x00
ZW_THERMOSTAT_SETPOINT_SCALE_FAHRENHEIT = 0x01


class ZwaveThermostatSetpoint:
    """
    Z-Wave Command Class: Thermostat Setpoint "0x43" [Decimal 67]

    """

    def __init__(self, logger, utility, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_THERMOSTAT_SETPOINT] = dict()
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_IDENTIFIER] = u"Thermostat Setpoint"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS] = dict()
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_SET] = u"Set"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_GET] = u"Get"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_REPORT] = u"Report"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_SUPPORTED_GET] = u"Supported Get"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_SUPPORTED_REPORT] = u"Supported Report"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_CAPABILITIES_GET] = u"Capabilities Get"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_CAPABILITIES_REPORT] = u"Capabilities Report"
            
            self.zw_thermostat_setpoint_types = dict()
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_HEATING] = u"Heating"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_COOLING] = u"Cooling"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_FURNACE] = u"Furnace"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_DRY_AIR] = u"Dry Air"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_MOIST_AIR] = u"Moist Air"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_AUTO_CHANGEOVER] = u"Auto Changeover"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_ENERGY_SAVE_HEATING] = u"Energy Save Heating"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_ENERGY_SAVE_COOLING] = u"Energy Save Cooling"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_AWAY_HEATING] = u"Away Heating"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_AWAY_COOLING] = u"Away Cooling"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_FULL_POWER] = u"Full Power"
            
            self.zw_thermostat_setpoint_scales = dict()
            self.zw_thermostat_setpoint_scales[ZW_THERMOSTAT_SETPOINT_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_thermostat_setpoint_scales[ZW_THERMOSTAT_SETPOINT_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatSetpoint' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_SETPOINT_SET:
                self._interpret_set()
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_SETPOINT_GET:
                self._interpret_get()
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_SETPOINT_REPORT:
                self._interpret_report()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_SETPOINT_SUPPORTED_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_SETPOINT_SUPPORTED_REPORT:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_SETPOINT_CAPABILITIES_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_SETPOINT_CAPABILITIES_REPORT:
                pass
    
            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message
    
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatSetpoint' Class, 'interpret' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_get(self):
        try:
            setpoint_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00001111
            self.zw_interpretation[ZW_SETPOINT_TYPE] = setpoint_type
            if setpoint_type in self.zw_thermostat_setpoint_types:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = self.zw_thermostat_setpoint_types[setpoint_type]
            else:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = u"Setpoint Type {0} unknown".format(setpoint_type)
    
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Setpoint Type: '{3}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_SETPOINT_TYPE_UI]))
    
            self.zw_interpretation[ZW_INTERPRETED] = True
    
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatSetpoint' Class, '_interpret_get' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_report(self):
        try:
            setpoint_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00001111
    
            precision, scale, size = self.utility.precision_scale_size(self.zw_interpretation[ZW_COMMAND_DETAIL][1])
    
            if scale in self.zw_thermostat_setpoint_scales:
                scale_ui = self.zw_thermostat_setpoint_scales[scale][0]
                scale_ui_compact = self.zw_thermostat_setpoint_scales[scale][1]
            else:
                scale_ui = scale_ui_compact = (u" [Unknown Scale: {0}]".format(scale))
    
            end_value = 2 + size
            value = self.utility.bytes_to_int(self.zw_interpretation[ZW_COMMAND_DETAIL][2:end_value])
            if self.zw_interpretation[ZW_COMMAND_DETAIL][2] & 0b10000000:  # Check if a negative number (high order bit set)
                value = self.utility.twos_complement(value, size * 8)
            # value = float(value)/10**precision  # Set precision e.g. 1859 > 18.59 if precision = 2
            value_ui_format = "{{:.{0}f}}".format(precision)
            value_ui = value_ui_format.format(float(value) / 10 ** precision)
    
            self.zw_interpretation[ZW_SETPOINT_TYPE] = setpoint_type
            if setpoint_type in self.zw_thermostat_setpoint_types:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = self.zw_thermostat_setpoint_types[setpoint_type]
            else:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = u"Setpoint Type {0} unknown".format(setpoint_type)
            self.zw_interpretation[ZW_PRECISION] = precision
            self.zw_interpretation[ZW_SCALES] = scale
            self.zw_interpretation[ZW_SCALE_UI] = scale_ui
            self.zw_interpretation[ZW_SCALE_UI_COMPACT] = scale_ui_compact
            self.zw_interpretation[ZW_SIZE] = size
            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_UI] = value_ui
    
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Setpoint Type: '{3}', Value: '{4}{5}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_SETPOINT_TYPE_UI],
                                                                    self.zw_interpretation[ZW_VALUE_UI],
                                                                    self.zw_interpretation[ZW_SCALE_UI_COMPACT]))
    
            self.zw_interpretation[ZW_INTERPRETED] = True
    
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatSetpoint' Class, '_interpret_report' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
    
    def _interpret_set(self):
        try:
            setpoint_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00001111
    
            precision, scale, size = self.utility.precision_scale_size(self.zw_interpretation[ZW_COMMAND_DETAIL][1])
    
            if scale in self.zw_thermostat_setpoint_scales:
                scale_ui = self.zw_thermostat_setpoint_scales[scale][0]
                scale_ui_compact = self.zw_thermostat_setpoint_scales[scale][1]
            else:
                scale_ui = scale_ui_compact = (u" [Unknown Scale: {0}]".format(scale))
    
            end_value = 2 + size
            value = self.utility.bytes_to_int(self.zw_interpretation[ZW_COMMAND_DETAIL][2:end_value])
            if self.zw_interpretation[ZW_COMMAND_DETAIL][2] & 0b10000000:  # Check if a negative number (high order bit set)
                value = self.utility.twos_complement(value, size * 8)
            # value = float(value)/10**precision  # Set precision e.g. 1859 > 18.59 if precision = 2
            value_ui_format = "{{:.{0}f}}".format(precision)
            value_ui = value_ui_format.format(float(value) / 10 ** precision)
    
            self.zw_interpretation[ZW_SETPOINT_TYPE] = setpoint_type
            if setpoint_type in self.zw_thermostat_setpoint_types:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = self.zw_thermostat_setpoint_types[setpoint_type]
            else:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = u"Setpoint Type {0} unknown".format(setpoint_type)
            self.zw_interpretation[ZW_PRECISION] = precision
            self.zw_interpretation[ZW_SCALES] = scale
            self.zw_interpretation[ZW_SCALE_UI] = scale_ui
            self.zw_interpretation[ZW_SCALE_UI_COMPACT] = scale_ui_compact
            self.zw_interpretation[ZW_SIZE] = size
            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_UI] = value_ui
    
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Setpoint: '{3}', Value: '{4}{5}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_SETPOINT_TYPE_UI],
                                                                    self.zw_interpretation[ZW_VALUE_UI],
                                                                    self.zw_interpretation[ZW_SCALE_UI_COMPACT]))
    
            self.zw_interpretation[ZW_INTERPRETED] = True
    
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatSetpoint' Class, '_interpret_set' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
