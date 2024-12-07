from django.core.management.base import BaseCommand
from evaluation.models import Question


class Command(BaseCommand):
    help = 'Populates the database with initial questions'

    def handle(self, *args, **kwargs):
        questions = [
            {
                "type": "reading",
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "answer": "Paris"
            },
            {
                "type": "reading",
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "answer": "4"
            },
        ]
        for q in questions:
            Question.objects.get_or_create(**q)
        self.stdout.write(self.style.SUCCESS('Questions populated successfully!'))
