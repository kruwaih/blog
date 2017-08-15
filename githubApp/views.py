from django.http import JsonResponse
from django.shortcuts import render
import requests

def org_members(request):
	person = request.user 
	github_account = person.socialaccount_set.get(user=person.id)
	token_object = github_account.socialtoken_set.get(account=github_account.id)
	token = token_object.token

	url = 'http://api.github.com/orgs/joinCODED/members'

	response = requests.get(url, headers={'Authorization': 'token '+token})
	# return JsonResponse(response.json(), safe=False)

	return render(request, 'members.html', {'response': response.json()})


def list_branches(request):
	user = request.user
	github_account = user.socialaccount_set.get(user=user.id)
	token_object = github_account.socialtoken_set.get(account=github_account.id)
	token = token_object.token
	url = 'http://api.github.com/repos/kruwaih/blog/branches'

	response = requests.get(url, headers={'Authorization': 'token '+token})
	return JsonResponse(response.json(), safe=False)
