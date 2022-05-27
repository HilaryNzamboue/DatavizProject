from django.test import TestCase

from django.urls import reverse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate

# from .models import Student, Notes, Groupe, Matiere, MoyenneS1, MoyenneS2, FileModel, FilePV, Classe, Classe_Student, User


# Create your tests here.


class Url_test(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        
        test_user1 = User.objects.create_user(username = 'user1', email='mail@mail.com', password='1X<ISRUkw+tuK', first_name = 'TEST USER 1')
        test_user2 = User.objects.create_user(username = 'user2', email='email@email.com', password='2HJ1vRV0Z&3iD', first_name = 'TEST USER 2')

        test_user1.save()
        test_user2.save()
        # print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass
    
    def test_bilan_url(self):
    
        # response = self.client.get(reverse('form'))
        # self.assertEqual(response.status_code, 200)
        
        login = self.client.login(username = 'user1', password='1X<ISRUkw+tuK')
        response = self.client.get('/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        
        pass
    