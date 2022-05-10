#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_CENTRAL_SCENE_SUPPORTED_GET = 0x01  # noqa [Duplicated code fragment!]
ZW_CENTRAL_SCENE_SUPPORTED_REPORT = 0x02
ZW_CENTRAL_SCENE_NOTIFICATION = 0x03
ZW_CENTRAL_SCENE_CONFIGURATION_SET = 0x04
ZW_CENTRAL_SCENE_CONFIGURATION_GET = 0x05
ZW_CENTRAL_SCENE_CONFIGURATION_REPORT = 0x06

ZW_CENTRAL_SCENE_KEY_PRESSED_1_TIME = 0x00
ZW_CENTRAL_SCENE_KEY_RELEASED = 0x01
ZW_CENTRAL_SCENE_KEY_HELD_DOWN = 0x02
ZW_CENTRAL_SCENE_KEY_PRESSED_2_TIMES = 0x03
ZW_CENTRAL_SCENE_KEY_PRESSED_3_TIMES = 0x04
ZW_CENTRAL_SCENE_KEY_PRESSED_4_TIMES = 0x05
ZW_CENTRAL_SCENE_KEY_PRESSED_5_TIMES = 0x06


class ZwaveCentralScene:
    """
    Z-Wave Command Class: Switch Multilevel "0x20" [Decimal 32]

    """

    def __init__(self, exception_handler, logger, utility, command_classes, zw_interpretation):
        try:
            self.exception_handler = exception_handler
            self.logger = logger
            self.utility = utility
            self.command_classes = command_classes
            self.zw_interpretation = zw_interpretation

            self.command_classes[ZW_CENTRAL_SCENE] = dict()
            self.command_classes[ZW_CENTRAL_SCENE][ZW_IDENTIFIER] = "Central Scene"
            self.command_classes[ZW_CENTRAL_SCENE][ZW_COMMANDS] = dict()
            self.command_classes[ZW_CENTRAL_SCENE][ZW_COMMANDS][ZW_CENTRAL_SCENE_SUPPORTED_GET] = "Supported Get"
            self.command_classes[ZW_CENTRAL_SCENE][ZW_COMMANDS][ZW_CENTRAL_SCENE_SUPPORTED_REPORT] = "Supported Report"
            self.command_classes[ZW_CENTRAL_SCENE][ZW_COMMANDS][ZW_CENTRAL_SCENE_NOTIFICATION] = "Notification"
            self.command_classes[ZW_CENTRAL_SCENE][ZW_COMMANDS][ZW_CENTRAL_SCENE_CONFIGURATION_SET] = "Configuration Set"
            self.command_classes[ZW_CENTRAL_SCENE][ZW_COMMANDS][ZW_CENTRAL_SCENE_CONFIGURATION_GET] = "Configuration Get"
            self.command_classes[ZW_CENTRAL_SCENE][ZW_COMMANDS][ZW_CENTRAL_SCENE_CONFIGURATION_GET] = "Configuration Report"

            self.zw_central_scene_key = dict()
            self.zw_central_scene_key[ZW_CENTRAL_SCENE_KEY_PRESSED_1_TIME] = "Key Pressed Once"
            self.zw_central_scene_key[ZW_CENTRAL_SCENE_KEY_RELEASED] = "Key Released"
            self.zw_central_scene_key[ZW_CENTRAL_SCENE_KEY_HELD_DOWN] = "Key Held Down"
            self.zw_central_scene_key[ZW_CENTRAL_SCENE_KEY_PRESSED_2_TIMES] = "Key Pressed Two Times"
            self.zw_central_scene_key[ZW_CENTRAL_SCENE_KEY_PRESSED_3_TIMES] = "Key Pressed Three Times"
            self.zw_central_scene_key[ZW_CENTRAL_SCENE_KEY_PRESSED_4_TIMES] = "Key Pressed Four Times"
            self.zw_central_scene_key[ZW_CENTRAL_SCENE_KEY_PRESSED_5_TIMES] = "Key Pressed Five Times"

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret(self):
        try:
            if self.zw_interpretation[ZW_COMMAND] == ZW_CENTRAL_SCENE_SUPPORTED_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_CENTRAL_SCENE_SUPPORTED_REPORT:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_CENTRAL_SCENE_NOTIFICATION:
                self._interpret_notification()
                return
            elif self.zw_interpretation[ZW_COMMAND] == ZW_CENTRAL_SCENE_CONFIGURATION_SET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_CENTRAL_SCENE_CONFIGURATION_GET:
                pass
            elif self.zw_interpretation[ZW_COMMAND] == ZW_CENTRAL_SCENE_CONFIGURATION_GET:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def _interpret_notification(self):
        try:
            sequence_number = self.zw_interpretation[ZW_COMMAND_DETAIL][0]
            key_attributes = self.zw_interpretation[ZW_COMMAND_DETAIL][1] & 0B00000111
            key_attributes_ui = self.zw_central_scene_key[key_attributes]
            scene_number = self.zw_interpretation[ZW_COMMAND_DETAIL][2]

            self.zw_interpretation[ZW_SEQUENCE_NUMBER] = sequence_number
            self.zw_interpretation[ZW_KEY_ATTRIBUTES] = key_attributes
            self.zw_interpretation[ZW_KEY_ATTRIBUTES_UI] = key_attributes_ui
            self.zw_interpretation[ZW_SCENE_NUMBER] = scene_number

            self.zw_interpretation[ZW_INTERPRETATION_UI] = (
                f"Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]', Command: '{self.zw_interpretation[ZW_COMMAND_UI]}', Sequence: '{self.zw_interpretation[ZW_SEQUENCE_NUMBER]}, Key: {self.zw_interpretation[ZW_KEY_ATTRIBUTES_UI]}, Scene: '{self.zw_interpretation[ZW_SCENE_NUMBER]}")

            self.zw_interpretation[ZW_INTERPRETED] = True

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
