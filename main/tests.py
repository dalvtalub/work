from django.test import TestCase
# from django.utils import timezone
#
# from .models import Question
#
#
# class QuestionModelTests(TestCase):
#
#     def test_was_published_recently_with_future_question(self):
#         """
#         was_published_recently() returns False for questions whose pub_date
#         is in the future.
#         """
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_question = Question(pub_date=time)
#         self.assertIs(future_question.was_published_recently(), False)

from django.contrib import auth

# from django.test import TestCase
#
# from django.contrib import auth
# from .models import *
#
# class AuthTestCase(TestCase):
#     def setUp(self):
#         self.u = UserProfile.objects.create_user('test@dom.com', 'iamtest', 'pass')
#         self.u.is_staff = True
#         self.u.is_superuser = True
#         self.u.is_active = True
#         self.u.save()
#
#     def testLogin(self):
#         self.client.login(username='test@dom.com', password='pass')
