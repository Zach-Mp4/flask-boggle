from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

# python -m unittest test.py
class FlaskTests(TestCase):
    # TODO -- write tests for every view function / feature!
    def test_main_page(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<div class="grid-container">', html)
    
    def test_guess(self):
        with app.test_client() as client:
            res = client.post('/guess', json={'g': 'zsdeds'})
            response_data = res.get_json()


            self.assertEqual(res.status_code, 200)
            self.assertEqual(response_data['result'], 'not-a-word')

    def test_scores(self):
         with app.test_client() as client:
             res = client.post('/scores', json={'score': 56})
             response_data = res.get_json()

             self.assertEqual(res.status_code, 200)
             self.assertEqual(response_data['highscore'], 56)
             self.assertEqual(response_data['timesplayed'], 1)

             res = client.get('/highscore')
             response_data = res.get_json()
             self.assertEqual(response_data['highscore'], 56)






