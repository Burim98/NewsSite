from django.shortcuts import render
from .models import ModelNews
from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import ModelNewsForm

def index(request):
    return render(request, 'News/index.html')

def new(request):
    bbs = ModelNews.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'News/NewsIndex.html', context)

def by_rubric(request,rubric_id):
    bbs = ModelNews.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'News/by_rubric.html', context)

class ModelNewsCreateView(CreateView):
    template_name = 'News/create.html'
    form_class = ModelNewsForm
    success_url = '/News/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

