from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('create-account/', views.CreateAccount.as_view(), name="create_account"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/', views.course_index, name='course_index'),
    path('courses/filter/', views.course_filter, name='course_filter'),
    path('courses/create/', views.course_create, name="course_create"),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/update/', views.course_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('meetings/', views.meeting_index, name='meeting_index'),
    path('meetings/filter/', views.meeting_filter, name='meeting_filter'),
    path('meetings/create/', views.meeting_create, name='meeting_create'),
    path('meetings/<int:pk>/', views.meeting_detail, name='meeting_detail'),
    path('meetings/<int:pk>/update/', views.meeting_update, name='meeting_update'),
    path('meetings/<int:pk>/delete/', views.meeting_delete, name='meeting_delete'),
    path('projects/', views.project_index, name='project_index'),
    path('projects/filter/', views.project_filter, name='project_filter'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/update/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('activities/', views.activity_index, name='activity_index'),
    path('activities/filter/', views.activity_filter, name='activity_filter'),
    path('activities/create/', views.activity_create, name='activity_create'),
    path('activities/<int:pk>/', views.activity_detail, name='activity_detail'),
    path('activities/<int:pk>/update/', views.activity_update, name='activity_update'),
    path('activities/<int:pk>/delete/', views.activity_delete, name='activity_delete'),
]
