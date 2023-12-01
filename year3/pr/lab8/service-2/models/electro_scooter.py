from models.database import db

class ElectroScooter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    battery_level = db.Column(db.Float, nullable=False)

    def __init__(self, name, battery_level):
        self.name = name
        self.battery_level = battery_level

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'battery_level': self.battery_level
        }