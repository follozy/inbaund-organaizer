import requests
import json
from data_base import take_engine, Users
from sqlalchemy.orm import Session

BASE_URL = "https://158.160.225.48:33723/9yorpgBPnJiUH9Zndd"   
USERNAME = "follozy"
PASSWORD = "1470gghh"


def take_setings (Wdata:str = "client"):
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
    # 2. Получаем список инбаундов
    resp = session.get(f"{BASE_URL}/panel/api/inbounds/list", timeout=15, verify=False)
    resp.raise_for_status()

    data = resp.json()

    # Обычно список лежит в obj
    inbounds = data.get("obj", [])

    for inbound in inbounds:

        # settings обычно хранится строкой JSON
        if Wdata == "client":
            raw_settings = inbound.get("settings", "{}")
            try:
                settings = json.loads(raw_settings)
            except json.JSONDecodeError:
                settings = {}
            return settings
        elif Wdata == "server":
            raw_stream_settings = inbound.get("streamSettings", "{}")
            try:
                settings = json.loads(raw_stream_settings)
            except json.JSONDecodeError:
                settings = {}
            return settings
    


def set_users():
    setings = take_setings("client")
    
    engine = take_engine()
    with Session(engine) as session:
        clients = []
        for id, client in enumerate(setings["clients"]):
            #print(client["email"])
            

            client_tg = f'{client['email']}'.replace('[', ';').replace(']', ';').split(';')
            #print(client_tg)

            user = Users(
                tgid = client_tg[len(client_tg) - 2],
                uuid = client["id"],
                email = client_tg[0],
                enable = client["enable"],
                created = client["created_at"],
                lustupdate = client["updated_at"],
                flow = client["flow"],
                tarif = 'white'
                )
            clients.append(user)
        session.add_all(clients)
        session.commit()
