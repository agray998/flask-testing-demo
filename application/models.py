from application import db

class Demo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    field1 = db.Column(db.String(50))
    def __str__(self):
        return f"id: {self.id}\tmessage: {self.field1}"