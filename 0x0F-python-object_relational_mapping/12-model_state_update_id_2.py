#!/usr/bin/python3
"""
a script that changes the name
of a State object from the database hbtn_0e_6_usa
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

    state = session.query(State).filter(State.id == 2).first()

    state.name = "New Mexico"

    session.commit()
