from django.urls import path
from example import views

app_name='example'
urlpatterns = [
    # /example/hello
    path('hello/', views.HelloAPI),
]