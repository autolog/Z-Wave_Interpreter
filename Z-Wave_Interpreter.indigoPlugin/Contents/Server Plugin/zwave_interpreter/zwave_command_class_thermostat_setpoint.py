#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

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

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_THERMOSTAT_SETPOINT] = dict()
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_IDENTIFIER] = "Thermostat Setpoint"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS] = dict()
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_SET] = "Set"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_GET] = "Get"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_REPORT] = "Report"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_SUPPORTED_GET] = "Supported Get"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_SUPPORTED_REPORT] = "Supported Report"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_CAPABILITIES_GET] = "Capabilities Get"
            self.command_classes[ZW_THERMOSTAT_SETPOINT][ZW_COMMANDS][ZW_THERMOSTAT_SETPOINT_CAPABILITIES_REPORT] = "Capabilities Report"
            
            self.zw_thermostat_setpoint_types = dict()
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_HEATING] = "Heating"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_COOLING] = "Cooling"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_FURNACE] = "Furnace"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_DRY_AIR] = "Dry Air"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_MOIST_AIR] = "Moist Air"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_AUTO_CHANGEOVER] = "Auto Changeover"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_ENERGY_SAVE_HEATING] = "Energy Save Heating"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_ENERGY_SAVE_COOLING] = "Energy Save Cooling"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_AWAY_HEATING] = "Away Heating"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_AWAY_COOLING] = "Away Cooling"
            self.zw_thermostat_setpoint_types[ZW_THERMOSTAT_SETPOINT_TYPE_FULL_POWER] = "Full Power"
            
            self.zw_thermostat_setpoint_scales = dict()
            self.zw_thermostat_setpoint_scales[ZW_THERMOSTAT_SETPOINT_SCALE_CELSIUS] = ("Celsius (C)", "° C")
            self.zw_thermostat_setpoint_scales[ZW_THERMOSTAT_SETPOINT_SCALE_FAHRENHEIT] = ("Fahrenheit (F)", "° F")

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_SETPOINT_SET:
                self._interpret_set()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_SETPOINT_GET:
                self._interpret_get()
                return
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
    
        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_get(self):
        try:
            setpoint_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00001111
            self.zw_interpretation[ZW_SETPOINT_TYPE] = setpoint_type
            if setpoint_type in self.zw_thermostat_setpoint_types:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = self.zw_thermostat_setpoint_types[setpoint_type]
            else:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = f"Setpoint Type {setpoint_type} unknown"
    
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Setpoint Type: '{self.zw_interpretation[ZW_SETPOINT_TYPE_UI]}'")
    
            self.zw_interpretation[ZW_INTERPRETED] = True
    
        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_report(self):
        try:
            setpoint_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00001111  # noqa [Duplicated code fragment!]
    
            precision, scale, size = self.utility.precision_scale_size(self.zw_interpretation[ZW_COMMAND_DETAIL][1])
    
            if scale in self.zw_thermostat_setpoint_scales:
                scale_ui = self.zw_thermostat_setpoint_scales[scale][0]
                scale_ui_compact = self.zw_thermostat_setpoint_scales[scale][1]
            else:
                scale_ui = scale_ui_compact = (f" [Unknown Scale: {scale}]")
    
            end_value = 2 + size
            value = self.utility.bytes_to_int(self.zw_interpretation[ZW_COMMAND_DETAIL][2:end_value])
            if self.zw_interpretation[ZW_COMMAND_DETAIL][2] & 0b10000000:  # Check if a negative number (high order bit set)
                value = self.utility.twos_complement(value, size * 8)
            # value = float(value)/10**precision  # Set precision e.g. 1859 > 18.59 if precision = 2
            value_ui_format = f"{{:.{precision}f}}"
            value_ui = value_ui_format.format(float(value) / 10 ** precision)
    
            self.zw_interpretation[ZW_SETPOINT_TYPE] = setpoint_type
            if setpoint_type in self.zw_thermostat_setpoint_types:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = self.zw_thermostat_setpoint_types[setpoint_type]
            else:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = f"Setpoint Type {setpoint_type} unknown"
            self.zw_interpretation[ZW_PRECISION] = precision
            self.zw_interpretation[ZW_SCALES] = scale
            self.zw_interpretation[ZW_SCALE_UI] = scale_ui
            self.zw_interpretation[ZW_SCALE_UI_COMPACT] = scale_ui_compact
            self.zw_interpretation[ZW_SIZE] = size
            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_UI] = value_ui
    
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Setpoint Type: '{self.zw_interpretation[ZW_SETPOINT_TYPE_UI]}', Value: '{self.zw_interpretation[ZW_VALUE_UI]}{self.zw_interpretation[ZW_SCALE_UI_COMPACT]}'")
    
            self.zw_interpretation[ZW_INTERPRETED] = True
    
        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
    
    def _interpret_set(self):
        try:
            setpoint_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00001111  # noqa [Duplicated code fragment!]
    
            precision, scale, size = self.utility.precision_scale_size(self.zw_interpretation[ZW_COMMAND_DETAIL][1])
    
            if scale in self.zw_thermostat_setpoint_scales:
                scale_ui = self.zw_thermostat_setpoint_scales[scale][0]
                scale_ui_compact = self.zw_thermostat_setpoint_scales[scale][1]
            else:
                scale_ui = scale_ui_compact = (f" [Unknown Scale: {scale}]")
    
            end_value = 2 + size
            value = self.utility.bytes_to_int(self.zw_interpretation[ZW_COMMAND_DETAIL][2:end_value])
            if self.zw_interpretation[ZW_COMMAND_DETAIL][2] & 0b10000000:  # Check if a negative number (high order bit set)
                value = self.utility.twos_complement(value, size * 8)
            # value = float(value)/10**precision  # Set precision e.g. 1859 > 18.59 if precision = 2
            value_ui_format = f"{{:.{precision}f}}"
            value_ui = value_ui_format.format(float(value) / 10 ** precision)
    
            self.zw_interpretation[ZW_SETPOINT_TYPE] = setpoint_type
            if setpoint_type in self.zw_thermostat_setpoint_types:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = self.zw_thermostat_setpoint_types[setpoint_type]
            else:
                self.zw_interpretation[ZW_SETPOINT_TYPE_UI] = f"Setpoint Type {setpoint_type} unknown"
            self.zw_interpretation[ZW_PRECISION] = precision
            self.zw_interpretation[ZW_SCALES] = scale
            self.zw_interpretation[ZW_SCALE_UI] = scale_ui
            self.zw_interpretation[ZW_SCALE_UI_COMPACT] = scale_ui_compact
            self.zw_interpretation[ZW_SIZE] = size
            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_UI] = value_ui
    
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Setpoint: '{self.zw_interpretation[ZW_SETPOINT_TYPE_UI]}', Value: '{self.zw_interpretation[ZW_VALUE_UI]}{self.zw_interpretation[ZW_SCALE_UI_COMPACT]}'")
    
            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
