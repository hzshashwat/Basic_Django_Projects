from django.urls import path
from . import views

urlpatterns = [
    path('simpleview',views.simple_view),
    path('',views.first_app),
    path('<int:page_num>',views.num_page_view),
    path('<topic>' ,views.news_view,name="topic-view"),
    path('<int:num1>/<int:num2>',views.add_view)
]