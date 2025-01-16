"""Const of iNels BUS tests."""

TEST_API_READ_DATA = "_Api__readDeviceData"
TEST_API_ROOM_DEVICES = "getRoomDevicesRaw"
TEST_API_FETCH_ALL_DEVICES = "fetch_all_devices"

TEST_API_NAMESPACE = "pyinels.api"
TEST_API_CLASS_NAMESPACE = "pyinels.api.Api"

TEST_DATA_THERM = {
    'title': 'Valve in bedroom',
    'temp': 'Bedroom_temerature',
    'rele': 'DIGITALGROUP_0001',
    'read_only': 'no',
    'temp_set': 'Bedroom_stateth'
}

TEST_DATA_LIGHT = {
    'title': 'Main light',
    'id': 'SV_12_Garage',
    'read_only': 'no'
}

TEST_DATA_SWITCH = {
    'title': 'Kitchen kettel switch',
    'id': 'KITCHEN_KETTLE_SWITCH',
    'read_only': 'no'
}

TEST_DATA_SHUTTER = {
    'title': 'Kitchen shuuter',
    'up': 'KITCHEN_SHUUTER_1_UP',
    'down': 'KITCHEN_SHUUTER_1_DOWN',
    'read_only': 'no'
}

TEST_DATA_DOOR = {
    'title': 'Garage door',
    'id': 'GARAGE_DOOR',
    'read_only': 'no'
}

TEST_DATA_HEATING = {
    'title': 'Holiday',
    'id': 'HOLIDAY_HEATING',
    'read_only': 'no'
}

TEST_HOST = "http://localhost"

TEST_INELS_DEVICE_NAMESPACE = "pyinels.device.Device"

TEST_PORT = "1000"

TEST_RESOURCE_SWITCH = {
    'column': '0',
    'group': 'basement',
    'inels': 'ZA_14_basement',
    'name': 'Office switch',
    'read_only': 'no',
    'row': '1',
    'type': 'switch'
}

TEST_SHUTTER_UP = "ZAL__ahor"
TEST_SHUTTER_DOWN = "Z_Obk_do"
TEST_SHUTTER_ID = f"{TEST_SHUTTER_UP}_{TEST_SHUTTER_DOWN}"
TEST_SHUTTER_NAME = "Zal OB"

TEST_RETURN_RESOURCE_SHUTTER = {
    f'{TEST_SHUTTER_DOWN}': 0,
    f'{TEST_SHUTTER_UP}': 0
}

TEST_RETURN_RESOURCE_SHUTTER_UP = {
    f'{TEST_SHUTTER_DOWN}': 0,
    f'{TEST_SHUTTER_UP}': 1
}

TEST_RETURN_RESOURCE_SHUTTER_DOWN = {
    f'{TEST_SHUTTER_DOWN}': 1,
    f'{TEST_SHUTTER_UP}': 0
}

TEST_RAW_LIGHT = """
lights:
name="Main light" column="0" inels="SV_12_Garage" read_only="no" row="0"
"""

TEST_RAW_SWITCH = """
on_off:
name="Zas loznice" column="3" inels="ZAS_13A_Loznice" read_only="no" row="0"
"""

TEST_RAW_GARAGE_DOOR = """
garage:
name="Vrata" column="0" inels="Vrata_Garaz" read_only="no" row="1"
"""

TEST_RAW_SCENE = """
scenes:
name="start irrigation immediately" column="0" row="2" abs_path="/etc/imm/scripts/irrigate_immediately.py"
""" # noqa E501

TEST_RAW_SHUTTER = """shutters:
name="Zal OB" column="0" down="Z_Obk_do" read_only="no" up="ZAL__ahor" row="3"
"""

TEST_RAW_DUPLICIT_DEVICES = """on_off:
name="Zas OB" column="0" inels="ZAS_1A_Obyvak" read_only="no" row="2"
name="Zas POK" column="1" inels="ZAS_1B_Pokoj_dole" read_only="no" row="2"
name="Zas POK" column="1" inels="ZAS_1B_Pokoj_dole" read_only="no" row="2"
thermals:
name="Obyvak" inels="Koupelna_dole_StateTH" placement="indoor"
heating:
name="DOVOLENA" column="0" inels="DIGITALGROUP_0001" read_only="no" row="5"
lights:
name="Obyvak" column="0" inels="SV_1_Obyvak_strop" read_only="no" row="0"
name="Stul" column="1" inels="SV_2_Jidelni_stul" read_only="no" row="0"
name="Kuchyn" column="2" inels="SV_3_Kuchyn" read_only="no" row="0"
name="Linka" column="3" inels="SV_4_Kuchyn_linka" read_only="no" row="0"
name="Schody" column="0" inels="SV_15_Schodiste" read_only="no" row="1"
name="Vstup" column="1" inels="SV_10_Chodba_dole" read_only="no" row="1"
name="Pokoj" column="2" inels="SV_7_Pokoj_dole" read_only="no" row="1"
name="Koupelna" column="3" inels="SV_9_Koupelna_dole" read_only="no" row="1"
name="Technicka" column="4" inels="SV_11_Technicka_1." read_only="no" row="1"
name="Pod schody" column="5" inels="SV_14_Kumbal_rozvc" read_only="no" row="1"
shutters:
name="Zal OB" column="0" down="Z_Obk_do" read_only="no" up="ZAL__ahor" row="3"
name="Rol KRB" column="1" down="ROL_Jillu" read_only="no" up="ROJidru" row="3"
name="Rol KUCH" column="2" down="RL_Kc_do" read_only="no" up="ROuchyu" row="3"
name="Rol POK" column="3" down="R_Po_dou" read_only="no" up="ROnahoru" row="3"
heat-control:
name="Obyvak" read_only="no" therm="O" column="0" stateth="O" rele="D" row="4"
name="Pokoj" read_only="no" therm="P" column="1" stateth="P" rele="D" row="4"
name="Koupel" read_only="no" therm="K" column="2" stateth="K" rele="D" row="4"
name="Zadveri" read_only="no" therm="V" column="3" stateth="V" rele="D" row="4"
name="Obyvak" read_only="no" therm="O" column="0" stateth="O" rele="D" row="4"
name="Pokoj" read_only="no" therm="P" column="1" stateth="P" rele="D" row="4"
name="Koupel" read_only="no" therm="K" column="2" stateth="K" rele="D" row="4"
name="Zadveri" read_only="no" therm="V" column="3" stateth="V" rele="D" row="4"
lights:
name="Fasada" column="0" inels="SV_6_Terasa_Fasada" read_only="no" row="0"
name="Garaz zadni vch" column="1" inels="SV_G_Za_V" read_only="no" row="0"
name="Terasa" column="2" inels="SV_Terasa_Zem" read_only="no" row="0"
name="Vchod a garaz" column="3" inels="SV_10_Ven_Garaz" read_only="no" row="0"
shutters:
name="Markyza" column="0" down="Marky_d" read_only="no" up="Marky_n" row="1"
lights:
name="Loznice" column="0" inels="SV_19_Loznice" read_only="no" row="0"
name="Satna" column="1" inels="SV_20_Loznice_satna" read_only="no" row="0"
name="Zachod" column="0" inels="SV_21_WC_patro" read_only="no" row="1"
name="Chodba" column="1" inels="SV_18_Chodba_2.NP" read_only="no" row="1"
name="Schodiste" column="2" inels="SV_15_Schodiste" read_only="no" row="1"
name="Puda" column="3" inels="SV_Puda" read_only="no" row="1"
name="Koupelna" column="0" inels="SV_22_Koupelna_nahore" read_only="no" row="2"
name="Umyvadlo" column="1" inels="SV_22_Umyvadlo" read_only="no" row="2"
name="Pokoj V." column="0" inels="SV_17_Pokoj_levy" read_only="no" row="3"
on_off:
name="Zas loznice" column="3" inels="ZAS_13A_Loznice" read_only="no" row="0"
name="Zas pok V." column="2" inels="ZAS_12B_Pokoj_levy" read_only="no" row="3"
name="Zas pok Z." column="1" inels="ZAS_12A_Pokoj_pravy" read_only="no" row="4"
heat-control:
name="Lozni" read_only="no" therm="Lo" column="2" stateth="LH" rele="D" row="0"
name="Koupa" read_only="no" therm="Ko" column="2" stateth="KH" rele="D" row="2"
name="Po V." read_only="no" therm="Pl" column="1" stateth="PT" rele="D" row="3"
name="Po Z." read_only="no" therm="Pp" column="0" stateth="PH" rele="D" row="4"
lights:
name="Hl. světlo" column="0" inels="SV_12_Garaz" read_only="no" row="0"
name="Půda" column="1" inels="SV_Puda_Garaz" read_only="no" row="0"
garage:
name="Vrata" column="0" inels="Vrata_Garaz" read_only="no" row="1"
on_off:
name="VZT ZAP/VYP" column="0" inels="VZT_Zapnout" read_only="no" row="0"
name="VZT ST 2" column="1" inels="VZT_rychlost_2" read_only="no" row="0"
name="VZT ST 3" column="2" inels="VZT_Rychlost_3" read_only="no" row="0"
"""

TEST_RAW_AIRING = """airing:
name="Equipment_room" column="0" inels="RE12_VT_equipment_room" \
read_only="no" row="1"
name="Pivnica 1" column="3" inels="RE10_VT_pivnica" read_only="no" row="1"
"""

TEST_RAW_METER = """meter:
name="Humidity cellar" inels="Humidity_cellar" min_disp="0" column="1" \
koef_mult="1.0" max_disp="100" decimal_digits="1" koef_add="0.0" \
units="%" row="1"
name="Teplota pivnica" inels="Therm_pivnica" min_disp="0" column="2" \
koef_mult="1.0" max_disp="100" decimal_digits="1" koef_add="0.0" \
units="stu" row="1"
"""

TEST_RAW_HC4 = """
hc4:
name="Kupelna_spalna" read_only="no" \
control_in="Controller_Control-IN_015AFA" \
required_therm_aout="Controller_Required-Therm-AOUT_015AFA" \
column="1" \
manual_cool_therm_ain="Controller_Manual-Cool-Therm-AIN_015AFA" \
status_dout="Controller_Status-DOUT_015AFA" \
manual_therm_ain="Controller_Manual-Therm-AIN_015AFA" \
actual_therm_aout="Controller_Actual-Therm-AOUT_015AFA" \
control_type_aout="Controller_Control-Type-AOUT_015AFA" \
required_heat_dout="Controller_Required-Heat-DOUT_015AFA" \
controller="kup_spal" \
control_manual_in="Controller_Control-Manual-IN_015AFA" \
control_hc_in="Controller_Control-HC-IN_015AFA" \
mode_dout="Controller_Mode-DOUT_015AFA" \
rele_c="Chod2" \
required_cool_therm_aout="Controller_Required-Cool-Therm-AOUT_015AFA" \
required_cool_dout="Controller_Required-Cool-DOUT_015AFA" \
rele_h="RE2_kur_kupelna_spalna" \
control_plan_in="Controller_Control-Plan-IN_015AFA" \
row="1"
"""

TEST_ROOMS = ['Basement', 'First floor', 'Front yard',
              'Back yard', 'Attic', 'Garrage']

TEST_VERSION = "CU3"
