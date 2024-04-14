import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_str(self):
        text: str = "What's up?"
        question = Question(question_text=text, pub_date=timezone.now())
        self.assertEqual(str(question), text)

    def test_does_not_exist(self):
        with self.assertRaises(Question.DoesNotExist):
            Question.objects.get(pk=1)

    def test_save_question(self):
        question_text = "What's new?"
        pub_date = timezone.now()
        question = Question(question_text=question_text, pub_date=pub_date)
        question.save()

        retrieved_question = Question.objects.get(pk=question.id)
        self.assertEqual(retrieved_question.question_text, question_text)
        self.assertEqual(retrieved_question.pub_date, pub_date)
