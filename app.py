# connects backend to frontend

from flask import Flask, render_template, request, jsonify
from backend.database import PETS_DB
from backend.search import get_ranked_results

app = Flask(__name__)

TIME_SLOTS = [
    "01:00 AM - 03:59 AM",
    "04:00 AM - 06:59 AM",
    "07:00 AM - 09:59 AM",
    "10:00 AM - 12:59 PM",
    "01:00 PM - 03:59 PM",
    "04:00 PM - 06:59 PM",
    "07:00 PM - 09:59 PM",
    "10:00 PM - 12:59 AM"
]

PET_IMAGES = {
        "ampon":        "images/dogs/ampon.png",
        "bella":        "images/dogs/bella.png",
        "betty":        "images/dogs/betty.png",
        "blanca":       "images/dogs/blanca.png",
        "blanch":       "images/dogs/blanch.png",
        "blythe":       "images/dogs/blythe.png",
        "brownie":      "images/dogs/brownie.png",
        "butterscotch": "images/dogs/butterscotch.png",
        "carrot_cake":  "images/dogs/carrotcake.png",
        "cm":           "images/dogs/cm.png",
        "ducky":        "images/dogs/ducky.png",
        "jewel":        "images/dogs/jewel.png",
        "lassie":       "images/dogs/lassie.png",
        "saki":         "images/dogs/saki.png",
        "maan":         "images/dogs/maan.png",
        "mathilda":     "images/dogs/mathilda.png",
        "milo":         "images/dogs/milo.png",
        "mimi":         "images/dogs/mimi.png",
        "molly":        "images/dogs/molly.png",
        "odette":       "images/dogs/odette.png",
        "paquito":      "images/dogs/paquito.png",
        "patchy":       "images/dogs/patchy.png",
        "potpot":       "images/dogs/potpot.png",
        "puppy":        "images/dogs/puppy.png",
        "scar2":        "images/dogs/scar2.png",
        "shane":        "",
        "shiela":       "images/dogs/shiela.png",
        "spot":         "images/dogs/spot.png",
        "brwylee":      "images/dogs/brwylee.png",
        "coli":         "images/cats/coli.png",
        "goldie":       "images/cats/goldie.png",
        "katyperry":    "images/cats/katyperry.png",
        "maomao":       "images/cats/maomao.png",
        "meric":        "images/cats/meric.png",
        "motherlitob":  "images/cats/motherlitob.png",
        "nella":        "images/cats/nella.png",
        "tanjiro":      "images/cats/tanjiro.png",
        "tiger":        "images/cats/tiger.png",
        "badbad":       "images/cats/badbad.png",
        "midnight":     "images/cats/midnight.png",
        "albie":        "images/cats/albie.png",
        "peachy":       "images/cats/peachy.png",
        "muzan":        "images/cats/muzan.png",
        "patches":      "images/cats/patches.png",
        "trisha":       "images/cats/trisha.png",
        "mikay":        "images/cats/mikay.png",
    }

LOCATIONS = [

    "SOTECH",
    "CAS",
    "CM",
    "CFOS Park-Pidlaoan Hall-Umali Hall",
    "CFOS OWL-Wet Lab",
    "CFOS Hatchery",
    "CUB/Mushroom",
    "RRC/New Library",
    "Old Admin",
    "New Admin/Box 1",
    "Dorm/CDH",
    "Box 2-Physical Plant Office-CDMO",
    "Staff House",
    "SSF-HSU-Executive House",
    "Teacher's Dorm",
    "Covered Court/Lover's Lane"
]


# insert logic here


# routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    pets_data = []
    
    for pet_id, pet_data in PETS_DB.items():
        pets_data.append({
            "id": pet_id, 
            "name": pet_id.title(),
            "photo": PET_IMAGES.get(pet_id.lower(), "images/default-placeholder.png")
        })
    return render_template("report.html", pets=pets_data, locations=LOCATIONS, times=TIME_SLOTS)

@app.route("/search")
def search():
    pet_list = sorted(PETS_DB.keys())
    return render_template("search.html", pets=pet_list, times=TIME_SLOTS, images=PET_IMAGES)

# submit new report
@app.route("/submit-report", methods=["POST"])
def submit_report():
    data = request.get_json()
    pet = data.get("pet", "").lower()
    location = data.get("location")
    time = data.get("time")

    print(f"DEBUG: Received pet={pet}, time={time}, location={location}")

    if pet not in PETS_DB:
        return jsonify({"message": "Pet not found"}), 404

    if time not in PETS_DB[pet]:
        PETS_DB[pet][time] = {}
        
    current_count = PETS_DB[pet][time].get(location, 0)
    PETS_DB[pet][time][location] = current_count + 1

    return jsonify({"message": f"Successfully reported {pet.title()}!"})


def search_pet():
    data = request.json
    pet = data['pet'].lower()      
    time = data['time']

    pet_info = PETS_DB.get(pet, {})  
    results = get_ranked_results(pet_info, time)
    return jsonify(results)

@app.route("/check-db")
def check_db():
    # testing report
    return jsonify(PETS_DB)

# run app
if __name__ == "__main__":
    app.run(debug=True)