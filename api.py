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

def take_user_by_id(id:list):
    with Session(engine) as session:
        stmt = select(Users).where(Users.id == id)
        user = vars(session.scalar(stmt))
        user.pop('_sa_instance_state', None)
        
    return user
        
    
    
def add_sever(data):

    print(data)
    out_data = {'status': 'bad'}
    with Session(engine) as session:
        server = Servers(
            IPv4 = data['IPv4'],
            port = int(data['port']),
            pubKey = data['pubKey'],
            mldsa65Verify = data['mldsa65Verify'],
            shortIDs = data['shortIDs'],
            uTLS = data['uTLS'],
            SNI = data['SNI'],
            Target = data['Target'],
            security = data['security'],
            fingerprint = data['fingerprint']
        )
        session.add(server)
        session.commit()
        out_data['id'] = server.id
        out_data['status'] = 'ok'
        

    return out_data

def take_fild(table:str):
    inspector = Inspector(engine)
    columns = inspector.get_columns(table)
    column_names = [col['name'] for col in columns]
    return column_names
