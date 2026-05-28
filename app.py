# connects backend to frontend
from flask import Flask, render_template

app = Flask(__name__)

# input dictionary data here


# insert logic here


# routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/search")
def search():
    return render_template("search.html")


# submit new report
@app.route("/submit-report", methods=["POST"])
def submit_report():
    pass
    # new data
    # create pet/loc/time if not existing in dictionary


# search pet
@app.route("/search-pet", methods=["POST"])
def search_pet():
    data = request.json
    pet = data['pet']
    results = compute(pet)
    return jsonify(results)     

# run app
if __name__ == "__main__":
    app.run(debug=True)