#!/usr/bin/python3
"""
a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    conn = f"mysql+mysqldb://{user_name}:{passwd}@localhost:3306/{db_name}"

    engine = create_engine(conn, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)

    session.commit()

    print(new_state.id)
