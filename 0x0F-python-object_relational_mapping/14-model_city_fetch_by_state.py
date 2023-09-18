#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    conn = f"mysql+mysqldb://{user_name}:{passwd}@localhost:3306/{db_name}"

    engine = create_engine(conn, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    # citys = session.query(State.name, City.id, City.name).\
    #     join(City, City.state_id == State.id).order_by(City.id).all()

    # for state_name, city_id, city_name in citys:
    #     print(f"{state_name}: ({city_id}) {city_name}")

    citys = session.query(State, City).\
        filter(City.state_id == State.id).order_by(City.id).all()

    for state, city in citys:
        print(f"{state.name}: ({city.id}) {city.name}")
