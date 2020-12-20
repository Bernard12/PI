from django.test import TestCase, Client
from django.contrib.auth import get_user_model, authenticate
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        UserModel = get_user_model()
        UserModel.objects.create_user('test1', 'test@test.com', 'secret')

    def test_should_redirect_if_not_auth(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/home/')

    def test_should_use_correct_template(self):
        self.client.login(username='test1', password='secret')
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class HomeViewTestsSelenium(StaticLiveServerTestCase):
    def setUp(self):
        self.client = Client()

        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)

        UserModel = get_user_model()
        self.user = UserModel.objects.create_user('test1', 'test@test.com', 'secret')

    def tearDown(self):
        self.driver.close()

    def url(self, path):
        return f'{self.live_server_url}{path}'

    def login(self):
        self.client.login(username='test1', password='secret')
        cookie = self.client.cookies['sessionid']
        self.driver.get(self.url('/'))
        self.driver.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.driver.refresh()

    def test_authed_user_should_see_username(self):
        self.login()
        self.driver.get(self.url('/home'))

        greet = self.driver.find_element_by_id('greetings')
        self.assertEquals(greet.text, 'Hello test1!')
