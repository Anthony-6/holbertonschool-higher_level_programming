#!/usr/bin/python3
"""print the first state from the
hbtn_0e_6_usa database"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    instance = session.query(State).order_by(State.id).first()
    if instance:
        print('{}: {}'.format(instance.id, instance.name))
    else:
        print('Nothing')
    session.close()
