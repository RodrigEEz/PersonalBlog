from applications.Home.forms import SubscriberForm
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from ..Entry.models import Entry
from .models import Home

from .forms import SubscriberForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):

        context = super(HomePageView, self).get_context_data(**kwargs)
        context["home"] = Home.objects.latest('created')
        context["cover"] = Entry.objects.entry_in_cover()
        context["home_entries"] = Entry.objects.entry_in_home()
        context["recent_entries"] = Entry.objects.recent_entries()
        context["form"] = SubscriberForm
        
        return context