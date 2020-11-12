from django.shortcuts import render
from .models import Poll, Option
from django.views.generic import ListView, DetailView, RedirectView

# Create your views here.
# def poll_list(req):
#     polls = models.Poll.objects.all()
#     return render(req, 'poll_list.html', {'poll_list': polls})

class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        options = Option.objects.filter(poll_id=self.kwargs['pk'])
        ctx['option_list'] = options
        return ctx

class PollVote(RedirectView):    
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id=self.kwargs['oid'])
        option.count += 1   # option.count = option.count + 1
        option.save()
        return '/poll/{}/'.format(option.poll_id)
        # return '/poll/'+str(option.poll_id)+'/'

