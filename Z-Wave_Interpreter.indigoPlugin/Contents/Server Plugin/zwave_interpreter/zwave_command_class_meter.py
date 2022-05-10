#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_METER_GET = 0x01
ZW_METER_REPORT = 0x02
ZW_METER_SUPPORTED_GET = 0x03
ZW_METER_SUPPORTED_REPORT = 0x04
ZW_METER_RESET = 0x05

ZW_METER_TYPE_ELECTRIC = 0x01
ZW_METER_TYPE_GAS = 0x02
ZW_METER_TYPE_WATER = 0x03
ZW_METER_TYPE_HEATING = 0x04
ZW_METER_TYPE_COOLING = 0x05

ZW_METER_RATE_TYPE_UNSPECIFIED = 0x00
ZW_METER_TYPE_IMPORT = 0x01
ZW_METER_TYPE_EXPORT = 0x02

ZW_SCALE_METER_TYPE_ELECTRIC_KWH = 0x00
ZW_SCALE_METER_TYPE_ELECTRIC_KVAH = 0x01
ZW_SCALE_METER_TYPE_ELECTRIC_W = 0x02
ZW_SCALE_METER_TYPE_ELECTRIC_PULSE_COUNT = 0x03
ZW_SCALE_METER_TYPE_ELECTRIC_V = 0x04
ZW_SCALE_METER_TYPE_ELECTRIC_A = 0x05
ZW_SCALE_METER_TYPE_ELECTRIC_POWER_FACTOR = 0x06
ZW_SCALE_METER_TYPE_ELECTRIC_M_S_T = 0x07

ZW_SCALE_METER_TYPE_GAS_CUBIC_METERS = 0x00
ZW_SCALE_METER_TYPE_GAS_CUBIC_FEET = 0x01
ZW_SCALE_METER_TYPE_GAS_PULSE_COUNT = 0x03
ZW_SCALE_METER_TYPE_GAS_M_S_T = 0x07

ZW_SCALE_METER_TYPE_WATER_CUBIC_METERS = 0x00
ZW_SCALE_METER_TYPE_WATER_CUBIC_FEET = 0x01
ZW_SCALE_METER_TYPE_WATER_US_GALLONS = 0x02
ZW_SCALE_METER_TYPE_WATER_PULSE_COUNT = 0x03
ZW_SCALE_METER_TYPE_WATER_M_S_T = 0x07

ZW_SCALE_METER_TYPE_HEATING_KWH = 0x00

ZW_SCALE_METER_TYPE_COOLING_KWH = 0x00


class ZwaveMeter:
    """
    Z-Wave Command Class: Meter "0x32" [Decimal 50]

    """

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_METER] = dict()
            self.command_classes[ZW_METER][ZW_IDENTIFIER] = "Meter"
            self.command_classes[ZW_METER][ZW_COMMANDS] = dict()
            self.command_classes[ZW_METER][ZW_COMMANDS][ZW_METER_GET] = "Get"
            self.command_classes[ZW_METER][ZW_COMMANDS][ZW_METER_REPORT] = "Report"
            self.command_classes[ZW_METER][ZW_COMMANDS][ZW_METER_SUPPORTED_GET] = "Supported Get"
            self.command_classes[ZW_METER][ZW_COMMANDS][ZW_METER_SUPPORTED_REPORT] = "Supported Report"
            self.command_classes[ZW_METER][ZW_COMMANDS][ZW_METER_RESET] = "Reset"

            self.zw_meter_rate_types = dict()
            self.zw_meter_rate_types[ZW_METER_RATE_TYPE_UNSPECIFIED] = "Unspecified"
            self.zw_meter_rate_types[ZW_METER_TYPE_IMPORT] = "Import"
            self.zw_meter_rate_types[ZW_METER_TYPE_EXPORT] = "Export"

            self.zw_meter_types = dict()
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC] = dict()
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_IDENTIFIER] = "Electric Meter"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES] = dict()
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_KWH] = "kWh"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_KVAH] = "kVAh"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_W] = "W"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_PULSE_COUNT] = "Pulse Count"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_V] = "V"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_A] = "A"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_POWER_FACTOR] = "Power Factor"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_M_S_T] = "M.S.T"
            
            self.zw_meter_types[ZW_METER_TYPE_GAS] = dict()
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_IDENTIFIER] = "Gas Meter"
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_SCALES] = dict()
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_SCALES][ZW_SCALE_METER_TYPE_GAS_CUBIC_METERS] = "Cubic Meters"
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_SCALES][ZW_SCALE_METER_TYPE_GAS_CUBIC_FEET] = "Cubic Feet"
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_SCALES][ZW_SCALE_METER_TYPE_GAS_CUBIC_METERS] = "Pulse Count"
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_SCALES][ZW_SCALE_METER_TYPE_GAS_CUBIC_METERS] = "M.S.T"
            
            self.zw_meter_types[ZW_METER_TYPE_WATER] = dict()
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_IDENTIFIER] = "Water Meter"
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES] = dict()
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES][ZW_SCALE_METER_TYPE_WATER_CUBIC_METERS] = "Cubic Meters"
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES][ZW_SCALE_METER_TYPE_WATER_CUBIC_FEET] = "Cubic Feet"
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES][ZW_SCALE_METER_TYPE_WATER_US_GALLONS] = "US Gallons"
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES][ZW_SCALE_METER_TYPE_WATER_PULSE_COUNT] = "Pulse Count"
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES][ZW_SCALE_METER_TYPE_WATER_M_S_T] = "M.S.T"
            
            self.zw_meter_types[ZW_METER_TYPE_HEATING] = dict()
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_IDENTIFIER] = "Heating Meter"
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_SCALES] = dict()
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_SCALES][ZW_SCALE_METER_TYPE_HEATING_KWH] = "kWh"
            
            self.zw_meter_types[ZW_METER_TYPE_HEATING] = dict()
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_IDENTIFIER] = "Cooling Meter"
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_SCALES] = dict()
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_SCALES][ZW_SCALE_METER_TYPE_COOLING_KWH] = "kWh"
            
        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_METER_GET:
                self._interpret_get()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_METER_REPORT:
                self._interpret_report()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_METER_SUPPORTED_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_METER_SUPPORTED_REPORT:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_METER_RESET:
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
    
        # 01 14 00 04 10 5A 0E 32 02 21 44 00 00 57 0A 00 00 00 04 00 00 A7
        # or
        # 01 0E 00 04 00 A9 08 32 02 21 12 00 00 00 00 FF
    
        try:
            if self.zw_interpretation[ZW_COMMAND_CLASS_VERSION] == 1:
                meter_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0b00011111
                precision_scale_size = self.zw_interpretation[ZW_COMMAND_DETAIL][1]
                precision = (precision_scale_size & 0b11100000) >> 5
                scale = (precision_scale_size & 0b00011000) >> 3
                if meter_type in self.zw_meter_types:  # noqa [Duplicated code fragment!]
                    if scale in self.zw_meter_types[meter_type][ZW_SCALES]:
                        scale_ui = scale_ui_compact = self.zw_meter_types[meter_type][ZW_SCALES][scale]
                    else:
                        scale_ui = scale_ui_compact = (f" [Unknown Scale: {scale}]")
                else:
                    scale_ui = scale_ui_compact = (f" [Unknown Scale: {scale}]")
                size = precision_scale_size & 0b00000111
                end_value = 2 + size
                value = self.utility.bytes_to_int(self.zw_interpretation[ZW_COMMAND_DETAIL][2:end_value])
                if self.zw_interpretation[ZW_COMMAND_DETAIL][2] & 0b10000000:  # Check if a negative number (high order bit set)
                    value = self.utility.twos_complement(value, size * 8)
                # value = float(value)/10**precision  # Set precision e.g. 1859 > 18.59 if precision = 2
                value_ui_format = f"{{:.{precision}f}}"
                value_ui = value_ui_format.format(float(value) / 10 ** precision)
    
                self.zw_interpretation[ZW_METER_TYPE] = meter_type
                if meter_type in self.zw_meter_types:
                    self.zw_interpretation[ZW_METER_TYPE_UI] = self.zw_meter_types[meter_type][ZW_IDENTIFIER]
                else:
                    self.zw_interpretation[ZW_METER_TYPE_UI] = f"Meter Type {meter_type} unknown"
                self.zw_interpretation[ZW_PRECISION] = precision
                self.zw_interpretation[ZW_SCALES] = scale
                self.zw_interpretation[ZW_SCALE_UI] = scale_ui
                self.zw_interpretation[ZW_SCALE_UI_COMPACT] = scale_ui_compact
                self.zw_interpretation[ZW_SIZE] = size
                self.zw_interpretation[ZW_VALUE] = value
                self.zw_interpretation[ZW_VALUE_UI] = value_ui
    
                self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                    f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Meter Type: '{self.zw_interpretation[ZW_METER_TYPE_UI]}', Value: '{self.zw_interpretation[ZW_VALUE_UI]}{self.zw_interpretation[ZW_SCALE_UI_COMPACT]}'")
    
                self.zw_interpretation[ZW_INTERPRETED] = True
    
            elif self.zw_interpretation[ZW_COMMAND_CLASS_VERSION] in (3, 5):
                meter_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0b00011111
                scale_2 = (self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0b10000000)  >> 5  # & b00000N00 is end result (where N is 1 or zero)
                # rate_type = (self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0b01100000)  >> 5
                precision_scale_1_size = self.zw_interpretation[ZW_COMMAND_DETAIL][1]
                precision = (precision_scale_1_size & 0b11100000) >> 5
                scale_1 = (precision_scale_1_size & 0b00011000) >> 3  # & b000000NN is end result (where N is 1 or zero)
                scale = scale_2 | scale_1  # & b00000NNN is end result (where N is 1 or zero)
                if meter_type in self.zw_meter_types:  # noqa [Duplicated code fragment!]
                    if scale in self.zw_meter_types[meter_type][ZW_SCALES]:
                        scale_ui = scale_ui_compact = self.zw_meter_types[meter_type][ZW_SCALES][scale]
                    else:
                        scale_ui = scale_ui_compact = (f" [Unknown Scale: {scale}]")
                else:
                    scale_ui = scale_ui_compact = (f" [Unknown Scale: {scale}]")
                size = precision_scale_1_size & 0b00000111
                end_value = 2 + size
                value = self.utility.bytes_to_int(self.zw_interpretation[ZW_COMMAND_DETAIL][2:end_value])
                if self.zw_interpretation[ZW_COMMAND_DETAIL][2] & 0b10000000:  # Check if a negative number (high order bit set)
                    value = self.utility.twos_complement(value, size * 8)
                # value = float(value)/10**precision  # Set precision e.g. 1859 > 18.59 if precision = 2
                value_ui_format = f"{{:.{precision}f}}"
                value_ui = value_ui_format.format(float(value) / 10 ** precision)
    
                self.zw_interpretation[ZW_METER_TYPE] = meter_type
                if meter_type in self.zw_meter_types:
                    self.zw_interpretation[ZW_METER_TYPE_UI] = self.zw_meter_types[meter_type][ZW_IDENTIFIER]
                else:
                    self.zw_interpretation[ZW_METER_TYPE_UI] = f"Meter Type {meter_type} unknown"
                self.zw_interpretation[ZW_PRECISION] = precision
                self.zw_interpretation[ZW_SCALES] = scale
                self.zw_interpretation[ZW_SCALE_UI] = scale_ui
                self.zw_interpretation[ZW_SCALE_UI_COMPACT] = scale_ui_compact
                self.zw_interpretation[ZW_SIZE] = size
                self.zw_interpretation[ZW_VALUE] = value
                self.zw_interpretation[ZW_VALUE_UI] = value_ui
    
                self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                    f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Meter Type: '{self.zw_interpretation[ZW_METER_TYPE_UI]}', Value: '{self.zw_interpretation[ZW_VALUE_UI]}{self.zw_interpretation[ZW_SCALE_UI_COMPACT]}'")
    
                self.zw_interpretation[ZW_INTERPRETED] = True
            else:
                self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                    f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]}', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}' [Logic not programmed for V{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]")
    
                self.zw_interpretation[ZW_INTERPRETED] = False
    
        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
