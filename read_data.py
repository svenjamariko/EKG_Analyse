import json

# Opening JSON file
def load_person_data():
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data

def get_person_list(person_data):
    list_of_names = []

    for eintrag in person_data:
        list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
    return list_of_names


def find_person_data_by_name(suchstring):

    person_data = load_person_data()

    if suchstring == "None":
        return {}
    
    two_names = suchstring.split(", ")
    vorname = two_names[1]
    nachname = two_names[0]

    for eintrag in person_data:
        #print(eintrag)
        if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):
            return eintrag
    return {}




