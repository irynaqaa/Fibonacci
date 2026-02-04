from application.app import db

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    metadata = db.Column(db.JSON, nullable=False)
    last_communication = db.Column(db.DateTime, nullable=False)

class TimeSeriesData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float, nullable=False)
    device = db.relationship('Device', backref='data')
