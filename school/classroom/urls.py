from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thank_you/', views.ThankYouView.as_view(), name = 'thankyou'),
    path('contact/', views.ContactFormView.as_view(), name = 'contact'),
    path('create_teacher/', views.TeacherCreateView.as_view(), name = 'createteacher'),
    path('list_teacher/', views.TeacherListView.as_view(), name='listteacher'),
    path('teacher_detail/<int:pk>/', views.TeacherDetailView.as_view(), name = 'teacherdetail'),
    path('update_teacher/<int:pk>/', views.TeacherUpdateView.as_view(), name = 'updateteacher'),
    path('delete_teacher/<int:pk>/', views.TeacherDeleteView.as_view(), name = 'deleteteacher')
]
