from django.shortcuts import render
from django.http import JsonResponse
import requests

def text_search(request):
	api_key = 'AIzaSyBwf1T5RclM-0D89IIeaBxBNjpPW69Yjjw'
	query = request.GET.get('query','')
	next_page_token = request.GET.get('next_page_token')
	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=%s'%(query, api_key)
	#url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&key="+API_KEY

	if next_page_token is not None:
		url+='&pagetoken=%s'%(next_page_token)

	response = requests.get(url)

	# return JsonResponse(response.json(), safe=False)
	return render(request, 'text.html', {'response': response.json()})


def place_search(request):
	api_key = 'AIzaSyBwf1T5RclM-0D89IIeaBxBNjpPW69Yjjw'
	key = 'AIzaSyC6CdCvlJZuAOJUhlHWDzlnXN7X7bo2rcY'
	reference = request.GET.get('reference')
	url = 'https://maps.googleapis.com/maps/api/place/details/json?reference=%s&key=%s'%(reference, api_key)
	#url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&key="+API_KEY

	response = requests.get(url)

	# return JsonResponse(response.json(), safe=False)
	return render(request, 'detail.html', {'response': response.json(), 'key':key})

def nearby_search(request):
	api_key = 'AIzaSyBwf1T5RclM-0D89IIeaBxBNjpPW69Yjjw'
	location = request.GET.get('location')
	radius = request.GET.get('radius','')

	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&key=%s'%(location, radius, api_key)
	response = requests.get(url)
	return render(request, 'nearby.html', {'response': response.json()})

	# return JsonResponse(response.json(), safe=False)
