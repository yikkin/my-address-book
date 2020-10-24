from django.shortcuts import render , redirect
from .forms import addressform
from .models import address 
from django.contrib import messages

def home(request):
	all_addresses = address.objects.all
	return render(request , "home.html" , {"all_addresses" : all_addresses})

def add_address(request):
	if request.method == "POST":
		form = addressform(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request , ("address has been added!"))

			return redirect("home")

		else: 
			messages.success(request , ("seems like there has been an error..."))
			return render(request , "add_address.html", {})

	else:
		return render(request , "add_address.html",{})


	
# Create your views here.
