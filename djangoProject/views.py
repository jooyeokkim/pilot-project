from django.views.generic import TemplateView
from user.models import User

class HomeView(TemplateView):
    user=User.objects.all()
    userList=list(user)
    print("id", userList)
    template_name='home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
