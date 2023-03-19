#!/usr/bin/python3
"""task 8 print first state"""
if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy import select

    mysql_username, mysql_password, database_name = argv[1], argv[2], argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = select(State).order_by(State.id)
        exe = session.execute(query).first()
        if exe is not None:
            print("{}: {}".format(exe[0].id, exe[0].name))
        else:
            print("Nothing")

