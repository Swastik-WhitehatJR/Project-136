import pandas as pd 
import csv
from data import data
from flask import Flask, jsonify, request

rows = []

with open("stars.csv","r") as f:
  csvreader = csv.reader(f)
  
  for row in csvreader:
    rows.append(row)

headers = rows[0]
stars_data = rows[1:]

final_star_list = []

for star_data in stars_data:
  temp_dict = {
    "name": star_data[2],
    "distance_from_host_star": star_data[3],
    "star_mass": star_data[4],
    "star_radius": star_data[5],
    "star_gravity": star_data[6]
  }

  final_star_list.append(temp_dict)



app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
    }), 200

@app.route("/star")
def star():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "Name of star": star_data["name"],
        "Distance from host star": star_data["distance_from_host_star"],
        "Gravity of star": star_data["star_gravity"],
        "Mass of star": star_data["star_mass"],
        "Radius of star": star_data["star_radius"],
    }), 200

if __name__ == "__main__":
    app.run()



