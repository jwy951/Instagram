from django.test import TestCase
from .models import Profile, Image
from django.contrib.auth.models import User


class ProfileTestClass(TestCase):
    from django.contrib.auth.models import User
    def setUp(self):
        self.user = User(username='martin')
        self.user.save()
        self.profile_test = Profile(id=1,user=self.user,photo='download.jpeg',bio='My name is Martin', name='person')

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_method(self):
        self.profile_test.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.profile_test = Profile(user=User(username='martin'))
        self.profile_test.user.save()
        self.profile_test.save()
        self.image_test = Image(user=self.profile_test,image='download.jpeg', name='person', caption='this is it')

    def test_insatance(self):
        self.assertTrue(isinstance(self.profile_test,Profile))
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)