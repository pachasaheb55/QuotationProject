from django.test import TestCase

# Create your tests here.

class URLTests(TestCase):
    """ Unit test cases for URl's"""

    def test_home_page_url(self):
        """ Test case for """
        response = self.client.get('/quote/')
        self.assertEqual(response.status_code, 200)

    def test_create_quote_url(self):
        response = self.client.get('/quote/createQuote/')
        self.assertEqual(response.status_code, 200)

    def test_customer_url(self):
        response = self.client.get('/quote/customer/')
        self.assertEqual(response.status_code, 200)

    def test_admin_url(self):
        response = self.client.get('/quote/customer/')
        self.assertEqual(response.status_code, 200)


class CreateQuoteViewTests(TestCase):
    """ Test case for CreateQuoteView"""

    def test_create_quote_get(self):
        response = self.client.get('/quote/createQuote/')
        self.assertEqual(response['content-type'], 'text/html; charset=utf-8')
        self.assertIsInstance(response.context['forms'], zip)

    def test_create_quote_post(self):
        input_data = { 'name': ['Pacha Saheb'], 'email': ['pachasaheb55@gmail.com'], 'mobile_number': ['9196525448'], 'year': ['2021'], 'model': ['Audi Q3'], 'make': ['audi'], 'number': ['qf1222'], 'price': 
            ['100000.0'], 'the_coverages': ['1', '2'], 'quote': ['GET QUOTE']}
        response = self.client.post('/quote/createQuote/', input_data)

# TODO the test cases
