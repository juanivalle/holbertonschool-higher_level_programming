#!/usr/bin/python3
""" task 7 """

if __name__ == '__main__':
    from model_state import Base, State
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session
    from sqlalchemy import select

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    mysql_db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_user, mysql_pass, mysql_db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
