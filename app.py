'''
- connects backend to frontend
- reads and handles the data and logic 
- sends data to HTML via render_template
'''

from flask import Flask, render_template, request, jsonify
from backend.database import PETS_DB
from backend.search import get_ranked_results

app = Flask(__name__)

'''
# accesing data from json files
with open("data/pets.json") as f:
    pets = json.load(f)

with open("data/location.json") as f:
    locations = json.load(f)
'''

with open("data/time.json") as f:
    times = json.load(f)

# input dictionary data here
reports = {
  "Cassie": {
    "7AM-9:59AM": {
      "Library": 3,
      "Canteen": 1
    },
    "10AM-12:59PM": {
      "Library": 2
    }
  }
}

# insert logic here


# routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    pet_list = sorted([pet.title() for pet in PETS_DB.keys()])
    return render_template("report.html", pets=pet_list)
  # return render_template("report.html", pets=pets, locations=locations, times=times)

@app.route("/search")
def search():
    pet_list = sorted(PETS_DB.keys())
        
    time_slots = [
        "07:00 AM - 09:59 AM",
        "10:00 AM - 12:59 PM",
        "01:00 PM - 03:59 PM",
        "04:00 PM - 06:59 PM",
        "07:00 PM - 09:59 PM",
        "10:00 PM - 12:59 AM",
        "01:00 AM - 03:59 AM"
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
    return render_template("search.html", pets=pet_list, times=time_slots, images=PET_IMAGES)

# submit new report
@app.route("/submit-report", methods=["POST"])
def submit_report():
    data = request.json

    pet = data["pet"]
    time = data["time"]
    location = data["location"]

    reports.setdefault(pet, {})
    reports[pet].setdefault(time, {})
    reports[pet][time].setdefault(location, 0)
    reports[pet][time][location] += 1

    return {"message": "Report saved"}

@app.route("/search-pet", methods=["POST"])
def search_pet():
    data = request.json
    pet = data['pet'].lower()      
    time = data['time']

    pet_info = PETS_DB.get(pet, {})  
    results = get_ranked_results(pet_info, time)
    return jsonify(results)
# run app
if __name__ == "__main__":
    app.run(debug=True)