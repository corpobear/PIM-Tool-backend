from app.tests.base import BaseTestCase



class TestBaseUrl(BaseTestCase):
    
    
    def test_base_access(self):
        
        response = self.client.get('/test')
        self.assertEqual(response.status_code, 200)
