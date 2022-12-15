import os
import json
import crud
import model
import server
from model import connect_to_db, db

os.system("dropdb WB")
os.system("createdb WB")

model.connect_to_db(server.app)
model.db.create_all()
