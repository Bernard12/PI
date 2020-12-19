from django.test import TestCase, Client
from django.contrib.auth import get_user_model 
from .views import UserProfile

# Create your tests here.
class UserProfileTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user('test1', 'test@test.com', 'secret')
        UserModel.objects.create_user('test2', 'test@test.com', 'secret')

        self.client = Client()

        self.userProfile = UserProfile.objects.create(
                name='test1'
        )
        self.userProfile.purchased_cards.set([])

    def test_should_redirect_without_auth(self):
        response = self.client.get('/api/v1/user')
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/api/v1/user')

    def test_should_show_user_info_if_has_auth(self):
        self.client.login(username='test1', password='secret')
        response = self.client.get('/api/v1/user')
        self.assertEquals(response.status_code, 200)

    def test_should_return_404_if_not_found(self):
        self.client.login(username='test2', password='secret')
        response = self.client.get('/api/v1/user')
        self.assertEquals(response.status_code, 404)
