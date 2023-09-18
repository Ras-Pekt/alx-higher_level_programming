#!/usr/bin/python3
"""
a script that lists all State objects,
and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    conn = f"mysql+mysqldb://{user_name}:{passwd}@localhost:3306/{db_name}"

    engine = create_engine(conn, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
