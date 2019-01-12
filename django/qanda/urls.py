from django.urls.conf import path
from .views import AskQuestionView, QuestionDetailView, CreateAnswerView, UpdateAcceptanceAnswer, DailyQuestionList, TodaysQuestionList

app_name = 'qanda'

urlpatterns = [
    path('', TodaysQuestionList.as_view(), name='index'),
    path('ask', AskQuestionView.as_view(), name='ask'),
    path('q/<int:pk>', QuestionDetailView.as_view(), name='question_detail'),
    path('q/<int:pk>/answer', CreateAnswerView.as_view(), name='answer_question'),
    path('q/<int:pk>/accept', UpdateAcceptanceAnswer.as_view(),
         name='update_answer_acceptance'),
    path('daily/<int:year>/<int:month>/<int:day>/',
         DailyQuestionList.as_view(), name='daily_questions')

]
