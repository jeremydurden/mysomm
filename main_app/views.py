from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, FormView, DeleteView
from .models import Winery, Wine, Grape
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from . import map_us
from .models import Wine, County
from .forms import WineryForm, WineForm



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
  return render(request, 'wines/index.html', context= {"selected_wines": selected_wines, "plot": map_data})

def profile(request):
  print('inside')
  print(request.user.id)
  my_wineries = Winery.objects.filter(user=request.user.id)

  return render(request, 'profile.html', {'my_wineries': my_wineries})

def glossary(request):
  return render(request, 'glossary.html')

def about(request):
  return render(request, 'about.html')

######### WINERY ########
def find_wineries(request):
  return render(request, 'winery/index.html')

def create_winery(request):
  if request.method == 'POST':
    form = WineryForm(request.POST)
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
  form = WineryForm()
  return render(request, 'main_app/winery_form.html', {"form": form})

def winery_detail(request, winery_id):
  try:
    winery = Winery.objects.get(id=winery_id)
  except:
    return redirect('profile')
  wine_form = WineForm()
  return render(request, 'winery/detail.html', {"winery": winery, "wine_form": wine_form})

def winery_update(request, winery_id):
  winery = Winery.objects.get(pk=winery_id)
  if request.method == 'POST':
    form = WineryForm(request.POST)
    if form.is_valid():
      input_county = form.cleaned_data['county']
      input_state = form.cleaned_data['state']
      db_county = County.objects.get(name=input_county, state=input_state)
      winery.name = form.cleaned_data['name']
      winery.address = form.cleaned_data['address']
      winery.region = form.cleaned_data['region']
      winery.county = db_county
      winery.city = form.cleaned_data['city']
      winery.zipcode = form.cleaned_data['zipcode']
      winery.img_url = form.cleaned_data['img_url']
      winery.logo_url = form.cleaned_data['logo_url']
      winery.user = request.user
      winery.save()
      return redirect('winery_detail', winery_id=winery.id)
  form = WineryForm(initial={
    'name': winery.name,
    'address': winery.address,
    'region': winery.region,
    'county': winery.county.name,
    'city': winery.city,
    'state': winery.county.state,
    'zipcode': winery.zipcode,
    'img_url': winery.img_url,
    'logo_url': winery.logo_url
    })
  return render(request, 'main_app/winery_form.html', {"form": form, "winery": winery})

class WineryDelete(DeleteView):
  model = Winery
  success_url = '/profile/'

######### WINES #########
def my_wines(request):
  # wines = Wine.objects.filter(user=request.user)
  #
  # if request.wine_id:
  #   selected_wine = Wine.objects.filter(pk=request.wine_id)
  # else:
  #   selected_wine = None
  return render(request, 'wines/my_wines.html', {
    # "my_wines": wines,
    # "selected_wine": selected_wine
  })


def create_wine(request, winery_id):
  form = WineForm(request.POST)
  if form.is_valid():
    new_wine = form.save(commit=False)
    new_wine.winery_id = winery_id
    new_wine.save()
  return redirect('winery_detail', winery_id=winery_id)
  






class WineDetail(DetailView):
  model = Wine


class WineUpdate(UpdateView):
  model = Wine
  fields = ['style', 'grape', 'vintage', 'color', 'taste_notes', 'image_url', ]

class WineDelete(DeleteView):
  model = Wine
  def get_success_url(self):
    return redirect ('winery_detail', kwargs={'id':self.object.winery.id})





######## GRAPES #########
def my_grapes(request):
  return render(request, 'mygrapes/index.html')


  
###### REGISTRATION ###########
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

