from django.views.generic import TemplateView
from user.models import User

class HomeView(TemplateView):
    user=User.objects.all()
    userList=list(user)
    print("id", userList)
    print(userList[0])
    print(userList[1])
    template_name='home.html'

