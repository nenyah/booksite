from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bid>/', views.bookDetail, name='bookDetail'),
    path('history/', views.viewHistory, name='viewHistory'),
    path('cate/<int:cateid>', views.bookCate, name='bookCate'),
    path('login', views.logIn, name='login'),
    path('register', views.register, name='register')
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
