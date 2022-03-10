from django.shortcuts import render
from django.http import response
from django.test import SimpleTestCase

class HomePageTests(SimpleTestCase):
    def test_admin_page_status_code(self):
        print("Verify admin Page")
        response=self.client.get('/admin')
        self.assertEquals(response.status_code,301)

    def test_about_page_status_code(self):
        print("Verify not exit about Page")
        response = self.client.get('/about')
        self.assertEquals(response.status_code, 404)
# Create your views here.
