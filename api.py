from data_base import engine, Servers, Users

from sqlalchemy import select
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
    