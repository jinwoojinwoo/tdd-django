from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': '신규 작업 아이템'})
        self.assertIn('신규 작업 아이템', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
