from application import db
from application.models import Demo

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    demo1 = Demo(field1="Hello World")
    demo2 = Demo(field1="Sample Text")
    demo3 = Demo(field1="Lorem ipsum")

    db.session.add(demo1)
    db.session.add(demo2)
    db.session.add(demo3)
    db.session.commit()