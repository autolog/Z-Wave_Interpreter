#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_THERMOSTAT_MODE_SET = 0x01
ZW_THERMOSTAT_MODE_GET = 0x02
ZW_THERMOSTAT_MODE_REPORT = 0x03
ZW_THERMOSTAT_MODE_SUPPORTED_GET = 0x04
ZW_THERMOSTAT_MODE_SUPPORTED_REPORT = 0x05

ZW_THERMOSTAT_MODE_OFF = 0x00
ZW_THERMOSTAT_MODE_HEAT = 0x01
ZW_THERMOSTAT_MODE_COOL = 0x02
ZW_THERMOSTAT_MODE_AUTO = 0x03
ZW_THERMOSTAT_MODE_AUXILIARY = 0x04
ZW_THERMOSTAT_MODE_RESUME_ON = 0x05
ZW_THERMOSTAT_MODE_FAN = 0x06
ZW_THERMOSTAT_MODE_FURNACE = 0x07
ZW_THERMOSTAT_MODE_DRY = 0x08
ZW_THERMOSTAT_MODE_MOIST = 0x09
ZW_THERMOSTAT_MODE_AUTO_CHANGEOVER = 0x0A
ZW_THERMOSTAT_MODE_ENERGY_HEAT = 0x0B
ZW_THERMOSTAT_MODE_ENERGY_COOL = 0x0C
ZW_THERMOSTAT_MODE_AWAY = 0x0D
ZW_THERMOSTAT_MODE_RESERVED = 0x0E
ZW_THERMOSTAT_MODE_FULL_POWER = 0x0F
ZW_THERMOSTAT_MODE_MANUFACTURER_SPECIFIC = 0x1F


class ZwaveThermostatMode:
    """
    Z-Wave Command Class: Thermostat Mode "0x40" [Decimal 64]

    """

    def __init__(self, logger, utility, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_THERMOSTAT_MODE] = dict()
            self.command_classes[ZW_THERMOSTAT_MODE][ZW_IDENTIFIER] = u"Thermostat Mode"
            self.command_classes[ZW_THERMOSTAT_MODE][ZW_COMMANDS] = dict()
            self.command_classes[ZW_THERMOSTAT_MODE][ZW_COMMANDS][ZW_THERMOSTAT_MODE_SET] = u"Set"
            self.command_classes[ZW_THERMOSTAT_MODE][ZW_COMMANDS][ZW_THERMOSTAT_MODE_GET] = u"Get"
            self.command_classes[ZW_THERMOSTAT_MODE][ZW_COMMANDS][ZW_THERMOSTAT_MODE_REPORT] = u"Report"
            self.command_classes[ZW_THERMOSTAT_MODE][ZW_COMMANDS][ZW_THERMOSTAT_MODE_SUPPORTED_GET] = u"Supported Get"
            self.command_classes[ZW_THERMOSTAT_MODE][ZW_COMMANDS][ZW_THERMOSTAT_MODE_SUPPORTED_REPORT] = u"Supported Report"

            self.zw_thermostat_modes = dict()
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_OFF] = u"Off"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_HEAT] = u"Heat"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_COOL] = u"Cool"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_AUTO] = u"Auto"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_AUXILIARY] = u"Auxiliary"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_RESUME_ON] = u"Resume [On]"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_FAN] = u"Fan"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_FURNACE] = u"Furnace"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_DRY] = u"Dry"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_MOIST] = u"Moist"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_AUTO_CHANGEOVER] = u"Auto Changeover"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_ENERGY_HEAT] = u"Energy Heat"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_ENERGY_COOL] = u"Energy Cool"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_AWAY] = u"Away"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_RESERVED] = u"Reserved"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_FULL_POWER] = u"Full Power"
            self.zw_thermostat_modes[ZW_THERMOSTAT_MODE_MANUFACTURER_SPECIFIC] = u"Manufacturer Specific"

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatMode' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_MODE_SET:
                self._interpret_set()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_MODE_GET:
                self._interpret_get()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_MODE_REPORT:
                self._interpret_report()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_MODE_SUPPORTED_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_MODE_SUPPORTED_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatMode' Class, 'interpret' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_set(self):
        try:
            mode = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00011111
            number_of_manufacturer_fields, manufacturer_fields = self._manufacturer_fields(mode)
            self.zw_interpretation[ZW_MODE] = mode
            self.zw_interpretation[ZW_MODE_UI] = self.zw_thermostat_modes[mode]
            self.zw_interpretation[ZW_NUMBER_OF_MANUFACTURER_FIELDS] = number_of_manufacturer_fields
            self.zw_interpretation[ZW_MANUFACTURER_FIELDS] = manufacturer_fields

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Mode: '{3}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_MODE_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatMode' Class, '_interpret_set' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_get(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatMode' Class, '_interpret_get' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_report(self):
        try:
            mode = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00011111
            number_of_manufacturer_fields, manufacturer_fields = self._manufacturer_fields(mode)
            self.zw_interpretation[ZW_MODE] = mode
            self.zw_interpretation[ZW_MODE_UI] = self.zw_thermostat_modes[mode]
            self.zw_interpretation[ZW_NUMBER_OF_MANUFACTURER_FIELDS] = number_of_manufacturer_fields
            self.zw_interpretation[ZW_MANUFACTURER_FIELDS] = manufacturer_fields

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Mode: '{3}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_MODE_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatMode' Class, '_interpret_report' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _manufacturer_fields(self, mode):
        try:
            number_of_manufacturer_fields = 0
            manufacturer_fields = ""
            if self.zw_interpretation[ZW_COMMAND_CLASS_VERSION] == 3 and mode == ZW_THERMOSTAT_MODE_MANUFACTURER_SPECIFIC:
                number_of_manufacturer_fields = (self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B11100000) >> 5
                end_value = 1 + number_of_manufacturer_fields
                manufacturer_fields = self.zw_interpretation[ZW_COMMAND_DETAIL][1:end_value]

            return number_of_manufacturer_fields, manufacturer_fields

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatMode' Class, '_manufacturer_fields' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
