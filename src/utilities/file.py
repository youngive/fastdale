import json
import os
import xml.etree.ElementTree as ET


def check_and_create_files():
    files = [
        "assets/preferences/promotion/promotions.json",
        "assets/preferences/promotion/banners.json",
        "assets/preferences/promotion/whats_new.json",
        "assets/preferences/promotion/licence.json",
        "assets/preferences/promotion/preloaders.json"
    ]

    for file_path in files:
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(file_path):
            create_default_json_file(file_path)

    # Возвращаемый список файлов
    return files


def create_default_json_file(file_path):
    default_data = {}

    # Define default data for specific files
    if "promotions.json" in file_path:
        default_data = [
            {"MRId": "20106", "State": "1"},
            {"MRId": "30896", "State": "7"}
        ]
    elif "banners.json" in file_path:
        default_data = [
            {"MRId": "30896"}
        ]
    elif "whats_new.json" in file_path:
        default_data = [
            {"Id": "386", "TypeId": "1", "MRId": "20143"},
            {"Id": "611", "TypeId": "2", "MRId": "27179"},
            {"Id": "784", "TypeId": "2", "MRId": "30841"},
            {"Id": "785", "TypeId": "2", "MRId": "30895"},
            {"Id": "786", "TypeId": "2", "MRId": "30897"}
        ]
    elif "licence.json" in file_path:
        default_data = [
            {"Id": "1", "GroupId": "0", "OrderId": "0", "MRId": "14763"},
            {"Id": "2", "GroupId": "0", "OrderId": "1", "MRId": "14764"},
            {"Id": "3", "GroupId": "0", "OrderId": "2", "MRId": "14765"},
            {"Id": "4", "GroupId": "1", "OrderId": "0", "MRId": "14766"},
            {"Id": "5", "GroupId": "1", "OrderId": "1", "MRId": "14767"},
            {"Id": "6", "GroupId": "1", "OrderId": "2", "MRId": "14768"},
            {"Id": "7", "GroupId": "2", "OrderId": "0", "MRId": "20597"},
            {"Id": "8", "GroupId": "2", "OrderId": "1", "MRId": "20598"},
            {"Id": "9", "GroupId": "2", "OrderId": "2", "MRId": "20599"}
        ]
    elif "preloaders.json" in file_path:
        default_data = [
            {"MRId": "30894", "ShowTime": "20;00"}
        ]

    # Write default data to the file
    with open(file_path, "w") as json_file:
        json.dump(default_data, json_file, indent=4)


def parse_json_file(file_path):
    # Check if the file exists, if not, create it
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump({}, file)

    # Parse JSON file
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def add_elements_to_response(response, tag_name, elements):
    element = ET.Element(tag_name)
    for item in elements:
        sub_element = ET.SubElement(element, "i")
        for key, value in item.items():
            sub_element.set(key, str(value))
    response.append(element)
