from django.urls import path
from mainapp.apps import MainappConfig
from mainapp import views


app_name = MainappConfig.name

urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('courses/', views.CoursesListView.as_view(), name='courses'),
    path('courses/<int:pk>/detail', views.CoursesDetailView.as_view(), name='courses_detail'),
    path('docsite/', views.DocSiteView.as_view(), name='docsite'),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<int:pk>/detail', views.NewsPageDetailView.as_view(), name='news_detail'),
]



