from fastapi import Request
from src.utilities.const import Const as cst
def is_local_network(request: Request):
    # Получаем IP-адрес медиа-сервера
    client_ip = request.client.host
    # Проверяем, является ли IP-адрес локальным
    if client_ip in ("127.0.0.1", "localhost"):
        return True
    return False

import requests

def check_for_updates(current_version):
    api_url = f"https://api.github.com/repos/{cst.REPO_OWNER}/{cst.REPO_NAME}/releases/latest"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            latest_release = response.json()
            latest_release_tag = latest_release.get("tag_name")

            if latest_release_tag and is_newer_version(latest_release_tag, current_version):
                return f"https://github.com/{cst.REPO_OWNER}/{cst.REPO_NAME}/releases/tag/{latest_release_tag}"
        else:
            print(f"Ошибка HTTP: {response.status_code}")
    except requests.RequestException as e:
        print(f"Ошибка в запросе: {e}")

    return None

def is_newer_version(latest_version, current_version):
    latest_parts = list(map(int, latest_version.split(".")))
    current_parts = list(map(int, current_version.split(".")))

    for latest, current in zip(latest_parts, current_parts):
        if latest > current:
            return True
        elif latest < current:
            return False

    return False  # Versions are equal
