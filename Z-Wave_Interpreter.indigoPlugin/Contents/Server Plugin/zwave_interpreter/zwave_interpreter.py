#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020-2022
#

# plugin Constants

try:
    # noinspection PyUnresolvedReferences
    import indigo
except ImportError:
    pass

from .zwave_constants import *
from .zwave_constants_command_classes import *
from .zwave_constants_interpretation import *
from .zwave_utility import ZwaveUtility
from .zwave_command_class_basic import ZwaveBasicCommand
from .zwave_command_class_thermostat_setpoint import ZwaveThermostatSetpoint
from .zwave_command_class_thermostat_mode import ZwaveThermostatMode
from .zwave_command_class_thermostat_operating_state import ZwaveThermostatOperatingState
from .zwave_command_class_thermostat_fan_mode import ZwaveThermostatFanMode
from .zwave_command_class_thermostat_fan_state import ZwaveThermostatFanState
from .zwave_command_class_sensor_multilevel import ZwaveSensorMultilevel
from .zwave_command_class_switch_multilevel import ZwaveSwitchMultilevel
from .zwave_command_class_meter import ZwaveMeter
from .zwave_command_class_wake_up import ZwaveWakeUp
from .zwave_command_class_sensor_binary import ZwaveSensorBinary
from .zwave_command_class_sensor_alarm import ZwaveSensorAlarm
from .zwave_command_class_battery import ZwaveBattery
from .zwave_command_class_climate_control_schedule import ZwaveClimateControlSchedule
from .zwave_command_class_notification import ZwaveNotification
from .zwave_command_class_multi_channel import ZwaveMultiChannel
from .zwave_command_class_switch_binary import ZwaveSwitchBinary
from .zwave_command_class_central_scene import ZwaveCentralScene


def convert_to_native(obj):
    # Thanks Jay: https://forums.indigodomo.com/viewtopic.php?p=193744#p193744
    if isinstance(obj, indigo.List):
        native_list = list()
        for item in obj:
            native_list.append(convert_to_native(item))
        return native_list
    elif isinstance(obj, indigo.Dict):
        native_dict = dict()
        for key, value in obj.items():
            native_dict[key] = convert_to_native(value)
        return native_dict
    else:
        return obj


# noinspection PyPep8Naming
class ZwaveInterpreter:
    """
    Z-Wave Interpreter interprets Indigo Z-Wave messages

    """

    def __init__(self, exception_handler, logger, indigo_devices):
        try:
            self.exception_handler = exception_handler
            self.logger = logger

            self.node_to_indigo_device = dict()
            if indigo_devices is not None:
                for dev in indigo_devices.iter("indigo.zwave"):
                    dev_address = int(dev.address)
                    if dev_address not in self.node_to_indigo_device:
                        self.node_to_indigo_device[int(dev.address)] = dict()
                    end_point = 0
                    # zwDevSubIndex_present = False
                    if 'zwDevSubIndex' in dev.ownerProps:
                        # zwDevSubIndex_present = True
                        end_point = int(dev.ownerProps['zwDevSubIndex'])
                    if end_point not in self.node_to_indigo_device[int(dev.address)]:
                        self.node_to_indigo_device[int(dev.address)][end_point] = dict()
                        self.node_to_indigo_device[int(dev.address)][end_point][ZW_INDIGO_DEVICE_ID] = dev.id
                        self.node_to_indigo_device[int(dev.address)][end_point][ZW_INDIGO_DEVICE_NAME] = dev.name
                        self.node_to_indigo_device[int(dev.address)][end_point][ZW_INDIGO_DEVICE_SUB_MODELS] = dict()
                        if end_point == 0:
                            dev_id_list = indigo.device.getGroupList(dev.id)
                            if len(dev_id_list) > 1:
                                for linked_dev_id in dev_id_list:
                                    if linked_dev_id != dev.id:
                                        linked_dev = indigo.devices[linked_dev_id]
                                        self.node_to_indigo_device[int(dev.address)][end_point][ZW_INDIGO_DEVICE_SUB_MODELS][linked_dev.subModel] = [linked_dev_id, linked_dev.name]

                        if end_point == 0:
                            #  zwClassCmdMapStr : 80v1 84v2 85v1 86v1 87v1 8Ev1 55v1 59v1 5Av1 5Ev1 9Fv1 20v1 70v1 71v1 6Cv1 30v1 31v11 72v1 73v1 7Av1 (string)
                            command_classes_indigo_dict = dev.ownerProps["zwClassCmdMap"]
                            command_classes_python_dict = convert_to_native(command_classes_indigo_dict)

                            # Copy dictionary replacing key with string format e.g. "c96" with int(96)
                            command_classes = dict()
                            for key, value in command_classes_python_dict.items():
                                new_key = int(key[1:])
                                command_classes[new_key] = value

                            self.node_to_indigo_device[int(dev.address)][end_point][ZW_INDIGO_DEVICE_COMMAND_CLASSES] = command_classes

                # self.logger.warning(f'ZWAVE NODE TO INDIGO DEVICE:\n{self.node_to_indigo_device}\n')

            self.zw_received_sent = False
            self.zw_interpretation = dict()
            self.device_id = 0
            self.device_name = ""
            self.device_command_classes = dict()
            self.interpret_all_devices = True
            self.interpret_devices_list = list()

            self.zw_command_classes = dict()

            self.utility = ZwaveUtility(self.exception_handler, self.logger, self.zw_command_classes, self.zw_interpretation)
            self.zwave_basic_command = ZwaveBasicCommand(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_battery = ZwaveBattery(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_central_scene = ZwaveCentralScene(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_climate_control_schedule = ZwaveClimateControlSchedule(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_meter = ZwaveMeter(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_multi_channel = ZwaveMultiChannel(self)
            self.zwave_notification = ZwaveNotification(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_sensor_alarm = ZwaveSensorAlarm(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_sensor_binary = ZwaveSensorBinary(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_sensor_multilevel = ZwaveSensorMultilevel(self)
            self.zwave_switch_binary = ZwaveSwitchBinary(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_switch_multilevel = ZwaveSwitchMultilevel(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_thermostat_mode = ZwaveThermostatMode(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_thermostat_fan_mode = ZwaveThermostatFanMode(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_thermostat_fan_state = ZwaveThermostatFanState(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_thermostat_operating_state = ZwaveThermostatOperatingState(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_thermostat_setpoint = ZwaveThermostatSetpoint(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)
            self.zwave_wake_up = ZwaveWakeUp(self.exception_handler, self.logger, self.utility, self.zw_command_classes, self.zw_interpretation)

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def link_node_to_indigo_device(self):
        try:
            node = self.zw_interpretation[ZW_NODE_ID]
            end_point = self.zw_interpretation[ZW_ENDPOINT]
            self.device_id = 0
            self.device_name = "unknown Indigo device"
            if end_point is None:
                end_point = 0
            if node is not None:
                self.device_name = f"{node} {end_point} Unknown Indigo device"
                if node in self.node_to_indigo_device:
                    if end_point in self.node_to_indigo_device[node]:
                        self.device_name = f"{self.node_to_indigo_device[node][end_point][ZW_INDIGO_DEVICE_NAME]}"
                        self.device_id = self.node_to_indigo_device[node][end_point][ZW_INDIGO_DEVICE_ID]
                        if end_point == 0:
                            self.device_command_classes = self.node_to_indigo_device[node][end_point][ZW_INDIGO_DEVICE_COMMAND_CLASSES]

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret_list(self, all_devices, device_list=None):
        try:
            if all_devices:
                self.interpret_all_devices = True
            else:
                self.interpret_all_devices = False
                self.interpret_devices_list = list()
                if device_list and len(device_list) > 0:
                    for device_id in device_list:
                        self.interpret_devices_list.append(device_id)

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def interpret_zwave(self, zwave_received, zwave_command):
            
        try:
            self.zw_interpretation.clear()

            if zwave_received:
                self.zw_received_sent = ["RCVD", "from"]
                class_displacement = 1
                self.zw_interpretation[ZW_COMMAND_SUCCESS] = None
                self.zw_interpretation[ZW_TIME_DELTA] = zwave_command['timeDelta'] = None
            else:
                self.zw_received_sent = ["SEND", "to"]
                class_displacement = 0
                self.zw_interpretation[ZW_COMMAND_SUCCESS] = zwave_command['cmdSuccess']
                self.zw_interpretation[ZW_TIME_DELTA] = zwave_command['timeDelta']

            # TODO: REMOVE DEBUG vvvv
            # if zwave_command['nodeId'] == 2 or zwave_command['nodeId'] == 72:
            #     self.logger.warning(f"\n\nInterpreting Z-Wave Command. {self.zw_received_sent[0]}: {zwave_command}")
            # TODO: REMOVE DEBUG ^^^^

            self.zw_interpretation[ZW_INTERPRETATION_ATTEMPTED] = False
            self.zw_interpretation[ZW_INTERPRETED] = False
            self.zw_interpretation[ZW_COMMAND_BYTES] = list()
            self.zw_interpretation[ZW_COMMAND_BYTES_UI] = "[ "
            for item in zwave_command["bytes"]:
                self.zw_interpretation[ZW_COMMAND_BYTES].append(item)
                self.zw_interpretation[ZW_COMMAND_BYTES_UI] = f"{self.zw_interpretation[ZW_COMMAND_BYTES_UI]}{'%0.2X' % item} "
            self.zw_interpretation[ZW_COMMAND_BYTES_UI] = f"{self.zw_interpretation[ZW_COMMAND_BYTES_UI]}]"
            self.zw_interpretation[ZW_ERROR_MESSAGE] = ""
            self.zw_interpretation[ZW_NODE_ID] = zwave_command['nodeId']  # Can be None!
            self.zw_interpretation[ZW_ENDPOINT] = zwave_command['endpoint']  # Often will be None!

            self.zw_interpretation[ZW_COMMAND_PACKET_LENGTH] = int(self.zw_interpretation[ZW_COMMAND_BYTES][5 + class_displacement])
            self.zw_interpretation[ZW_COMMAND_CLASS] = int(self.zw_interpretation[ZW_COMMAND_BYTES][6 + class_displacement])
            self.zw_interpretation[ZW_COMMAND] = int(self.zw_interpretation[ZW_COMMAND_BYTES][7 + class_displacement])
            self.zw_interpretation[ZW_COMMAND_DETAIL] = self.zw_interpretation[ZW_COMMAND_BYTES][8 + class_displacement:]  # The bytes following the Command Class and the Command

            self.link_node_to_indigo_device()  # Derive the Indigo Device from the Z-Wave Node and Endpoint

            if not self.interpret_all_devices:
                if self.device_id not in self.interpret_devices_list:
                    return self.zw_interpretation  # exit as not a Z-Wave device to be interpreted.

            self.zw_interpretation[ZW_INTERPRETATION_ATTEMPTED] = True

            if self.zw_interpretation[ZW_COMMAND_CLASS] in self.zw_command_classes:
                self.zw_interpretation[ZW_COMMAND_CLASS_UI] = self.zw_command_classes[self.zw_interpretation[ZW_COMMAND_CLASS]][ZW_IDENTIFIER]

                if self.zw_interpretation[ZW_COMMAND_CLASS] in self.device_command_classes:
                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION] = self.device_command_classes[self.zw_interpretation[ZW_COMMAND_CLASS]]
                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI] = f"v{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION]}"
                else:
                    # Unable to determine version number
                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI] = "Version Indeterminate"
                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION] = 0

                if self.zw_interpretation[ZW_COMMAND_CLASS_VERSION] == 0:
                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI] = "Version unknown"
                else:
                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI] = f"v{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION]}"

                    # SPECIAL FIX FOR COMMAND CLASS 0x71
                    if self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_NOTIFICATION:  # Could be " Command Class Alarm"
                        if self.zw_interpretation[ZW_COMMAND_PACKET_LENGTH] < 9:  # If Command Packet Length 9 or greater, assume Version 3-8
                            if (self.zw_interpretation[ZW_COMMAND_CLASS_VERSION] == 1) or (self.zw_interpretation[ZW_COMMAND_CLASS_VERSION] == 2):
                                self.zw_interpretation[ZW_COMMAND_CLASS_UI] = "Alarm"  # Override Command Class name if version 1 or 2, otherwise leave as "Notification"
                        else:
                            self.zw_interpretation[ZW_COMMAND_CLASS_VERSION] = 8
                            self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI] = "v8 ?"  # Reset to V8 but indicate questionable
                    # END SPECIAL FIX FOR COMMAND CLASS 0x71

                if self.zw_interpretation[ZW_COMMAND] in self.zw_command_classes[self.zw_interpretation[ZW_COMMAND_CLASS]][ZW_COMMANDS]:
                    self.zw_interpretation[ZW_COMMAND_UI] = self.zw_command_classes[self.zw_interpretation[ZW_COMMAND_CLASS]][ZW_COMMANDS][self.zw_interpretation[ZW_COMMAND]]

                    self.zw_interpretation[ZW_INTERPRETATION_UI] = ""

                    if self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_BASIC_COMMAND:
                        self.zwave_basic_command.interpret()

                    if self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_SWITCH_BINARY:
                        self.zwave_switch_binary.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_METER:
                        self.zwave_meter.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_SWITCH_MULTILEVEL:
                        self.zwave_switch_multilevel.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_SENSOR_BINARY:
                        self.zwave_sensor_binary.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_SENSOR_MULTILEVEL:
                        self.zwave_sensor_multilevel.interpret(self.zw_interpretation[ZW_COMMAND], self.zw_interpretation[ZW_COMMAND_DETAIL])

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_THERMOSTAT_OPERATING_STATE:
                        self.zwave_thermostat_operating_state.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_THERMOSTAT_MODE:
                        self.zwave_thermostat_mode.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_THERMOSTAT_FAN_MODE:
                        self.zwave_thermostat_fan_mode.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_THERMOSTAT_FAN_STATE:
                        self.zwave_thermostat_fan_state.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_THERMOSTAT_SETPOINT:
                        self.zwave_thermostat_setpoint.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_WAKE_UP:
                        self.zwave_wake_up.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_BATTERY:
                        self.zwave_battery.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_SENSOR_ALARM:
                        self.zwave_sensor_alarm.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_CLIMATE_CONTROL_SCHEDULE:
                        self.zwave_climate_control_schedule.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_NOTIFICATION:  # ## Note that this overloads the Alarm Class
                        self.zwave_notification.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_MULTI_CHANNEL:
                        self.zwave_multi_channel.interpret()

                    elif self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_CENTRAL_SCENE:
                        self.zwave_central_scene.interpret()

                    else:
                        self.zw_interpretation[ZW_ERROR_MESSAGE] = (
                            f"Logic not programmed for Z-Wave Command: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]}' and Z-Wave Command Class: '{self.zw_interpretation[ZW_COMMAND_UI]} [v{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]'")
                else:
                    # Z-Wave Command not known for Z-Wave Command Class
                    self.zw_interpretation[ZW_ERROR_MESSAGE] = (
                        f"Logic not programmed for Z-Wave Command: '{self.zw_interpretation[ZW_COMMAND]} [{hex(self.zw_interpretation[ZW_COMMAND])}]' and Z-Wave Command Class: '{self.zw_interpretation[ZW_COMMAND_CLASS_UI]} [v{self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI]}]'")
            else:
                # Z-Wave Command Class and command not known for Z-Wave Command Class
                self.zw_interpretation[ZW_ERROR_MESSAGE] = (
                    f"Logic not programmed for Z-Wave Command Class: '{self.zw_interpretation[ZW_COMMAND_CLASS]} [{hex(self.zw_interpretation[ZW_COMMAND_CLASS])}]'")

            interpreted_device_name = self.device_name

            # Setup Node & Endpoint for interpretation output
            if self.zw_interpretation[ZW_NODE_ID] is None:
                node_endpoint = ""
            else:
                if self.zw_interpretation[ZW_ENDPOINT] is None or self.zw_interpretation[ZW_ENDPOINT] == 0:
                    if self.device_id != 0:
                        dev = indigo.devices[self.device_id]
                        if len(self.node_to_indigo_device[int(dev.address)][0][ZW_INDIGO_DEVICE_SUB_MODELS]) > 0:
                            for key, value in self.node_to_indigo_device[int(dev.address)][0][ZW_INDIGO_DEVICE_SUB_MODELS].items():
                                if ZW_SENSOR_TYPE_UI in self.zw_interpretation and key == self.zw_interpretation[ZW_SENSOR_TYPE_UI]:
                                    interpreted_device_name = value[1]
                                    break

                    node_endpoint = f" [Node: {self.zw_interpretation[ZW_NODE_ID]}]"
                else:
                    node_endpoint = f" [Node: {self.zw_interpretation[ZW_NODE_ID]}, Endpoint: {self.zw_interpretation[ZW_ENDPOINT]}]"

            if not zwave_received:
                # Sent Z-Wave message log format

                success = "OK"
                if not self.zw_interpretation[ZW_COMMAND_SUCCESS]:
                    success = "FAILED"
                time_delta = self.zw_interpretation[ZW_TIME_DELTA]

                interpretation_overview = (
                    f"{self.zw_received_sent[0]}: '{success}', {self.zw_interpretation[ZW_COMMAND_BYTES_UI]} ({time_delta}ms) {self.zw_received_sent[1]} '{interpreted_device_name}'{node_endpoint}")
            else:
                # Received Z-Wave message log format
                interpretation_overview = (f"{self.zw_received_sent[0]}: '{self.zw_interpretation[ZW_COMMAND_BYTES_UI]}' {self.zw_received_sent[1]} '{interpreted_device_name}'{node_endpoint}")

            self.zw_interpretation[ZW_INTERPRETATION_OVERVIEW_UI] = interpretation_overview
            if self.zw_interpretation[ZW_INTERPRETED]:
                self.zw_interpretation[ZW_INTERPRETATION_DETAIL_UI] = self.zw_interpretation[ZW_INTERPRETATION_UI]

                # Multi Channel Processing - Interpreted encapsulated command class
                if self.zw_interpretation[ZW_COMMAND_CLASS] == ZW_MULTI_CHANNEL:
                    if len(self.zw_interpretation[ZW_COMMAND_DETAIL]) > 4:
                        if self.zw_interpretation[ZW_COMMAND_DETAIL][2] == ZW_SENSOR_MULTILEVEL:
                            zw_encapsulated_command = self.zw_interpretation[ZW_COMMAND_DETAIL][3]
                            zw_encapsulated_command_detail = self.zw_interpretation[ZW_COMMAND_DETAIL][4:]
                            zw_interpretation_detail_ui = f"{self.zw_interpretation[ZW_INTERPRETATION_UI]}\n  Encapsulated: "
                            self.zw_interpretation[ZW_COMMAND_CLASS_UI] = self.zw_command_classes[ZW_SENSOR_MULTILEVEL][ZW_IDENTIFIER]
                            self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI] = "n/a"
                            self.zw_interpretation[ZW_COMMAND_UI] = self.zw_command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][zw_encapsulated_command]
                            self.zwave_sensor_multilevel.interpret(zw_encapsulated_command, zw_encapsulated_command_detail)
                            if self.zw_interpretation[ZW_INTERPRETED]:
                                self.zw_interpretation[ZW_INTERPRETATION_DETAIL_UI] = f"{zw_interpretation_detail_ui}{self.zw_interpretation[ZW_INTERPRETATION_UI]}"
                            else:
                                self.zw_interpretation[ZW_INTERPRETATION_DETAIL_UI] = f"{zw_interpretation_detail_ui}Unable to interpret encapsulated command"
                                self.zw_interpretation[ZW_INTERPRETED] = True
            else:
                self.zw_interpretation[ZW_INTERPRETATION_DETAIL_UI] = self.zw_interpretation[ZW_ERROR_MESSAGE]

            return self.zw_interpretation

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
