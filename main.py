import csv
import requests

from flask import Flask, abort, request
from faker import Faker


app = Flask(__name__)
fake = Faker()


@app.route("/requirements", methods=["GET"])
def return_requirements():
    try:
        with open("./requirements.txt", "r") as file:
            return file.readlines()
    except IOError:
        abort(404)


@app.route("/generate-users", methods=["GET"])
def generate_users():
    count = 0
    try:
        count = int(request.args.get("count"))
    except TypeError:
        abort(400)
    if not count or count < 0:
        abort(412)
    res = []
    for _ in range(count):
        res.append({"email": fake.email(), "name": fake.first_name()})
    return res


@app.route("/mean", methods=["GET"])
def get_average_h_w():
    dict_response = {"avg_h": 0, "avg_w": 0}
    with open("./hw.csv", newline="") as csvfile:
        rows = list(csv.reader(csvfile, delimiter=",", quotechar="|"))[1:-1]
        h_sum = 0
        w_sum = 0
        for row in rows:
            h_sum += float(row[1])
            w_sum += float(row[2])

        dict_response["avg_h"] = h_sum * 2.54 / len(rows)
        dict_response["avg_w"] = w_sum * 0.453592 / len(rows)
    return dict_response


@app.route("/space", methods=["GET"])
def get_num_astronauts():
    r = requests.get("http://api.open-notify.org/astros.json")
    res = r.json()
    print(res)
    return {"count": res["number"]}


if __name__ == "__main__":
    app.run()
