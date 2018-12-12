# posts/api.py
from django.contrib.auth.models import User

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from .models import Question


class QuestionResource(DjangoResource):
    # Controls what data is included in the serialized output.
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'question': 'question_text'
    })

    # GET /
    def list(self):
        return Question.objects.all()

    # GET /pk/
    def detail(self, pk):
        return Question.objects.get(id=pk)

    # POST /
    def create(self):
        return Question.objects.create(
            question_text=self.data['question'],
        )

    # PUT /pk/
    def update(self, pk):
        try:
            question = Question.objects.get(id=pk)
        except Question.DoesNotExist:
            question = Question()

        question.question_text = self.data['question']
        question.save()
        return question

    # DELETE /pk/
    def delete(self, pk):
        Question.objects.get(id=pk).delete()