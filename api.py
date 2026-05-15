from data_base import engine, Servers, Users

from sqlalchemy import select, Inspector
from sqlalchemy.orm import Session

import json

def take_users():
    users = []
    with Session(engine) as session:
        stmt = select(Users)
        for user in session.scalars(stmt):
            userd = vars(user)
            userd.pop('_sa_instance_state', None)
            users.append(userd)
            #print(type(vars(user)))
        
    return json.loads(json.dumps(users))
    
    
def add_sever(raw_data:str):
    data = json.loads(raw_data)


    return{'b': 'заглушка'}

def take_fild(table:str):
    inspector = Inspector(engine)
    columns = inspector.get_columns(table)
    column_names = [col['name'] for col in columns]
    return column_names
