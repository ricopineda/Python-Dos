from __future__ import unicode_literals
from models import *
from django.shortcuts import render
import random
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):

	return render(request,'python_app/index.html')

def register(request):

	name = request.POST['name']
	alias = request.POST['alias']
	email = request.POST['email']
	password = request.POST['password']

	users = User.objects.filter(email=email)
	if len(users):
		messages.error(request, "This email is taken")
		return redirect('/')
	else:
	
		users = User.objects.create(name=name, alias=alias, email=email, password=password)
		request.session['id'] = users.id
		print request.session['id'] 

		return redirect("/home")

	redirect('/')

def login(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.all().filter(email=email)
		if len(user):
			if user[0].password == password:
				request.session['id'] = user[0].id

				return redirect('/home')
		return redirect ('/')		

def logout(request):

	request.session['id'] = 0
	return redirect('/')

def home(request):

	context = {
	'user': User.objects.get(id=request.session['id']),
	'users':  Quote.objects.all()
	}
	# User.objects.get(id=request.session['id']).upload_quotes.all()
	return render(request, 'python_app/home.html', context)

def add(request):
	quote = request.POST['message']
	quote_by = request.POST['quote_by']
	Quote.objects.create(uploader_id=request.session['id'], message=quote, quote_by=quote_by)

	return redirect('/home')


def add_list(request):

	Quote.objects.get(id=1).quotes.add(User.objects.get(id=request.session['id']))

	context= {
	'fav': User.objects.get(id=request.session['id']).fav_quotes.all()
	}

	return redirect('/home', context)

def view(request):
	context = {
		'user': User.objects.get(id=request.session['id']),
		'quote': User.objects.get(id=request.session['id']).upload_quotes.all()
	}

	return render(request,'python_app/view.html', context)


def delete(request, id):

		a = Quote.objects.get(id=id)
		a.delete()
		a.save()

		return redirect('/view')













