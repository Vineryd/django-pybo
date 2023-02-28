from django.urls import path
from .views import base_view, question_views, answer_view, comment_view

app_name = 'pybo'

urlpatterns = [
    path('', base_view.index, name='index'),                      # 목록 보기
    path('<int:question_id>/', base_view.detail, name='detail'),   # 상세 보기
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),

    path('answer/create/<int:question_id>/', answer_view.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_view.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_view.answer_delete, name='answer_delete'),

    path('comment/create/question/<int:question_id>/', comment_view.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_view.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_view.comment_delete_question, name='comment_delete_question'),

    path('comment/create/answer/<int:answer_id>/', comment_view.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_view.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_view.comment_delete_answer, name='comment_delete_answer'),
]
