from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo, name="demo"),
    # path('home/',views.new, name="new"),
    # path('create/',views.letter, name="letter")
]



