#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter - Plugin © Autolog 2020-2022
#
# Requires Indigo 2022.1+ [Runs under Python 3]

# noinspection PyUnresolvedReferences
# ============================== Native Imports ===============================

from datetime import datetime
import logging
import os
import platform
import sys
import traceback

# ============================== Custom Imports ===============================
try:
    # noinspection PyUnresolvedReferences
    import indigo
except ImportError:
    pass

from constants import *
from zwave_interpreter.zwave_interpreter import *
from zwave_interpreter.zwave_constants_interpretation import *

# ================================== Header ===================================
__author__    = "Autolog"
__copyright__ = ""
__license__   = "MIT"
__build__     = "unused"
__title__     = "Z-Wave Interpreter Plugin for Indigo"
__version__   = "unused"

kDefaultPluginPrefs = {
    "zwaveInterpretationMode": "S",
    "zwaveLogToIndigoEventLogOption": False,
    "zwaveLogToPluginLogOption": False,
    "zwaveLogToStandAloneFileOption": False,
    "standAloneZwaveLogFolderPath": "",
    "standAloneZwaveLogFileName": ""
}


class Plugin(indigo.PluginBase):

    def __init__(self, plugin_id, plugin_display_name, plugin_version, plugin_prefs):
        super(Plugin, self).__init__(plugin_id, plugin_display_name, plugin_version, plugin_prefs)

        self.zwave_available_devices = dict()
        self.zwave_interpreted_devices = dict()

        # Initialise dictionary to store plugin Globals
        self.globals = dict()

        self.needToSavePrefs = True
        # if True:  # when adding a pref
        #     self.needToSavePrefs = True

        # Initialise Indigo plugin info
        self.globals[K_PLUGIN_INFO] = {}
        self.globals[K_PLUGIN_INFO][K_PLUGIN_ID] = plugin_id
        self.globals[K_PLUGIN_INFO][K_PLUGIN_DISPLAY_NAME] = plugin_display_name
        self.globals[K_PLUGIN_INFO][K_PLUGIN_VERSION] = plugin_version
        self.globals[K_PLUGIN_INFO][K_PATH] = indigo.server.getInstallFolderPath()
        self.globals[K_PLUGIN_INFO][K_API_VERSION] = indigo.server.apiVersion
        self.globals[K_PLUGIN_INFO][K_ADDRESS] = indigo.server.address

        log_format = logging.Formatter("%(asctime)s.%(msecs)03d\t%(levelname)-12s\t%(name)s.%(funcName)-25s %(msg)s", datefmt="%Y-%m-%d %H:%M:%S")
        self.plugin_file_handler.setFormatter(log_format)
        self.plugin_file_handler.setLevel(K_LOG_LEVEL_INFO)  # Logging Level for plugin log file
        self.indigo_log_handler.setLevel(K_LOG_LEVEL_INFO)   # Logging level for Indigo Event Log

        self.logger = logging.getLogger("Plugin.ZWI")

        self.event_log_level = K_LOG_LEVEL_INFO
        self.plugin_log_level = K_LOG_LEVEL_INFO

        # Now logging is set up, output Initialising Message
        startup_message_ui = "\n"  # Start with a line break
        startup_message_ui += f"{' Initialising Z-Wave Interpreter Plugin ':={'^'}130}\n"
        startup_message_ui += f"{'Plugin Name:':<31} {self.globals[K_PLUGIN_INFO][K_PLUGIN_DISPLAY_NAME]}\n"
        startup_message_ui += f"{'Plugin Version:':<31} {self.globals[K_PLUGIN_INFO][K_PLUGIN_VERSION]}\n"
        startup_message_ui += f"{'Plugin ID:':<31} {self.globals[K_PLUGIN_INFO][K_PLUGIN_ID]}\n"
        startup_message_ui += f"{'Indigo Version:':<31} {indigo.server.version}\n"
        startup_message_ui += f"{'Indigo License:':<31} {indigo.server.licenseStatus}\n"
        startup_message_ui += f"{'Indigo API Version:':<31} {indigo.server.apiVersion}\n"
        machine = platform.machine()
        startup_message_ui += f"{'Architecture:':<31} {machine}\n"
        sys_version = sys.version.replace("\n", "")
        startup_message_ui += f"{'Python Version:':<31} {sys_version}\n"
        startup_message_ui += f"{'Mac OS Version:':<31} {platform.mac_ver()[0]}\n"
        startup_message_ui += f"{'':={'^'}130}\n"
        self.logger.info(startup_message_ui)

        # Set Plugin Config Values
        self.initialise_closedPrefsConfigUi = True
        self.closedPrefsConfigUi(plugin_prefs, False)

    def exception_handler(self, exception_error_message, log_failing_statement):
        filename, line_number, method, statement = traceback.extract_tb(sys.exc_info()[2])[-1]
        module = filename.split('/')
        log_message = f"'{exception_error_message}' in module '{module[-1]}', method '{method}'"
        if log_failing_statement:
            log_message = log_message + f"\n   Failing statement [line {line_number}]: '{statement}'"
        else:
            log_message = log_message + f" at line {line_number}"
        self.logger.error(log_message)

    def closedPrefsConfigUi(self, values_dict=None, user_cancelled=False):
        """
        Indigo method invoked after plugin configuration dialog is closed.

        -----
        :param values_dict:
        :param user_cancelled:
        :return:
        """

        try:
            if user_cancelled:
                return

            # Get required Event Log and Plugin Log logging levels
            self.event_log_level = int(values_dict.get("eventLogLevel", K_LOG_LEVEL_ZWAVE))
            self.plugin_log_level = int(values_dict.get("pluginLogLevel", K_LOG_LEVEL_ZWAVE))

            # Set initial required logging levels
            self.indigo_log_handler.setLevel(self.event_log_level)
            self.plugin_file_handler.setLevel(self.plugin_log_level)

            # Modify Logging levels dependant on Z-Wave Interpretations Requested

            if bool(values_dict.get("indigoEventLogDebug", False)):
                self.event_log_level = K_LOG_LEVEL_DEBUGGING
                self.indigo_log_handler.setLevel(self.event_log_level)

            zwave_log_to_indigo_event_log = bool(values_dict.get("zwaveLogToIndigoEventLogOption", False))
            if self.event_log_level != K_LOG_LEVEL_DEBUGGING:  # Check Debug not in process
                if self.initialise_closedPrefsConfigUi:
                    if zwave_log_to_indigo_event_log:
                        self.event_log_level = K_LOG_LEVEL_ZWAVE
                        self.indigo_log_handler.setLevel(self.event_log_level)
                    else:
                        self.event_log_level = K_LOG_LEVEL_INFO
                        self.indigo_log_handler.setLevel(self.event_log_level)
                    self.pluginPrefs["eventLogLevel"] = f"{self.event_log_level}"
                    indigo.server.savePluginPrefs()
            self.logger.info(f"Indigo Event Log set to '{K_LOG_LEVEL_TRANSLATION[self.event_log_level]}'")

            if bool(values_dict.get("pluginLogDebug", False)):
                self.plugin_log_level = K_LOG_LEVEL_DEBUGGING
                self.indigo_log_handler.setLevel(self.plugin_log_level)

            zwave_log_to_plugin_log = bool(self.pluginPrefs.get("zwaveLogToPluginLogOption", False))
            if self.plugin_log_level != K_LOG_LEVEL_DEBUGGING:  # Check Debug not in process
                if self.initialise_closedPrefsConfigUi:
                    if zwave_log_to_plugin_log:
                        self.plugin_log_level = K_LOG_LEVEL_ZWAVE
                        self.plugin_file_handler.setLevel(self.plugin_log_level)
                    else:
                        self.plugin_log_level = K_LOG_LEVEL_INFO
                        self.plugin_file_handler.setLevel(self.plugin_log_level)
                    self.pluginPrefs["pluginLogLevel"] = f"{self.plugin_log_level}"
                    indigo.server.savePluginPrefs()
            self.logger.info(f"Plugin Log set to '{K_LOG_LEVEL_TRANSLATION[self.plugin_log_level]}'")

            self.initialise_closedPrefsConfigUi = False

            if self.event_log_level <= K_LOG_LEVEL_ZWAVE:
                self.pluginPrefs["zwaveLogToIndigoEventLogOption"] = True
            else:
                self.pluginPrefs["zwaveLogToIndigoEventLogOption"] = False
            if self.plugin_log_level <= K_LOG_LEVEL_ZWAVE:
                self.pluginPrefs["zwaveLogToPluginLogOption"] = True
            else:
                self.pluginPrefs["zwaveLogToPluginLogOption"] = False
            indigo.server.savePluginPrefs()

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def getMenuActionConfigUiValues(self, menu_id=0):  # noqa [Unused local symbols]

        # Indigo method called to pre-populate menu config dialogs.

        try:
            values_dict = indigo.Dict()

            values_dict["zwaveLogToIndigoEventLogOption"] = bool(self.pluginPrefs.get("zwaveLogToIndigoEventLogOption", False))
            values_dict["zwaveLogToPluginLogOption"] = bool(self.pluginPrefs.get("zwaveLogToPluginLogOption", False))
            values_dict["zwaveLogToStandAloneFileOption"] = bool(self.pluginPrefs.get("zwaveLogToStandAloneFileOption", False))

            stand_alone_zwave_log_folder_path = self.pluginPrefs.get("standAloneZwaveLogFolderPath", "")
            if stand_alone_zwave_log_folder_path == "":
                stand_alone_zwave_log_folder_path = f"{self.globals[K_PLUGIN_INFO][K_PATH]}/Logs/com.autologplugin.indigoplugin.zwaveinterpreter/zwave_log"
                self.pluginPrefs["standAloneZwaveLogFolderPath"] = stand_alone_zwave_log_folder_path
                indigo.server.savePluginPrefs()
            values_dict["standAloneZwaveLogFolderPath"] = stand_alone_zwave_log_folder_path

            stand_alone_zwave_log_file_name = self.pluginPrefs.get("standAloneZwaveLogFileName", "")
            if stand_alone_zwave_log_file_name == "":
                stand_alone_zwave_log_file_name = "zwave_interpreter_log.txt"
                self.pluginPrefs["standAloneZwaveLogFileName"] = stand_alone_zwave_log_file_name
                indigo.server.savePluginPrefs()
            values_dict["standAloneZwaveLogFileName"] = stand_alone_zwave_log_file_name

            self.zwave_available_devices = dict()  # noqa [Duplicated code fragment!]
            self.zwave_interpreted_devices = dict()

            for zwave_dev in indigo.devices.iter("indigo.zwave"):
                zwave_dev_name = f"{zwave_dev.name}"
                zwave_props = zwave_dev.pluginProps
                if "zwave_interpretation" in zwave_props and bool(zwave_props["zwave_interpretation"]):
                    self.zwave_interpreted_devices[zwave_dev.id] = zwave_dev_name
                else:
                    self.zwave_available_devices[zwave_dev.id] = zwave_dev_name

            values_dict["zwaveInterpretationMode"] = self.pluginPrefs["zwaveInterpretationMode"]

            errors_dict = indigo.Dict()

            return values_dict, errors_dict

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def evaluateZwaveInterpretationMode(self, values_dict, type_id):  # noqa [Unused local symbols]
        try:

            saved_zwave_interpretation_mode = self.pluginPrefs.get("zwaveInterpretationMode", "S")
            updated_zwave_interpretation_mode = values_dict.get("zwaveInterpretationMode", "S")
            # self.logger.warning(f"evaluateZwaveInterpretationMode: Saved='{saved_zwave_interpretation_mode}', Updated='{updated_zwave_interpretation_mode}'")
            if updated_zwave_interpretation_mode != saved_zwave_interpretation_mode:
                self.pluginPrefs["zwaveInterpretationMode"] = updated_zwave_interpretation_mode

                if updated_zwave_interpretation_mode == "S":  # Selected Z-Wave devices only
                    interpreted_zwave_devices_list = list()
                    for zwave_dev_id, zwave_dev_name in self.zwave_interpreted_devices.items():
                        interpreted_zwave_devices_list.append(int(zwave_dev_id))
                    self.zwave_interpreter_class_instance.interpret_list(False, interpreted_zwave_devices_list)
                else:
                    # All Z-Wave devices
                    self.zwave_interpreter_class_instance.interpret_list(True, None)

                indigo.server.savePluginPrefs()

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def setZwaveLogToIndigoEventLogOption(self, values_dict, type_id):  # noqa [Unused local symbols]
        try:
            saved_zwave_log_to_indigo_event_log = bool(self.pluginPrefs.get("zwaveLogToIndigoEventLogOption", False))
            updated_zwave_log_to_indigo_event_log = bool(values_dict.get("zwaveLogToIndigoEventLogOption", False))
            if updated_zwave_log_to_indigo_event_log != saved_zwave_log_to_indigo_event_log:
                self.pluginPrefs["zwaveLogToIndigoEventLogOption"] = updated_zwave_log_to_indigo_event_log
                indigo.server.savePluginPrefs()

            if self.event_log_level != 5:  # Check Debug not in process
                if updated_zwave_log_to_indigo_event_log:
                    self.event_log_level = K_LOG_LEVEL_ZWAVE
                    self.indigo_log_handler.setLevel(self.event_log_level)
                else:
                    self.event_log_level = K_LOG_LEVEL_INFO
                    self.indigo_log_handler.setLevel(self.event_log_level)
                self.pluginPrefs["eventLogLevel"] = f"{self.event_log_level}"
                self.logger.info(f"Indigo Event Log set to '{K_LOG_LEVEL_TRANSLATION[self.event_log_level]}'")
                indigo.server.savePluginPrefs()

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def setZwaveLogToPluginLogOption(self, values_dict, type_id):  # noqa [Unused local symbols]
        try:
            saved_zwave_log_to_plugin_log = bool(self.pluginPrefs.get("zwaveLogToPluginLogOption", False))
            updated_zwave_log_to_plugin_log = bool(values_dict.get("zwaveLogToPluginLogOption", False))
            if updated_zwave_log_to_plugin_log != saved_zwave_log_to_plugin_log:
                self.pluginPrefs["zwaveLogToPluginLogOption"] = updated_zwave_log_to_plugin_log
                indigo.server.savePluginPrefs()

            if self.plugin_log_level != 5:  # Check Debug not in process
                if updated_zwave_log_to_plugin_log:
                    self.plugin_log_level = K_LOG_LEVEL_ZWAVE
                    self.plugin_file_handler.setLevel(self.plugin_log_level)
                else:
                    self.plugin_log_level = K_LOG_LEVEL_INFO
                    self.plugin_file_handler.setLevel(self.plugin_log_level)
                self.pluginPrefs["pluginLogLevel"] = f"{self.plugin_log_level}"
                self.logger.info(f"Plugin Log set to '{K_LOG_LEVEL_TRANSLATION[self.plugin_log_level]}'")
                indigo.server.savePluginPrefs()

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def setZwaveLogToStandAloneLogOption(self, values_dict, type_id):  # noqa [Unused local symbols]
        try:
            saved_zwave_log_to_stand_alone_log = bool(self.pluginPrefs.get("zwaveLogToStandAloneFileOption", False))
            updated_zwave_log_to_stand_alone_log = bool(values_dict.get("zwaveLogToStandAloneFileOption", False))
            if updated_zwave_log_to_stand_alone_log != saved_zwave_log_to_stand_alone_log:
                self.pluginPrefs["zwaveLogToStandAloneFileOption"] = updated_zwave_log_to_stand_alone_log
                indigo.server.savePluginPrefs()

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def setZwaveLogToStandAloneLogFolderPath(self, values_dict, type_id):  # noqa [Unused local symbols]
        try:
            saved_zwave_log_to_stand_alone_log_folder_path = self.pluginPrefs.get("standAloneZwaveLogFolderPath", "")
            updated_zwave_log_to_stand_alone_log_folder_path = values_dict.get("standAloneZwaveLogFolderPath", "")
            if updated_zwave_log_to_stand_alone_log_folder_path != saved_zwave_log_to_stand_alone_log_folder_path:
                self.pluginPrefs["standAloneZwaveLogFolderPath"] = updated_zwave_log_to_stand_alone_log_folder_path
                indigo.server.savePluginPrefs()

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def setZwaveLogToStandAloneLogFileName(self, values_dict, type_id):  # noqa [Unused local symbols]
        try:
            saved_zwave_log_to_stand_alone_log_file_name = self.pluginPrefs.get("standAloneZwaveLogFileName", "")
            updated_zwave_log_to_stand_alone_log_file_name = values_dict.get("standAloneZwaveLogFileName", "")
            if updated_zwave_log_to_stand_alone_log_file_name != saved_zwave_log_to_stand_alone_log_file_name:
                self.pluginPrefs["standAloneZwaveLogFileName"] = updated_zwave_log_to_stand_alone_log_file_name
                indigo.server.savePluginPrefs()

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def getPrefsConfigUiValues(self):
        try:
            prefs_config_ui_values = self.pluginPrefs

            if "zwave_log_file_path" not in prefs_config_ui_values:
                prefs_config_ui_values["zwave_log_file_path"] = f"{self.globals[K_PLUGIN_INFO][K_PATH]}/Logs/com.autologplugin.indigoplugin.zwaveinterpreter/zwave_logs"
            if "zwave_log_file_name" not in prefs_config_ui_values:
                prefs_config_ui_values["zwave_log_file_name"] = "zwave_interpreter_log.txt"

            return prefs_config_ui_values

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def shutdown(self):
        self.logger.threaddebug("shutdown called")

    def startup(self):
        try:
            if self.needToSavePrefs:
                indigo.server.savePluginPrefs()

            self.zwave_available_devices = dict()  # noqa [Duplicated code fragment!]
            self.zwave_interpreted_devices = dict()

            for zwave_dev in indigo.devices.iter("indigo.zwave"):
                zwave_dev_name = f"{zwave_dev.name}"
                zwave_props = zwave_dev.pluginProps
                if "zwave_interpretation" in zwave_props and bool(zwave_props["zwave_interpretation"]):
                    self.zwave_interpreted_devices[zwave_dev.id] = zwave_dev_name
                else:
                    self.zwave_available_devices[zwave_dev.id] = zwave_dev_name

            self.zwave_interpreter_class_instance = ZwaveInterpreter(self.exception_handler, self.logger, indigo.devices)  # noqa [Defined outside __init__] Instantiate and initialise Z-Wave Interpreter Object

            # Having instantiated the Z-Wave Interpreter Object, determine what Z-Wave devices should be logged for it.
            zwave_interpretation_mode = self.pluginPrefs.get("zwaveInterpretationMode", "S")
            if zwave_interpretation_mode == "S":  # Selected Z-Wave devices only
                interpreted_zwave_devices_list = list()
                for zwave_dev_id, zwave_dev_name in self.zwave_interpreted_devices.items():
                    interpreted_zwave_devices_list.append(int(zwave_dev_id))
                self.zwave_interpreter_class_instance.interpret_list(False, interpreted_zwave_devices_list)
            else:
                # All Z-Wave devices
                self.zwave_interpreter_class_instance.interpret_list(True, None)

            # Intercept incoming and outgoing Z-Wave messages
            indigo.zwave.subscribeToIncoming()
            indigo.zwave.subscribeToOutgoing()

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def zwaveCommandReceived(self, zwave_command):
        try:
            self.process_zwave_interpretation(ZW_RECEIVED, zwave_command)

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def zwaveCommandSent(self, zwave_command):
        try:
            self.process_zwave_interpretation(ZW_SENT, zwave_command)

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    #################################
    #
    # Start of bespoke plugin methods
    #
    #################################

    def add_interpreted_zwave_devices(self, values_dict, type_id):  # noqa [Unused local symbols]
        try:
            for dev_id in values_dict["available_zwave_devices_list"]:
                zwave_dev_id = int(dev_id)  # noqa [Duplicated code fragment!]
                zwave_dev_name = self.zwave_available_devices.pop(zwave_dev_id)

                zwave_dev = indigo.devices[zwave_dev_id]
                props = zwave_dev.pluginProps
                props["zwave_interpretation"] = True
                zwave_dev.replacePluginPropsOnServer(props)

                self.zwave_interpreted_devices[zwave_dev_id] = zwave_dev_name

                interpreted_zwave_devices_list = list()
                for zwave_dev_id, zwave_dev_name in self.zwave_interpreted_devices.items():
                    interpreted_zwave_devices_list.append(int(zwave_dev_id))
                self.zwave_interpreter_class_instance.interpret_list(False, interpreted_zwave_devices_list)

            return values_dict

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def build_interpreted_zwave_devices_list(self, filter="", values_dict=None, type_id="", target_id=0):  # noqa [Unused local symbols]
        try:
            interpreted_zwave_devices_list = list()
            for zwave_dev_id, zwave_dev_name in self.zwave_interpreted_devices.items():
                interpreted_zwave_devices_list.append((zwave_dev_id, zwave_dev_name))

            return sorted(interpreted_zwave_devices_list, key=lambda item: item[1])  # Sort list by Device Name

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def build_available_zwave_devices_list(self, filter="", values_dict=None, type_id="", target_id=0):  # noqa [Unused local symbols]
        try:
            available_zwave_devices_list = list()
            for zwave_dev_id, zwave_dev_name in self.zwave_available_devices.items():
                available_zwave_devices_list.append((zwave_dev_id, zwave_dev_name))

            return sorted(available_zwave_devices_list, key=lambda item: item[1])  # Sort list by Device Name

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def mkdir_with_mode(self, directory):
        try:
            # Forces Read | Write on creation so that the plugin can delete the folder id required
            if not os.path.isdir(directory):
                old_mask = os.umask(000)
                os.makedirs(directory, 0o777)
                os.umask(old_mask)
        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def process_zwave_interpretation(self, send_receive_option, zwave_command):
        try:
            zw_interpretation = self.zwave_interpreter_class_instance.interpret_zwave(send_receive_option, zwave_command)
            if zw_interpretation[ZW_INTERPRETATION_ATTEMPTED]:
                # self.logger.warning("Z-Wave Interpreted")
                self.zwave_log(zw_interpretation[ZW_INTERPRETATION_OVERVIEW_UI], zw_interpretation[ZW_INTERPRETATION_DETAIL_UI])

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def remove_interpreted_zwave_devices(self, values_dict, type_id):  # noqa [Unused local symbols]
        try:
            for dev_id in values_dict["interpreted_zwave_devices_list"]:
                zwave_dev_id = int(dev_id)  # noqa [Duplicated code fragment!]
                zwave_dev_name = self.zwave_interpreted_devices.pop(zwave_dev_id)

                zwave_dev = indigo.devices[zwave_dev_id]
                props = zwave_dev.pluginProps
                props["zwave_interpretation"] = False
                zwave_dev.replacePluginPropsOnServer(props)

                self.zwave_available_devices[zwave_dev_id] = zwave_dev_name

                interpreted_zwave_devices_list = list()
                for zwave_dev_id, zwave_dev_name in self.zwave_interpreted_devices.items():
                    interpreted_zwave_devices_list.append(int(zwave_dev_id))
                self.zwave_interpreter_class_instance.interpret_list(False, interpreted_zwave_devices_list)

            return values_dict

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement

    def zwave_log(self, overview, detail):
        try:
            def zwave_log_to_file(_overview, _detail, logfile_path_and_name):
                try:
                    f = open(logfile_path_and_name, "ab")
                    f.write(_overview)
                    f.write(str.encode("\n"))
                    f.write(_detail)
                    f.write(str.encode("\n\n"))
                    f.close()
                except IOError as io_error_message:
                    self.logger.error(f"Z-wave Logging error: {io_error_message}")

            now = datetime.now()  # current date and time
            logged_date_time = (now.strftime("%Y-%m-%d %H:%M:%S.%f"))[:-3]  # e.g. '2020-11-03 00:00:11.688'
            output_overview = (f"{logged_date_time} {overview}").encode("utf8")
            output_detail = (f"                              {detail}").encode("utf8")

            if bool(self.pluginPrefs.get("zwaveLogToStandAloneFileOption", False)):
                if not os.path.exists(self.pluginPrefs["standAloneZwaveLogFolderPath"]):
                    self.mkdir_with_mode(self.pluginPrefs["standAloneZwaveLogFolderPath"])

                logfile_name = f"{self.pluginPrefs[u'standAloneZwaveLogFolderPath']}/{self.pluginPrefs[u'standAloneZwaveLogFileName']}"
                zwave_log_to_file(output_overview, output_detail, logfile_name)

            if self.logger.getEffectiveLevel() <= 10:
                self.logger.debug(f"{logged_date_time} {overview}\n                                   {detail}\n")

        except Exception as exception_error:
            self.exception_handler(exception_error, True)  # Log error and display failing statement
