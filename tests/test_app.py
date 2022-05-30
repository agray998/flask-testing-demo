from application import app, db
from flask import url_for
from flask_testing import TestCase
from application.models import Demo

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            SECRET_KEY = 'test secret key',
            WTF_CSRF_ENABLED = False
        )
        return app
    
    def setUp(self):
        demo1 = Demo(field1="This is sample data")
        demo2 = Demo(field1="This is more sample data")
        db.create_all()
        db.session.add(demo1)
        db.session.add(demo2)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViewHome(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)
        self.assertIn(b'sample data', response.data)

class TestViewAdd(TestBase):
    def test_get_add(self):
        response = self.client.get(url_for('add'))
        self.assert200(response)
        self.assertIn(b'Add Item:', response.data)

class TestAddItem(TestBase):
    def test_post_add(self):
        response = self.client.post(url_for('add'),
        data = dict(add="This has been added in a test"),
        follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'added in a test', response.data)