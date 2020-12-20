from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_render_correct_template(self):
        response = self.client.get('/login')
        self.assertTemplateUsed('login.html')


class LoginViewTestSelenium(StaticLiveServerTestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)

    def tearDown(self):
        self.driver.close()

    def url(self, path):
        return f'{self.live_server_url}{path}'

    def test_login_template_has_google_oauth(self):
        self.driver.get(self.url('/login'))
        google_login = self.driver.find_element_by_id('google-login')
        github_login = self.driver.find_element_by_id('github-login')

        self.assertEquals(google_login.text, 'GOOGLE LOGIN')
        self.assertEquals(github_login.text, 'GITHUB LOGIN')
