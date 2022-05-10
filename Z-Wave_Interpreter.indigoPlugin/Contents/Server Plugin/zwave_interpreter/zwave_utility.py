#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

from .zwave_constants import *
from .zwave_constants_interpretation import *


class ZwaveUtility:
    """
    Z-wave Interpreter Utility methods

    """

    def __init__(self, exception_handler, logger, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def evaluate_value(self, value):
        try:
            value_bool = bool(value)
            if value == 0:
                value_ui = "Off"
            elif value == 0xFE:
                value_ui = "Unknown"
            else:
                if value == 99:
                    value = 100
                value_ui = "on"

            return value, value_bool, value_ui

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def evaluate_value_2(self, value):
        try:
            value_bool = bool(value)
            if value == 0:
                value_ui = "Off"
            elif value <= 99 or value == 255:
                if value == 99:
                    value = 100
                value_ui = "on"
            else:
                value_ui = "Reserved"

            return value, value_bool, value_ui

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def evaluate_value_3(self, value):
        try:
            value_bool = bool(value)
            if value == 0:
                value_ui = "Off"
            elif value == 255:
                value_ui = "on"
            elif value == 254:
                value_ui = "Unknown"
            else:
                value_ui = "Reserved"

            return value, value_bool, value_ui

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

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
                    command_ui = (f"{command} [{hex(command)}]")
            else:
                command_class_ui = (f"{command_class} [{hex(command_class)}]")
                command_ui = (f"{command} [{hex(command)}]")

            return f"Z-Wave Command '{command_ui}' not yet supported for Z-Wave Command Class '{command_class_ui}' [{version_ui}]"

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def precision_scale_size(self, precision_scale_size):
        try:
            precision = (precision_scale_size & 0b11100000) >> 5
            scale = (precision_scale_size & 0b00011000) >> 3
            size = precision_scale_size & 0b00000111
            return precision, scale, size

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def bytes_to_int(self, byte_list):  # noqa - Method may be static
        result = 0
        for b in byte_list:
            result = result * 256 + int(b)
        return result

    def twos_complement(self, value, bit_width):  # noqa - Method may be static
        if value >= 2**bit_width:
            # This catches when someone tries to give a value that is out of range
            raise ValueError(f"Value: {value} out of range of {bit_width}-bit value.")
        else:
            return value - int((value << 1) & 2**bit_width)

    def convert_list_to_hex_string(self, byte_list):  # noqa - Method may be static
        return ' '.join(["%02X" % byte for byte in byte_list])
