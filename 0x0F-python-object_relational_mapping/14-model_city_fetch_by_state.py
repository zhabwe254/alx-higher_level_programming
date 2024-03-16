#!/usr/bin/python3
"""Script to print all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Create an engine to interact with the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all City objects and print them with their State
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(session.query(State).get(city.state_id).name,
                                   city.id, city.name))

    # Close the session
    session.close()
