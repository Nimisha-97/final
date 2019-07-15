from flaskblog import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_homepage(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Welcome to Kinetic Labs' in response.data)
        self.assertTrue(b'New messages every time you refresh' in response.data)

    def test_aboutpage(self):
        tester = app.test_client(self)
        response = tester.get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertTrue((b'About Page' in response.data))

    def test_formpage(self):
        tester = app.test_client(self)
        response = tester.get("/form")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
