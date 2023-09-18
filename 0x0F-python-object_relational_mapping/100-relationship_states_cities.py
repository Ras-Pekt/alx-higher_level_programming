#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
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

    state = session.query(State).filter(State.name == "California").first()

    if state is None:
        state = State(name="California")
        city = City(name="San Francisco", state=state)
        session.add(city)
        # session.flush()
        session.commit()
