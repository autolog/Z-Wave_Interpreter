#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Z-Wave Interpreter © Autolog 2020
#

import sys

from .zwave_constants import *
from .zwave_constants_interpretation import *
from .zwave_constants_command_classes import *

ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR = 0x01
ZW_SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT = 0x02
ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE = 0x03
ZW_SENSOR_MULTILEVEL_GET = 0x04
ZW_SENSOR_MULTILEVEL_REPORT = 0x05
ZW_SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT = 0x06

ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE = 0x01
ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE = 0x02
ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE = 0x03
ZW_SENSOR_MULTILEVEL_TYPE_POWER = 0x04
ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY = 0x05

ZW_SENSOR_MULTILEVEL_TYPE_VELOCITY = 0x06
ZW_SENSOR_MULTILEVEL_TYPE_DIRECTION = 0x07
ZW_SENSOR_MULTILEVEL_TYPE_ATMOSPHERIC_PRESSURE = 0x08
ZW_SENSOR_MULTILEVEL_TYPE_BAROMTERIC_PRESSURE = 0x09
ZW_SENSOR_MULTILEVEL_TYPE_SOLAR_RADIATION = 0x0A

ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT = 0x0B

ZW_SENSOR_MULTILEVEL_TYPE_RAIN_RATE = 0x0C
ZW_SENSOR_MULTILEVEL_TYPE_TIDE_LEVEL = 0x0D
ZW_SENSOR_MULTILEVEL_TYPE_WEIGHT = 0x0E
ZW_SENSOR_MULTILEVEL_TYPE_VOLTAGE = 0x0F
ZW_SENSOR_MULTILEVEL_TYPE_CURRENT = 0x10
ZW_SENSOR_MULTILEVEL_TYPE_CO2_LEVEL = 0x11
ZW_SENSOR_MULTILEVEL_TYPE_AIR_FLOW = 0x12
ZW_SENSOR_MULTILEVEL_TYPE_TANK_CAPACITY = 0x13
ZW_SENSOR_MULTILEVEL_TYPE_DISTANCE = 0x14
ZW_SENSOR_MULTILEVEL_TYPE_ANGLE_POSITION = 0x15
ZW_SENSOR_MULTILEVEL_TYPE_ROTATION = 0x16
ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE = 0x17
ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE = 0x18
ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_INTENSITY = 0x19
ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_MAGNITUDE = 0x1A

ZW_SENSOR_MULTILEVEL_TYPE_ULTRAVIOLET = 0x1B

ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_RESISTIVITY = 0x1C
ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_CONDUCTIVITY = 0x1D
ZW_SENSOR_MULTILEVEL_TYPE_LOUDNESS = 0x1E
ZW_SENSOR_MULTILEVEL_TYPE_MOISTURE = 0x1F

ZW_SENSOR_MULTILEVEL_TYPE_FREQUENCY = 0x20
ZW_SENSOR_MULTILEVEL_TYPE_TIME = 0x21
ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE = 0x22
ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_2_5 = 0x23
ZW_SENSOR_MULTILEVEL_TYPE_FORMALDEHYDE_CH2O_LEVEL = 0x24
ZW_SENSOR_MULTILEVEL_TYPE_RADON_CONCENTRATION = 0x25
ZW_SENSOR_MULTILEVEL_TYPE_METHANE_CH4_DENSITY = 0x26
ZW_SENSOR_MULTILEVEL_TYPE_VOLATILE_ORGANIC_COMPOUND_LEVEL = 0x27
ZW_SENSOR_MULTILEVEL_TYPE_CARBON_MONOXIDE_CO_LEVEL = 0x28
ZW_SENSOR_MULTILEVEL_TYPE_SOIL_HUMIDITY = 0x29
ZW_SENSOR_MULTILEVEL_TYPE_SOIL_REACTIVITY = 0x2A
ZW_SENSOR_MULTILEVEL_TYPE_SOIL_SALINITY = 0x2B
ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE = 0x2C
ZW_SENSOR_MULTILEVEL_TYPE_BLOOD_PRESSURE = 0x2D
ZW_SENSOR_MULTILEVEL_TYPE_MUSCLE_MASS = 0x2E
ZW_SENSOR_MULTILEVEL_TYPE_FAT_MASS = 0x2F

ZW_SENSOR_MULTILEVEL_TYPE_BONE_MASS = 0x30
ZW_SENSOR_MULTILEVEL_TYPE_TOTAL_BODY_WATER_TBW = 0x31
ZW_SENSOR_MULTILEVEL_TYPE_BASIS_METABOLIC_RATE_BMR = 0x32
ZW_SENSOR_MULTILEVEL_TYPE_BODY_MASS_INDEX_BMI = 0x33
ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_X_AXIS = 0x34
ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Y_AXIS = 0x35
ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Z_AXIS = 0x36
ZW_SENSOR_MULTILEVEL_TYPE_SMOKE_DENSITY = 0x37
ZW_SENSOR_MULTILEVEL_TYPE_WATER_FLOW = 0x38
ZW_SENSOR_MULTILEVEL_TYPE_WATER_PRESSURE = 0x39
ZW_SENSOR_MULTILEVEL_TYPE_RF_SIGNAL_STRENGTH = 0x3A
ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_10 = 0x3B
ZW_SENSOR_MULTILEVEL_TYPE_RESPIRATORY_RATE = 0x3C
ZW_SENSOR_MULTILEVEL_TYPE_RELATIVE_MODULATION_LEVEL = 0x3D
ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE = 0x3E
ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE = 0x3F

ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE = 0x40
ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE = 0x41
ZW_SENSOR_MULTILEVEL_TYPE_WATER_CHLORINE_LEVEL = 0x42
ZW_SENSOR_MULTILEVEL_TYPE_WATER_ACIDITY = 0x43
ZW_SENSOR_MULTILEVEL_TYPE_WATER_OXIDATION_REDUCTION_POTENTIA = 0x44
ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE_LF_HF_RATIO = 0x45
ZW_SENSOR_MULTILEVEL_TYPE_MOTION_DIRECTION = 0x46
ZW_SENSOR_MULTILEVEL_TYPE_APPLIED_FORCE_ON_THE_SENSOR = 0x47
ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE = 0x48
ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE = 0x49
ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE = 0x4A
ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE = 0x4B
ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE = 0x4C
ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE = 0x4D
ZW_SENSOR_MULTILEVEL_TYPE_SUCTION_INPUT_PUMP_COMPRESSOR_PRESSURE = 0x4E
ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_OUTPUT_PUMP_COMPRESSOR_PRESSURE = 0x4F

ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST = 0x50
ZW_SENSOR_MULTILEVEL_TYPE_OZONE_O3 = 0x51
ZW_SENSOR_MULTILEVEL_TYPE_SULFUR_DIOXIDE_SO2 = 0x52
ZW_SENSOR_MULTILEVEL_TYPE_NITROGEN_DIOXIDE_NO2 = 0x53
ZW_SENSOR_MULTILEVEL_TYPE_AMMONIA_NH3 = 0x54
ZW_SENSOR_MULTILEVEL_TYPE_LEAD_PB = 0x55
ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_1 = 0x56

ZW_SCALE_CELSIUS = 0x00
ZW_SCALE_FAHRENHEIT = 0x01
ZW_SCALE_PERCENTAGE = 0x00
ZW_SCALE_LUX = 0x01
ZW_SCALE_HUMIDITY = 0x01
ZW_SCALE_DIMENSIONLESS_VALUE = 0x01
ZW_SCALE_WATT = 0x00
ZW_SCALE_BTU_H = 0x01
ZW_SCALE_UV_INDEX = 0x00


class ZwaveSensorMultilevel():
    """
    Z-Wave Command Class: Thermostat Multilevel "0x31" [Decimal 49]

    """

    #     def __init__(self, logger, utility, command_classes, zw_interpretation):
    def __init__(self, parent):
        try:
            self.logger = parent.logger
            self.utility = parent.utility
            self.command_classes = parent.zw_command_classes
            self.zw_interpretation = parent.zw_interpretation

            self.command_classes[ZW_SENSOR_MULTILEVEL] = dict()
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_IDENTIFIER] = u"Multilevel Sensor"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS] = dict()
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR] = u"Get Supported Sensor"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT] = u"Supported Sensor Report"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE] = u"Get Supported Scale"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_GET] = u"Get"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_REPORT] = u"Report"
            self.command_classes[ZW_SENSOR_MULTILEVEL][ZW_COMMANDS][ZW_SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT] = u"Supported Scale Report"

            self.zw_sensor_multilevel_types = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE][ZW_IDENTIFIER] = u"Air Temperature"  # 0x01
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE][ZW_IDENTIFIER] = u"General Purpose"  # 0x02
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE][ZW_SCALES][ZW_SCALE_PERCENTAGE] = (u"Percentage Value (%)", u"%")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_GENERAL_PURPOSE][ZW_SCALES][ZW_SCALE_DIMENSIONLESS_VALUE] = (u"Dimensionless", u" Dimensionless")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE][ZW_IDENTIFIER] = u"Illuminance"  # 0x03
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE][ZW_SCALES][ZW_SCALE_PERCENTAGE] = (u"Percentage Value (%)", u"%")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ILLUMINANCE][ZW_SCALES][ZW_SCALE_LUX] = (u"Lux", u" Lux")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_POWER] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_POWER][ZW_IDENTIFIER] = u"Power"  # 0x04
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_POWER][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_POWER][ZW_SCALES][ZW_SCALE_WATT] = (u"Watt (W)", u" W")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_POWER][ZW_SCALES][ZW_SCALE_BTU_H] = (u"Btu/h", u" Btu/h")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY][ZW_IDENTIFIER] = u"Humidity"  # 0x05
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY][ZW_SCALES][ZW_SCALE_PERCENTAGE] = (u"Percentage Value (%)", u"%")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HUMIDITY][ZW_SCALES][ZW_SCALE_HUMIDITY] = (u"Absolute humidity (g/m3)", u" g/m3")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VELOCITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VELOCITY][ZW_IDENTIFIER] = u"Velocity"  # 0x06

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DIRECTION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DIRECTION][ZW_IDENTIFIER] = u"Direction"  # 0x07

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ATMOSPHERIC_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ATMOSPHERIC_PRESSURE][ZW_IDENTIFIER] = u"Atmospheric pressure"  # 0x08

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BAROMTERIC_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BAROMTERIC_PRESSURE][ZW_IDENTIFIER] = u"Barometric pressure"  # 0x09

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOLAR_RADIATION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOLAR_RADIATION][ZW_IDENTIFIER] = u"Solar radiation"  # 0x0A

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT][ZW_IDENTIFIER] = u"Dew Point"  # 0x0B
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEW_POINT][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RAIN_RATE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RAIN_RATE][ZW_IDENTIFIER] = u"Rain Rate"  # 0x0C

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TIDE_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TIDE_LEVEL][ZW_IDENTIFIER] = u"Tide Level"  # 0x0D

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WEIGHT] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WEIGHT][ZW_IDENTIFIER] = u"Weight"  # 0x0E

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VOLTAGE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VOLTAGE][ZW_IDENTIFIER] = u"Voltage"  # 0x0F

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CURRENT] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CURRENT][ZW_IDENTIFIER] = u"Current"  # 0x10

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CO2_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CO2_LEVEL][ZW_IDENTIFIER] = u"Carbon Dioxide [CO2] Level"  # 0x11

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_FLOW] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AIR_FLOW][ZW_IDENTIFIER] = u"Air Flow"  # 0x12

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TANK_CAPACITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TANK_CAPACITY][ZW_IDENTIFIER] = u"Tank Capacity"  # 0x13

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISTANCE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISTANCE][ZW_IDENTIFIER] = u"Distance"  # 0x14

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ANGLE_POSITION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ANGLE_POSITION][ZW_IDENTIFIER] = u"Angle Position"  # 0x15

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ROTATION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ROTATION][ZW_IDENTIFIER] = u"Rotation"  # 0x16

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE][ZW_IDENTIFIER] = u"Water Temperature"  # 0x17
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE][ZW_IDENTIFIER] = u"Soil Temperature"  # 0x18
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_INTENSITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_INTENSITY][ZW_IDENTIFIER] = u"Seismic Intensity"  # 0x19

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_MAGNITUDE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SEISMIC_MAGNITUDE][ZW_IDENTIFIER] = u"Seismic Magnitude"  # 0x1A

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ULTRAVIOLET] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ULTRAVIOLET][ZW_IDENTIFIER] = u"Ultraviolet"  # 0x1B
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ULTRAVIOLET][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ULTRAVIOLET][ZW_SCALES][ZW_SCALE_UV_INDEX] = (u"UV Index", u" UV Index")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_RESISTIVITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_RESISTIVITY][ZW_IDENTIFIER] = u"Electrical Resistivity"  # 0x1C

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_CONDUCTIVITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ELECTRICAL_CONDUCTIVITY][ZW_IDENTIFIER] = u"Electrical Conductivity"  # 0x1D

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LOUDNESS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LOUDNESS][ZW_IDENTIFIER] = u"Loudness"  # 0x1E

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MOISTURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MOISTURE][ZW_IDENTIFIER] = u"Moisture"  # 0x1F

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FREQUENCY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FREQUENCY][ZW_IDENTIFIER] = u"Frequency"  # 0x20

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TIME] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TIME][ZW_IDENTIFIER] = u"Time"  # 0x21

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE][ZW_IDENTIFIER] = u"Target Temperature"  # 0x22
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TARGET_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_2_5] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_2_5][ZW_IDENTIFIER] = u"Particulate Matter 2.5"  # 0x23

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FORMALDEHYDE_CH2O_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FORMALDEHYDE_CH2O_LEVEL][ZW_IDENTIFIER] = u"Formaldehyde [CH2O] Level"  # 0x24

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RADON_CONCENTRATION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RADON_CONCENTRATION][ZW_IDENTIFIER] = u"Radon Concentration"  # 0x25

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_METHANE_CH4_DENSITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_METHANE_CH4_DENSITY][ZW_IDENTIFIER] = u"Methane [CH4] Density"  # 0x26

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VOLATILE_ORGANIC_COMPOUND_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_VOLATILE_ORGANIC_COMPOUND_LEVEL][ZW_IDENTIFIER] = u"Volatile Organic Compound Level"  # 0x27

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CARBON_MONOXIDE_CO_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CARBON_MONOXIDE_CO_LEVEL][ZW_IDENTIFIER] = u"Carbon Monoxide [CO] Level"  # 0x28

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_HUMIDITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_HUMIDITY][ZW_IDENTIFIER] = u"Soil Humidity"  # 0x29

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_REACTIVITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_REACTIVITY][ZW_IDENTIFIER] = u"Soil Reactivity"  # 0x2A

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_SALINITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SOIL_SALINITY][ZW_IDENTIFIER] = u"Soil Salinity"  # 0x2B

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE][ZW_IDENTIFIER] = u"Heart Rate"  # 0x2C

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BLOOD_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BLOOD_PRESSURE][ZW_IDENTIFIER] = u"Blood Pressure"  # 0x2D

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MUSCLE_MASS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MUSCLE_MASS][ZW_IDENTIFIER] = u"Muscle Mass"  # 0x2E

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FAT_MASS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_FAT_MASS][ZW_IDENTIFIER] = u"Fat Mass"  # 0x2F

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BONE_MASS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BONE_MASS][ZW_IDENTIFIER] = u"Bone Mass"  # 0x30

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TOTAL_BODY_WATER_TBW] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_TOTAL_BODY_WATER_TBW][ZW_IDENTIFIER] = u"Total Body Water [TBW]"  # 0x31

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BASIS_METABOLIC_RATE_BMR] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BASIS_METABOLIC_RATE_BMR][ZW_IDENTIFIER] = u"Basis Metabolic Rate [BMR]"  # 0x32

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BODY_MASS_INDEX_BMI] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BODY_MASS_INDEX_BMI][ZW_IDENTIFIER] = u"Body Mass Index [BMI]"  # 0x33

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_X_AXIS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_X_AXIS][ZW_IDENTIFIER] = u"Acceleration X-Axis"  # 0x34

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Y_AXIS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Y_AXIS][ZW_IDENTIFIER] = u"Acceleration Y-Axis"  # 0x35

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Z_AXIS] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_ACCELERATION_Z_AXIS][ZW_IDENTIFIER] = u"Acceleration Z-Axis"  # 0x36

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SMOKE_DENSITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SMOKE_DENSITY][ZW_IDENTIFIER] = u"Smoke Density"  # 0x37

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_FLOW] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_FLOW][ZW_IDENTIFIER] = u"Water Flow"  # 0x38

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_PRESSURE][ZW_IDENTIFIER] = u"Water Pressure"  # 0x39

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RF_SIGNAL_STRENGTH] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RF_SIGNAL_STRENGTH][ZW_IDENTIFIER] = u"RF Signal Strength"  # 0x3A

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_10] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_10][ZW_IDENTIFIER] = u"Particulate Matter 10"  # 0x3B

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RESPIRATORY_RATE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RESPIRATORY_RATE][ZW_IDENTIFIER] = u"Respiratory Rate"  # 0x3C

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RELATIVE_MODULATION_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RELATIVE_MODULATION_LEVEL][ZW_IDENTIFIER] = u"Relative Modulation Level"  # 0x3D

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE][ZW_IDENTIFIER] = u"Boiler Water Temperature"  # 0x3E
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_BOILER_WATER_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE][ZW_IDENTIFIER] = u"Domestic Hot Water [DHW] Temperature"  # 0x3F
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DOMESTIC_HOT_WATER_DHW_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE][ZW_IDENTIFIER] = u"Outside Temperature"  # 0x40
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OUTSIDE_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE][ZW_IDENTIFIER] = u"Exhaust Temperature"  # 0x41
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EXHAUST_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_CHLORINE_LEVEL] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_CHLORINE_LEVEL][ZW_IDENTIFIER] = u"Water Chlorine Level"  # 0x42

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_ACIDITY] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_ACIDITY][ZW_IDENTIFIER] = u"Water Acidity"  # 0x43

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_OXIDATION_REDUCTION_POTENTIA] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_WATER_OXIDATION_REDUCTION_POTENTIA][ZW_IDENTIFIER] = u"Water Oxidation Reduction Potential"  # 0x44

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE_LF_HF_RATIO] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_HEART_RATE_LF_HF_RATIO][ZW_IDENTIFIER] = u"Heart Rate LF/HF Ratio"  # 0x45

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MOTION_DIRECTION] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_MOTION_DIRECTION][ZW_IDENTIFIER] = u"Motion Direction"  # 0x46

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_APPLIED_FORCE_ON_THE_SENSOR] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_APPLIED_FORCE_ON_THE_SENSOR][ZW_IDENTIFIER] = u"Applied Force On The Sensor"  # 0x47

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE][ZW_IDENTIFIER] = u"Return Air Temperature"  # 0x48
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_RETURN_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE][ZW_IDENTIFIER] = u"Supply Air Temperature"  # 0x49
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUPPLY_AIR_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE][ZW_IDENTIFIER] = u"Condenser Coil Temperature"  # 0x4A
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_CONDENSER_COIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE][ZW_IDENTIFIER] = u"Evaporator Coil Temperature"  # 0x4B
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_EVAPORATOR_COIL_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE][ZW_IDENTIFIER] = u"Liquid Line Temperature"  # 0x4C
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LIQUID_LINE_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE][ZW_IDENTIFIER] = u"Discharge Line Temperature"  # 0x4D
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_LINE_TEMPERATURE][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUCTION_INPUT_PUMP_COMPRESSOR_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SUCTION_INPUT_PUMP_COMPRESSOR_PRESSURE][ZW_IDENTIFIER] = u"Suction [Input Pump/Compressor] Pressure"  # 0x4E

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_OUTPUT_PUMP_COMPRESSOR_PRESSURE] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DISCHARGE_OUTPUT_PUMP_COMPRESSOR_PRESSURE][ZW_IDENTIFIER] = u"Discharge (output Pump/compressor) Pressure"  # 0x4F

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST][ZW_IDENTIFIER] = u"Defrost Temperature [Sensor Used To Decide When To Defrost]"  # 0x50
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST][ZW_SCALES] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST][ZW_SCALES][ZW_SCALE_CELSIUS] = (u"Celsius (C)", u"º C")
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_DEFROST_TEMPERATURE_SENSOR_USED_TO_DECIDE_WHEN_TO_DEFROST][ZW_SCALES][ZW_SCALE_FAHRENHEIT] = (u"Fahrenheit (F)", u"º F")

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OZONE_O3] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_OZONE_O3][ZW_IDENTIFIER] = u"Ozone (o3)"  # 0x51

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SULFUR_DIOXIDE_SO2] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_SULFUR_DIOXIDE_SO2][ZW_IDENTIFIER] = u"Sulfur Dioxide (so2)"  # 0x52

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_NITROGEN_DIOXIDE_NO2] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_NITROGEN_DIOXIDE_NO2][ZW_IDENTIFIER] = u"XXXNitrogen Dioxide (no2)XXXXXXX"  # 0x53

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AMMONIA_NH3] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_AMMONIA_NH3][ZW_IDENTIFIER] = u"Ammonia (nh)"  # 0x54

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LEAD_PB] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_LEAD_PB][ZW_IDENTIFIER] = u"Lead (pb)"  # 0x55

            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_1] = dict()
            self.zw_sensor_multilevel_types[ZW_SENSOR_MULTILEVEL_TYPE_PARTICULATE_MATTER_1][ZW_IDENTIFIER] = u"Particulate Matter 1"  # 0x56

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveSensorMultilevel' Class, '__init__' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def interpret(self, zw_command, zw_command_detail):
        try:
            if zw_command == ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR:
                pass
            elif zw_command == ZW_SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT:
                pass
            elif zw_command == ZW_SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE:
                pass
            elif zw_command == ZW_SENSOR_MULTILEVEL_GET:
                self._interpret_get(zw_command_detail)
                return
            elif zw_command == ZW_SENSOR_MULTILEVEL_REPORT:
                self._interpret_report(zw_command_detail)
                return
            elif zw_command == ZW_SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT:
                pass

            error_message = self.utility.not_supported(self.zw_interpretation)
            self.zw_interpretation[ZW_ERROR_MESSAGE] = error_message

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveSensorMultilevel' Class, 'interpret' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_get(self, zw_command_detail):
        try:
            self.zw_interpretation[ZW_INTERPRETATION_UI] = (u"Class: '{0} [{1}]', Command: '{2}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI]))

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveSensorMultilevel' Class, '_interpret_get' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))

    def _interpret_report(self, zw_command_detail):
        try:
            # sensor_type = self.zw_interpretation[ZW_COMMAND_DETAIL][0]
            # precision_scale_size = self.zw_interpretation[ZW_COMMAND_DETAIL][1]
            sensor_type = zw_command_detail[0]
            precision_scale_size = zw_command_detail[1]
            precision = (precision_scale_size & 0b11100000) >> 5
            scale = (precision_scale_size & 0b00011000) >> 3
            if sensor_type in self.zw_sensor_multilevel_types:
                if scale in self.zw_sensor_multilevel_types[sensor_type][ZW_SCALES]:
                    scale_ui = self.zw_sensor_multilevel_types[sensor_type][ZW_SCALES][scale][0]
                    scale_ui_compact = self.zw_sensor_multilevel_types[sensor_type][ZW_SCALES][scale][1]
                else:
                    scale_ui = scale_ui_compact = (u" [Unknown Scale: {0}]".format(scale))
            else:
                scale_ui = scale_ui_compact = (u" [Unknown Scale: {0}]".format(scale))
            size = precision_scale_size & 0b00000111
            end_value = 2 + size
            # value = self.utility.bytes_to_int(self.zw_interpretation[ZW_COMMAND_DETAIL][2:end_value])
            # if self.zw_interpretation[ZW_COMMAND_DETAIL][2] & 0b10000000:  # Check if a negative number (high order bit set)
            value = self.utility.bytes_to_int(zw_command_detail[2:end_value])
            if zw_command_detail[2] & 0b10000000:  # Check if a negative number (high order bit set)
                value = self.utility.twos_complement(value, size * 8)
            # value = float(value)/10**precision  # Set precision e.g. 1859 > 18.59 if precision = 2
            value_ui_format = "{{:.{0}f}}".format(precision)
            value_ui = value_ui_format.format(float(value) / 10 ** precision)

            self.zw_interpretation[ZW_SENSOR_TYPE] = sensor_type
            if sensor_type in self.zw_sensor_multilevel_types:
                self.zw_interpretation[ZW_SENSOR_TYPE_UI] = self.zw_sensor_multilevel_types[sensor_type][ZW_IDENTIFIER]
            else:
                self.zw_interpretation[ZW_SENSOR_TYPE_UI] = "Sensor Type {0} unknown".format(sensor_type)
            self.zw_interpretation[ZW_PRECISION] = precision
            self.zw_interpretation[ZW_SCALES] = scale
            self.zw_interpretation[ZW_SCALE_UI] = scale_ui
            self.zw_interpretation[ZW_SCALE_UI_COMPACT] = scale_ui_compact
            self.zw_interpretation[ZW_SIZE] = size
            self.zw_interpretation[ZW_VALUE] = value
            self.zw_interpretation[ZW_VALUE_UI] = value_ui

            zw_interpretation_ui = (u"Class: '{0} [{1}]', Command: '{2}', Sensor: '{3}', Value: '{4}{5}'"
                                                            .format(self.zw_interpretation[ZW_COMMAND_CLASS_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_CLASS_VERSION_UI],
                                                                    self.zw_interpretation[ZW_COMMAND_UI],
                                                                    self.zw_interpretation[ZW_SENSOR_TYPE_UI],
                                                                    self.zw_interpretation[ZW_VALUE_UI],
                                                                    self.zw_interpretation[ZW_SCALE_UI_COMPACT]))

            self.zw_interpretation[ZW_INTERPRETATION_UI] = zw_interpretation_ui

            self.zw_interpretation[ZW_INTERPRETED] = True

        except StandardError as standard_error_message:
            result_message = u"Error detected in 'ZwaveSensorMultilevel' Class, '_interpret_report' method"
            self.logger.error(u"{0}: Line {1} has error '{2}'".format(result_message, sys.exc_traceback.tb_lineno, standard_error_message))
