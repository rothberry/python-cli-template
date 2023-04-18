from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace

# from models import (AllModels)
# from helpers import (*)

engine = create_engine('sqlite:///app/grocery_stores.db')
session = sessionmaker(bind=engine)()


if __name__ == '__main__':
  # Intro: welcome to the CLI, pick a store
  print("WELCOME TO YOUR CLI PROJECT!!!!")
