#!/usr/bin/python3
"""Script to delete all State objects with a name containing the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine to interact with the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the states
    for state in states_with_a:
        session.delete(state)

    # Commit the session to delete the states
    session.commit()

    # Close the session
    session.close()
