#!/usr/bin/python3
"""change the state name of a state from
hbtn_0e_6_usa database"""
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
    newstate = session.query(State).filter(State.id == 2).first()
    newstate.name = 'New Mexico'
    session.commit()
    session.close()
