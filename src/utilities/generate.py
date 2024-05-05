import json
import random
import string
import os
import xml.dom.minidom
import xml.etree.ElementTree as ET
import datetime

import src.utilities.config as cfg
from src.utilities.crypto import encrypt
from src.utilities.file import check_and_create_files, parse_json_file, add_elements_to_response


def generate_ticket():
    length = 10
    characters = string.ascii_letters + string.digits  # Символы: буквы и цифры
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def generate_config_xml_str():
    # Путь к файлу config.json
    config_file_path = os.path.join("assets", "preferences", "config.json")

    # Проверяем существование файла config.json
    if not os.path.exists(config_file_path):
        # Создаем config.json со значениями по умолчанию
        default_config_data = [
            {"Id": "1", "Parameter": "AccessRoleFlags", "Value": "0", "Type": "number"},
            {"Id": "3", "Parameter": "IsPreloaderFast", "Value": "0", "Type": "bool"},
            {"Id": "4", "Parameter": "InitialVolumeValue", "Value": "0", "Type": "number"},
            {"Id": "6", "Parameter": "IsPreloaderEnabled", "Value": "1", "Type": "bool"},
            {"Id": "7", "Parameter": "IsStartupHomeLocation", "Value": "0", "Type": "bool"},
            {"Id": "8", "Parameter": "SwfVersion", "Value": "", "Type": "string"},
            {"Id": "9", "Parameter": "SynchronizeAvatarRotation", "Value": "1", "Type": "bool"},
            {"Id": "10", "Parameter": "StatisticsSendInterval", "Value": "0", "Type": "number"},
            {"Id": "12", "Parameter": "LanguageId", "Value": "1", "Type": "number"},
            {"Id": "13", "Parameter": "SnId", "Value": "1", "Type": "number"},
            {"Id": "14", "Parameter": "IsInternational", "Value": "0", "Type": "bool"},
            {"Id": "15", "Parameter": "AutoServerSelectionAllowed", "Value": "1", "Type": "bool"},
            {"Id": "16", "Parameter": "DaysToFullSoil", "Value": "28", "Type": "number"},
            {"Id": "17", "Parameter": "DaysToHalfSoil", "Value": "14", "Type": "number"},
            {"Id": "18", "Parameter": "CurrentQuest", "Value": "467", "Type": "number"},
            {"Id": "20", "Parameter": "TypeWeapon", "Value": "0", "Type": "number"},
            {"Id": "21", "Parameter": "SkipTutorial", "Value": "1", "Type": "bool"},
            {"Id": "23", "Parameter": "CurrentQuestGroup", "Value": "1000", "Type": "string"},
            {"Id": "24", "Parameter": "IsNewRegistration", "Value": "1", "Type": "bool"},
            {"Id": "25", "Parameter": "IsMotivatingAdsOn", "Value": "1", "Type": "bool"},
            {"Id": "26", "Parameter": "VersionMode", "Value": "2", "Type": "number"}
        ]
        with open(config_file_path, "w") as json_file:
            json.dump(default_config_data, json_file, indent=4)

    # Загрузим данные из файла config.json
    with open(config_file_path, "r") as json_file:
        config_data = json.load(json_file)

    # Создаем элемент config
    config = ET.Element("config")

    # Пройдемся по каждому элементу в config_data и добавим его в XML
    for item in config_data:
        element = ET.SubElement(config, "item")
        for key, value in item.items():
            element.set(key, value)

    # Преобразуем config в строку
    cfg_str = ET.tostring(config, encoding="utf-8", method="xml").decode("utf-8")

    return cfg_str


def generate_servers_xml_str():
    # Путь к файлу servers.json
    servers_file_path = os.path.join("assets", "preferences", "servers.json")

    # Проверяем существование файла servers.json
    if not os.path.exists(servers_file_path):
        # Создаем servers.json со значениями по умолчанию
        default_servers_data = [{
            "Id": "1",
            "TRId": "1",
            "RId": "5",
            "RTMPUrl": f"rtmp://{cfg.instancehost}:{cfg.instanceport}/{cfg.instancename}",
            "Load": "0",
            "QuestLocationLoad": "0",
            "FriendsCount": "1",
            "ClubsCount": "5",
            "Weight": "0"
        }]
        with open(servers_file_path, "w") as json_file:
            json.dump(default_servers_data, json_file, indent=4)

        # Загружаем данные из только что созданного файла servers.json
        servers_data = default_servers_data
    else:
        # Загружаем данные из существующего файла servers.json
        with open(servers_file_path, "r") as json_file:
            servers_data = json.load(json_file)

    # Создаем элемент servers_list
    servers_list = ET.Element("servers")

    # Пройдемся по каждому серверу в servers_data и добавим его в XML
    for server in servers_data:
        server_element = ET.SubElement(servers_list, "item", server)

    # Преобразуем servers_list в строку
    slist_str = ET.tostring(servers_list, encoding="utf-8", method="xml").decode("utf-8")

    return slist_str


def generate_user_xml_str(userId, ticket, roleflags, isbanned):
    # Создаем элемент user_data
    user_data = ET.Element("user", {
        "UserId": str(userId),
        "hwId": str(ticket),
        "ticketId": str(ticket),
        "RoleFlags": str(roleflags)
    })

    # Добавляем атрибуты BanDateExpired и BanTextResourceID, если пользователь забанен
    if isbanned:
        user_data.set("BanDateExpired", "31-12-9999 23:59:59")
        user_data.set("BanTextResourceID", "162")

    # Преобразуем user_data в строку
    ud_str = ET.tostring(user_data, encoding="utf-8", method="xml").decode("utf-8")

    return ud_str


def generate_system_xml_str():
    # Путь к файлу system.json
    system_file_path = os.path.join("assets", "preferences", "system.json")

    # Проверяем существование файла system.json
    if not os.path.exists(system_file_path):
        # Создаем system.json со значениями по умолчанию
        default_system_data = {
            "RPath": "fs/3p897j5lf4e0j.swf",
            "RVersion": "49"
        }
        with open(system_file_path, "w") as json_file:
            json.dump(default_system_data, json_file, indent=4)
    # Загружаем данные из файла system.json
    with open(system_file_path, "r") as json_file:
        system_data = json.load(json_file)

    # Извлекаем значения rpath и rversion из system_data
    rpath = system_data.get("RPath", "fs/3p897j5lf4e0j.swf")
    rversion = system_data.get("RVersion", "49")

    # Создаем элемент system
    system = ET.Element("system", {
        "ServerDate": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "RPath": rpath,
        "RVersion": rversion
    })

    # Преобразуем system в строку
    sys_str = ET.tostring(system, encoding="utf-8", method="xml").decode("utf-8")

    return sys_str


def generate_server_action_xml_str(NotAuthenticated: bool, userId=None, ticket=None, roleFlags=None, isbanned=None, username=None):
    if NotAuthenticated:
        return None # в бесплатной версии fastdale нет поддержки нативной авторизации

    response = ET.Element("response", {"NotAuthenticated": str(NotAuthenticated).lower()})

    check_and_create_files()

    promotions = parse_json_file("assets/preferences/promotion/promotions.json")
    whats_new = parse_json_file("assets/preferences/promotion/whats_new.json")
    banners = parse_json_file("assets/preferences/promotion/banners.json")
    licence = parse_json_file("assets/preferences/promotion/licence.json")
    preloaders = parse_json_file("assets/preferences/promotion/preloaders.json")

    add_elements_to_response(response, "promotion", promotions)
    add_elements_to_response(response, "promotion_banner", banners)
    add_elements_to_response(response, "promotion_whats_new", whats_new)
    add_elements_to_response(response, "licence_promotion", licence)
    add_elements_to_response(response, "preloader", preloaders)

    response.extend([
        ET.Element("sn_status", {"IsBinded": "1"}),
        ET.Element("phone"),
        ET.Element("user_name", {"Value": str(username)}),
        ET.Element("postcard"),
        ET.Element("flags", {"EntranceCount": "2600", "IsUserDetailsMissing": "1"}),
        ET.Element("tutorial"),
        ET.Element("miniquest"),
        ET.Element("grants", {"ReceivingCount": "0"}),
        ET.Element("requests", {"ReceivingCount": "0"})
    ])

    tutorial_element = response.find("tutorial")
    for i in range(1, 6):
        ET.SubElement(tutorial_element, "item", {"Id": str(i), "State": "1"})

    cfg_str = generate_config_xml_str()
    slist_str = generate_servers_xml_str()
    ud_str = generate_user_xml_str(userId, ticket, roleFlags, isbanned)
    sys_str = generate_system_xml_str()

    response.extend([
        ET.Element("cdata", {"value": str(encrypt(cfg_str, "_level0"))}),
        ET.Element("cdata", {"value": str(encrypt(sys_str, "_level0"))}),
        ET.Element("cdata", {"value": str(encrypt(ud_str, "_level0"))}),
        ET.Element("cdata", {"value": str(encrypt(slist_str, "_level0"))})
    ])

    xml_str = ET.tostring(response, encoding="utf-8", xml_declaration=True)

    dom = xml.dom.minidom.parseString(xml_str.decode("utf-8"))
    pretty_xml_str = dom.toprettyxml(encoding="utf-8").decode("utf-8")

    return pretty_xml_str

