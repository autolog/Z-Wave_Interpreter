#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys

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

    def __init__(self, logger, utility, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_METER] = dict()
            self.command_classes[ZW_METER][ZW_IDENTIFIER] = u"Meter"
            self.command_classes[ZW_METER][ZW_COMMANDS] = dict()
            self.command_classes[ZW_METER][ZW_COMMANDS][ZW_METER_GET] = u"Get"
            self.command_classes[ZW_METER][ZW_COMMANDS][ZW_METER_REPORT] = u"Report"
            self.command_classes[ZW_METER][ZW_COMMANDS][ZW_METER_SUPPORTED_GET] = u"Supported Get"
            self.command_classes[ZW_METER][ZW_COMMANDS][ZW_METER_SUPPORTED_REPORT] = u"Supported Report"
            self.command_classes[ZW_METER][ZW_COMMANDS][ZW_METER_RESET] = u"Reset"

            self.zw_meter_rate_types = dict()
            self.zw_meter_rate_types[ZW_METER_RATE_TYPE_UNSPECIFIED] = u"Unspecified"
            self.zw_meter_rate_types[ZW_METER_TYPE_IMPORT] = u"Import"
            self.zw_meter_rate_types[ZW_METER_TYPE_EXPORT] = u"Export"

            self.zw_meter_types = dict()
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC] = dict()
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_IDENTIFIER] = u"Electric Meter"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES] = dict()
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_KWH] = u"kWh"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_KVAH] = u"kVAh"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_W] = u"W"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_PULSE_COUNT] = u"Pulse Count"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_V] = u"V"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_A] = u"A"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_POWER_FACTOR] = u"Power Factor"
            self.zw_meter_types[ZW_METER_TYPE_ELECTRIC][ZW_SCALES][ZW_SCALE_METER_TYPE_ELECTRIC_M_S_T] = u"M.S.T"
            
            self.zw_meter_types[ZW_METER_TYPE_GAS] = dict()
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_IDENTIFIER] = u"Gas Meter"
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_SCALES] = dict()
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_SCALES][ZW_SCALE_METER_TYPE_GAS_CUBIC_METERS] = u"Cubic Meters"
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_SCALES][ZW_SCALE_METER_TYPE_GAS_CUBIC_FEET] = u"Cubic Feet"
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_SCALES][ZW_SCALE_METER_TYPE_GAS_CUBIC_METERS] = u"Pulse Count"
            self.zw_meter_types[ZW_METER_TYPE_GAS][ZW_SCALES][ZW_SCALE_METER_TYPE_GAS_CUBIC_METERS] = u"M.S.T"
            
            self.zw_meter_types[ZW_METER_TYPE_WATER] = dict()
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_IDENTIFIER] = u"Water Meter"
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES] = dict()
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES][ZW_SCALE_METER_TYPE_WATER_CUBIC_METERS] = u"Cubic Meters"
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES][ZW_SCALE_METER_TYPE_WATER_CUBIC_FEET] = u"Cubic Feet"
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES][ZW_SCALE_METER_TYPE_WATER_US_GALLONS] = u"US Gallons"
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES][ZW_SCALE_METER_TYPE_WATER_PULSE_COUNT] = u"Pulse Count"
            self.zw_meter_types[ZW_METER_TYPE_WATER][ZW_SCALES][ZW_SCALE_METER_TYPE_WATER_M_S_T] = u"M.S.T"
            
            self.zw_meter_types[ZW_METER_TYPE_HEATING] = dict()
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_IDENTIFIER] = u"Heating Meter"
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_SCALES] = dict()
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_SCALES][ZW_SCALE_METER_TYPE_HEATING_KWH] = u"kWh"
            
            self.zw_meter_types[ZW_METER_TYPE_HEATING] = dict()
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_IDENTIFIER] = u"Cooling Meter"
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_SCALES] = dict()
            self.zw_meter_types[ZW_METER_TYPE_HEATING][ZW_SCALES][ZW_SCALE_METER_TYPE_COOLING_KWH] = u"kWh"
            
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveMeter' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

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
    
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveMeter' Class, 'interpret' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
    
    def _interpret_get(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI]))
    
            self.zw_interpretation[ZW_INTERPRETED] = True
    
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveMeter' Class, '_interpret_get' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
    
    def _interpret_report(self):
    
        # 01 14 00 04 10 5A 0E 32 02 21 44 00 00 57 0A 00 00 00 04 00 00 A7
    
        try:
            if self.zw_interpretation[ZW_COMMAND_CLASS_VERSION] == 1:
                meter_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0]
                precision_scale_size = self.zw_interpretation[ZW_COMMAND_DETAIL][1]
                precision = (precision_scale_size & 0b11100000) >> 5
                scale = (precision_scale_size & 0b00011000) >> 3
                if meter_type in self.zw_meter_types:
                    if scale in self.zw_meter_types[meter_type][ZW_SCALES]:
                        scale_ui = scale_ui_compact = self.zw_meter_types[meter_type][ZW_SCALES][scale]
                    else:
                        scale_ui = scale_ui_compact = (u" [Unknown Scale: {0}]".format(scale))
                else:
                    scale_ui = scale_ui_compact = (u" [Unknown Scale: {0}]".format(scale))
                size = precision_scale_size & 0b00000111
                end_value = 2 + size
                value = self.utility.bytes_to_int(self.zw_interpretation[ZW_COMMAND_DETAIL][2:end_value])
                if self.zw_interpretation[ZW_COMMAND_DETAIL][2] & 0b10000000:  # Check if a negative number (high order bit set)
                    value = self.utility.twos_complement(value, size * 8)
                # value = float(value)/10**precision  # Set precision e.g. 1859 > 18.59 if precision = 2
                value_ui_format = "{{:.{0}f}}".format(precision)
                value_ui = value_ui_format.format(float(value) / 10 ** precision)
    
                self.zw_interpretation[ZW_METER_TYPE] = meter_type
                if meter_type in self.zw_meter_types:
                    self.zw_interpretation[ZW_METER_TYPE_UI] = self.zw_meter_types[meter_type][ZW_IDENTIFIER]
                else:
                    self.zw_interpretation[ZW_METER_TYPE_UI] = "Meter Type {0} unknown".format(meter_type)
                self.zw_interpretation[ZW_PRECISION] = precision
                self.zw_interpretation[ZW_SCALES] = scale
                self.zw_interpretation[ZW_SCALE_UI] = scale_ui
                self.zw_interpretation[ZW_SCALE_UI_COMPACT] = scale_ui_compact
                self.zw_interpretation[ZW_SIZE] = size
                self.zw_interpretation[ZW_VALUE] = value
                self.zw_interpretation[ZW_VALUE_UI] = value_ui
    
                self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Meter Type: '{3}', Value: '{4}{5}'"
                                                                .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                        self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                        self.zw_interpretation[ZW_COMMAND_UI],
                                                                        self.zw_interpretation[ZW_METER_TYPE_UI],
                                                                        self.zw_interpretation[ZW_VALUE_UI],
                                                                        self.zw_interpretation[ZW_SCALE_UI_COMPACT]))
    
                self.zw_interpretation[ZW_INTERPRETED] = True
    
            elif self.zw_interpretation[ZW_COMMAND_CLASS_VERSION] == 3:
                meter_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0b00011111
                scale_2 = (self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0b10000000)  >> 5  # & b00000N00 is end result (where N is 1 or zero)
                rate_type = (self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0b01100000)  >> 5
                precision_scale_1_size = self.zw_interpretation[ZW_COMMAND_DETAIL][1]
                precision = (precision_scale_1_size & 0b11100000) >> 5
                scale_1 = (precision_scale_1_size & 0b00011000) >> 3  # & b000000NN is end result (where N is 1 or zero)
                scale = scale_2 | scale_1  # & b00000NNN is end result (where N is 1 or zero)
                if meter_type in self.zw_meter_types:
                    if scale in self.zw_meter_types[meter_type][ZW_SCALES]:
                        scale_ui = scale_ui_compact = self.zw_meter_types[meter_type][ZW_SCALES][scale]
                    else:
                        scale_ui = scale_ui_compact = (u" [Unknown Scale: {0}]".format(scale))
                else:
                    scale_ui = scale_ui_compact = (u" [Unknown Scale: {0}]".format(scale))
                size = precision_scale_1_size & 0b00000111
                end_value = 2 + size
                value = self.utility.bytes_to_int(self.zw_interpretation[ZW_COMMAND_DETAIL][2:end_value])
                if self.zw_interpretation[ZW_COMMAND_DETAIL][2] & 0b10000000:  # Check if a negative number (high order bit set)
                    value = self.utility.twos_complement(value, size * 8)
                # value = float(value)/10**precision  # Set precision e.g. 1859 > 18.59 if precision = 2
                value_ui_format = "{{:.{0}f}}".format(precision)
                value_ui = value_ui_format.format(float(value) / 10 ** precision)
    
                self.zw_interpretation[ZW_METER_TYPE] = meter_type
                if meter_type in self.zw_meter_types:
                    self.zw_interpretation[ZW_METER_TYPE_UI] = self.zw_meter_types[meter_type][ZW_IDENTIFIER]
                else:
                    self.zw_interpretation[ZW_METER_TYPE_UI] = "Meter Type {0} unknown".format(meter_type)
                self.zw_interpretation[ZW_PRECISION] = precision
                self.zw_interpretation[ZW_SCALES] = scale
                self.zw_interpretation[ZW_SCALE_UI] = scale_ui
                self.zw_interpretation[ZW_SCALE_UI_COMPACT] = scale_ui_compact
                self.zw_interpretation[ZW_SIZE] = size
                self.zw_interpretation[ZW_VALUE] = value
                self.zw_interpretation[ZW_VALUE_UI] = value_ui
    
                self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [v{1}]', Command: '{2}', Meter Type: '{3}', Value: '{4}{5}'"
                                                                .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                        self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                        self.zw_interpretation[ZW_COMMAND_UI],
                                                                        self.zw_interpretation[ZW_METER_TYPE_UI],
                                                                        self.zw_interpretation[ZW_VALUE_UI],
                                                                        self.zw_interpretation[ZW_SCALE_UI_COMPACT]))
    
                self.zw_interpretation[ZW_INTERPRETED] = True
            else:
                self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0}', Command: '{1}' [Logic not programmed for V{2}]"
                                                                .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                        self.zw_interpretation[ZW_COMMAND_UI],
                                                                        self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]))
    
                self.zw_interpretation[ZW_INTERPRETED] = False
    
        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveMeter' Class, '_interpret_report' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
