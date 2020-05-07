#watch out
from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	api_rquest= requests.get("http://api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={215f0416ba9e09387babe40ef5517a81}Parameters:")
	
	try:
		api = json.loads(api_request.content)

	except Exception as e:
		api="Error..."



	return render(request,"home.html",{'api':api})

def about(request):
	return render(request,"about.html",{})
	