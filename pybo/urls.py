from django.urls import path
<<<<<<< HEAD
from .views import base_view, question_views, answer_view, comment_view, vote_views
=======
from . import views
>>>>>>> f0cf70c187a02ef13c7821c4c612dbff267fc274

app_name = 'pybo'

urlpatterns = [
<<<<<<< HEAD
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

    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),
]

=======
    path('', views.index, name='index'),                    # 목록보기
    path('<int:question_id>/', views.detail, name='detail'), # 상세 보기   <변환함수:변수명>, 
    path('answer/create/<int:question_id>/', views.answer_create,
        name='answer_create')
]
>>>>>>> f0cf70c187a02ef13c7821c4c612dbff267fc274
