from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Wine

# Create your views here.
def home(request):
  if(request.wine_id):
    selected_wine = Wine.objects.filter(pk=request.wine_id)
  else:
    selected_wine = None
  return render(request, 'base.html', {"selected_wine": selected_wine})

def about(request):
  return render(request, 'about.html')

def my_wines(request):
  my_wines = Wine.objects.filter(user=request.user)
   if(request.wine_id):
    selected_wine = Wine.objects.filter(pk=request.wine_id)
  else:
    selected_wine = None
  return render(request, 'mywines/index.html', {
    "my_wines": my_wines,
     "selected_wine": selected_wine
    })

def my_grapes(request):
  return render(request, 'mygrapes/index.html')

def find_wines(request):
  return render(request, 'findwines/index.html')

def find_wineries(request):
  return render(request, 'findwineries/index.html')


#This is the logic for the map page
  # template_name = '{TEMPLATE_NAME.html}'
  #
  # def get_context_data(self, **kwargs):
  #   context = super(IndexView, self).get_context_data(**kwargs)
  #   context['plot'] = map_us.render_map()
  #   return context
  
  
  

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('about')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

