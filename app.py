'''
- connects backend to frontend
- reads and handles the data and logic 
- sends data to HTML via render_template
'''

import json
from flask import Flask, render_template

app = Flask(__name__)

# accesing data from json files
with open("data/pets.json") as f:
    pets = json.load(f)

with open("data/location.json") as f:
    locations = json.load(f)

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
    return render_template("report.html", pets=pets, locations=locations, times=times)

@app.route("/search")
def search():
    return render_template("search.html")


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

# search pet
@app.route("/search-pet", methods=["POST"])
def search_pet():
    data = request.json
    pet = data["pet"]
    time = data["time"]

    if pet not in reports or time not in reports[pet]:
        return []
    
    locations = reports[pet][time]      # returns { key-value pairs }

    # call helper func for logic
    # return json format of logic results (ranked list of tuples)

# run app
if __name__ == "__main__":
    app.run(debug=True)