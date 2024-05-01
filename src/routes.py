from src.models import db, Computer
from flask import request, Blueprint
import json

app_blueprint = Blueprint("routes", __name__)


@app_blueprint.route("/computers", methods=["GET"])
def list_computers():
    data = [computer.to_dict() for computer in Computer.query.all()]
    return json.dumps(data, indent=4)

@app_blueprint.route("/computers/", methods=["POST"])
def add_computer():
    data = request.get_json()
    computer = Computer(
        hard_drive_type=data["hard_drive_type"],
        processor=data["processor"],
        ram_amount=data["ram_amount"],
        maximum_ram=data["maximum_ram"],
        hard_drive_space=data["hard_drive_space"],
        form_factor=data["form_factor"],
    )
    db.session.add(computer)
    db.session.commit()
    return "MESSAGE: Computer details successfully added"


@app_blueprint.route("/computers/<id>", methods=["PATCH"])
def update_computer(id):
    data = request.get_json()
    computer = Computer.query.filter_by(id=id).first_or_404()
    if "hard_drive_type" in data:
        computer.hard_drive_type = data["hard_drive_type"]
    if "processor" in data:
        computer.processor = data["processor"]
    if "ram_amount" in data:
        computer.ram_amount = data["ram_amount"]
    if "maximum_ram" in data:
        computer.maximum_ram = data["maximum_ram"]
    if "hard_drive_space" in data:
        computer.hard_drive_space = data["hard_drive_space"]
    if "form_factor" in data:
        computer.form_factor = data["form_factor"]
    db.session.commit()
    return json.dumps(computer.to_dict(), indent=4)


@app_blueprint.route("/computers/<id>", methods=["DELETE"])
def delete_computer(id):
    computer = Computer.query.filter_by(id=id).first_or_404()
    db.session.delete(computer)
    db.session.commit()
    return "MESSAGE: Computer entry successfully deleted"
