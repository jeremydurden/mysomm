from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, FormView
from .models import Winery, Wine, Grape
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from . import map_us
from .models import Wine, County
from .forms import CreateWineryForm



# Create your views here.
def home(request, **kwargs):
  # If no query, then show all
  selected_wines = Wine.objects.all()
  # else show the search results

  wine_query =  []
  for county in County.objects.all():
    county_wines = selected_wines.filter(winery__county = county)
    wine_query.append({
      "name": county.name,
      "state": county.state,
      "lat": county.lat,
      "lon": county.lon,
      "count": len(county_wines)
    })


  map_data= map_us.render_map(wine_query)
  #This is the logic for the map page
  
  return render(request, 'findwines/index.html', context= {"selected_wines": selected_wines, "plot": map_data})

def create_winery(request):
  if request.method == 'POST':
    form = CreateWineryForm(request.POST)
    if form.is_valid():
      input_county = form.cleaned_data['county']
      input_state = form.cleaned_data['state']
      db_county = County.objects.get(name=input_county, state=input_state)
      winery = Winery(
        name = form.cleaned_data['name'],
        address = form.cleaned_data['address'],
        region = form.cleaned_data['region'],
        county = db_county,
        city = form.cleaned_data['city'],
        zipcode = form.cleaned_data['zipcode'],
        img_url = form.cleaned_data['img_url'],
        logo_url = form.cleaned_data['logo_url'],
        user = request.user
      )
      winery.save()
      return redirect('winery_detail', winery_id=winery.id)
  form = CreateWineryForm()
  return render(request, 'main_app/winery_form.html', {"form": form})

def winery_detail(request, winery_id):
  winery = Winery.objects.get(id=winery_id)
  return render(request, 'winery/detail.html', {"winery": winery})

def about(request):
  return render(request, 'about.html')

def my_wines(request):
  my_wines = Wine.objects.filter(user=request.user)

  if request.wine_id:
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

