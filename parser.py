import requests
import json

BASE_URL = "https://158.160.225.48:33723/9yorpgBPnJiUH9Zndd"   
USERNAME = "follozy"
PASSWORD = "1470gghh"

session = requests.Session()

# 1. Логин
login_resp = session.post(
    f"{BASE_URL}/login",
    data={
        "username": USERNAME,
        "password": PASSWORD
    },
    timeout=15,
    verify=False
)
login_resp.raise_for_status()
def take_setings ():
    # 2. Получаем список инбаундов
    resp = session.get(f"{BASE_URL}/panel/api/inbounds/list", timeout=15, verify=False)
    resp.raise_for_status()

    data = resp.json()

    # Обычно список лежит в obj
    inbounds = data.get("obj", [])

    for inbound in inbounds:
        print("ID:", inbound.get("id"))
        print("Remark:", inbound.get("remark"))
        print("Protocol:", inbound.get("protocol"))
        print("Port:", inbound.get("port"))

        # settings обычно хранится строкой JSON
        raw_settings = inbound.get("settings", "{}")
        try:
            settings = json.loads(raw_settings)
        except json.JSONDecodeError:
            settings = {}

        raw_stream_settings = inbound.get("streamSettings", "{}")
        try:
            stream_settings = json.loads(raw_stream_settings)
        except json.JSONDecodeError:
            stream_settings = {}
        
        print("Settings:", settings)
        print("-" * 50)
        return stream_settings