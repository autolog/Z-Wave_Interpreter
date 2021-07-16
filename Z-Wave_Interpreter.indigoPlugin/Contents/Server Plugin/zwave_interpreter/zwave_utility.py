#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys
from .zwave_constants import *
from .zwave_constants_interpretation import *


class ZwaveUtility:
    """
    Z-wave Interpreter Utility methods

    """

    def __init__(self, logger, command_classes, zw_interpretation):
        try:
            self.logger = logger
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveUtility' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def evaluate_value(self, value):
        try:
            value_bool = bool(value)
            if value == 0:
                value_ui = u"Off"
            elif value == 0xFE:
                value_ui = u"Unknown"
            else:
                if value == 99:
                    value = 100
                value_ui = u"on"

            return value, value_bool, value_ui

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'evaluate_value' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def evaluate_value_2(self, value):
        try:
            value_bool = bool(value)
            if value == 0:
                value_ui = u"Off"
            elif value <= 99 or value == 255:
                if value == 99:
                    value = 100
                value_ui = u"on"
            else:
                value_ui = u"Reserved"

            return value, value_bool, value_ui

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'evaluate_value_2' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def evaluate_value_3(self, value):
        try:
            value_bool = bool(value)
            if value == 0:
                value_ui = u"Off"
            elif value == 255:
                value_ui = u"on"
            elif value == 254:
                value_ui = u"Unknown"
            else:
                value_ui = "Reserved"

            return value, value_bool, value_ui

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'evaluate_value_3' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def not_supported(self, interpretation):
        try:
            command_class = interpretation[ZW_COMMAND_CLASS]
            command = interpretation[ZW_COMMAND]
            version_ui = interpretation[ZW_COMMAND_CLASS_VERSION_UI]
            if command_class in self.command_classes:
                # command_class_ui = ZW_COMMAND_CLASSES[command_class][ZW_IDENTIFIER]
                command_class_ui = self.zw_interpretation[ZW_COMMAND_CLASS_UI]  # Allows for Command Class Notification | Alarm fix
                if command in self.command_classes[command_class][ZW_COMMANDS]:
                    command_ui = self.command_classes[command_class][ZW_COMMANDS][command]
                else:
                    command_ui = (u"{0} [{1}]".format(command, hex(command)))
            else:
                command_class_ui = (u"{0} [{1}]".format(command_class, hex(command_class)))
                command_ui = (u"{0} [{1}]".format(command, hex(command)))

            return u"Z-Wave Command '{0}' not yet supported for Z-Wave Command Class '{1}' [{2}]".format(command_ui, command_class_ui, version_ui)

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'supported' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def precision_scale_size(self, precision_scale_size):
        try:
            precision = (precision_scale_size & 0b11100000) >> 5
            scale = (precision_scale_size & 0b00011000) >> 3
            size = precision_scale_size & 0b00000111
            return precision, scale, size

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'precision_scale_size' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def bytes_to_int(self, byte_list):
        result = 0
        for b in byte_list:
            result = result * 256 + int(b)
        return result

    def twos_complement(self, value, bit_width):
        if value >= 2**bit_width:
            # This catches when someone tries to give a value that is out of range
            raise ValueError(u"Value: {} out of range of {}-bit value.".format(value, bit_width))
        else:
            return value - int((value << 1) & 2**bit_width)

    def convert_list_to_hex_string(self, byte_list):
        return ' '.join(["%02X" % byte for byte in byte_list])
