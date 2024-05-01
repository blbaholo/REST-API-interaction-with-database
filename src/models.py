from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()


class HardDriveType(str, Enum):
    SSD = "SSD"
    HDD = "HDD"


class FormFactor(str, Enum):
    MINI = "Mini-ITX"
    MICRO = "Micro-ATX"
    ATX = "ATX"
    EATX = "E-ATX"


class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hard_drive_type = db.Column(
        db.Enum(
            HardDriveType,
            values_callable=lambda HardDriveType: [
                hard_drive_type.value for hard_drive_type in HardDriveType
            ],
        )
    )
    processor = db.Column(db.String(50), nullable=False)
    maximum_ram = db.Column(db.Integer, nullable=False)
    ram_amount = db.Column(db.Integer, nullable=False)
    hard_drive_space = db.Column(db.Integer, nullable=False)
    form_factor = db.Column(
        db.Enum(
            FormFactor,
            values_callable=lambda FormFactor: [
                form_factor_type.value for form_factor_type in FormFactor
            ],
        )
    )

    def __init__(
        self,
        hard_drive_type,
        processor,
        ram_amount,
        maximum_ram,
        hard_drive_space,
        form_factor,
    ):
        self.hard_drive_type = hard_drive_type
        self.processor = processor
        self.ram_amount = ram_amount
        self.maximum_ram = maximum_ram
        self.hard_drive_space = hard_drive_space
        self.form_factor = form_factor

    def to_dict(self):
        return {
            "id": self.id,
            "hard_drive_type": self.hard_drive_type,
            "processor": self.processor,
            "ram_amount": self.ram_amount,
            "maximum_ram": self.maximum_ram,
            "hard_drive_space": self.hard_drive_space,
            "form_factor": self.form_factor,
        }

    def __repr__(self):
        return f"{{Hard drive type: {self.hard_drive_type}, Processor: {self.processor}, Amount of Ram: {self.ram_amount}, Maximum Ram: {self.maximum_ram}, Hard drive space: {self.hard_drive_space}, Form-factor: {self.form_factor}}}"