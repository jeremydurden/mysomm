from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')


##This is the logic for the map page
  # template_name = '{TEMPLATE_NAME.html}' 

  # def get_context_data(self, **kwargs):
  #     context = super(IndexView, self).get_context_data(**kwargs)
  #     context['plot'] = map_us.render_map()
  #     return context
