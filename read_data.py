import json

# Opening JSON file
def load_person_data():
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data