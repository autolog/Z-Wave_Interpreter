#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_THERMOSTAT_FAN_MODE_SET = 0x01
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

    def __init__(self, logger, utility, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_THERMOSTAT_FAN_MODE] = dict()
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_IDENTIFIER] = u"Thermostat Fan Mode"
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS] = dict()
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_MODE_SET] = u"Set"
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_MODE_GET] = u"Get"
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_MODE_REPORT] = u"Report"
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_MODE_SUPPORTED_GET] = u"Supported Get"
            self.command_classes[ZW_THERMOSTAT_FAN_MODE][ZW_COMMANDS][ZW_THERMOSTAT_FAN_MODE_SUPPORTED_REPORT] = u"Supported Report"

            self.zw_thermostat_modes = dict()
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_AUTO_LOW] = u"Auto Low"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_LOW] = u"Low"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_AUTO_HIGH] = u"Auto High"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_HIGH] = u"High"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_AUTO_MEDIUM] = u"Auto Medium"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_MEDIUM] = u"Medium"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_CIRCULATION] = u"Circulation"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_HUMIDITY_CIRCULATION] = u"Humidity Circulation"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_LEFT_AND_RIGHT] = u"Left & Right"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_UP_AND_DOWN] = u"Up & Down"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_QUIET] = u"Quiet"
            self.zw_thermostat_modes[ZW_THERMOSTAT_FAN_MODE_EXTERNAL_CIRCULATION] = u"External Circulation"

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatFanMode' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_THERMOSTAT_FAN_MODE_SET:
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

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatFanMode' Class, 'interpret' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_set(self):
        try:
            fan_mode = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00011111
            self.zw_interpretation[ZW_FAN_MODE] = fan_mode
            self.zw_interpretation[ZW_FAN_MODE_UI] = self.zw_thermostat_modes[fan_mode]

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Fan Mode: '{3}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_FAN_MODE_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatFanMode' Class, '_interpret_set' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_get(self):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatFanMode' Class, '_interpret_get' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_report(self):
        try:
            fan_mode = self.zw_interpretation[ZW_COMMAND_DETAIL][0] & 0B00011111
            self.zw_interpretation[ZW_FAN_MODE] = fan_mode
            self.zw_interpretation[ZW_FAN_MODE_UI] = self.zw_thermostat_modes[fan_mode]

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}', Fan Mode: '{3}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_MODE_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveThermostatFanMode' Class, '_interpret_report' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
