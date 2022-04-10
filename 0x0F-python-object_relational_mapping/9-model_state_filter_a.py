#!/usr/bin/python3
"""list all state that contains the 'a' letter
from the hbtn_0e_6_usa database"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    for instance in session.query(State)\
        .filter(State.name.like('%a%'))\
            .order_by(State.id):
        print('{}: {}'.format(instance.id, instance.name))
    session.close()
