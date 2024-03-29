from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
	context = {
	"title": "WELCOME TO DAIKYO JAPAN MOTORS AN AUTOMOBILE DEALER!",
	"content": "Welcome to the Home Page",

	}
	if request.user.is_authenticated():
		context["premium_content"] = "YEAAAAAAH"
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
	"title": "About Page",
	"content": "Welcome to the About Page"
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
	"title": "Contact Page",
	"content": "Welcome to the Contact Page",
	"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method == "POST":
	# 	#print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, "contact/view.html", context)

def login_page(request):
	form = LoginForm(request.POST or None)
	dect_2 = {
		"form": form
		}
	print("User logged in")
	
	# print(request.user.is_authenticated)
	if form.is_valid():

	    print(form.cleaned_data)
	    username = form.cleaned_data.get("username")
	    password = form.cleaned_data.get("password")
	    user = authenticate(request, username=username, password=password)
	    print(user)
	    # print(request.user.is_authenticated)
	    if user is not None:
	        # print(request.user.is_authenticated)
	        login(request, user)
	        # dect_2['fr'] = form.login_form()
	        return redirect("/login")
	# A backend authenticated the credentials
	    else:
	    	# Return an 'invalid login' error message
	        print("heey you can't")
	# No backend authenticated the credential
	dect_2['fr'] = LoginForm()

	return render(request, "auth/login.html", dect_2)


User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
	"form": form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)	
		print(new_user)	

		context['form'] = RegisterForm()
		
	return render(request, "auth/register.html", context)



def home_page_old(request):
	html_="""
	<!doctype html>
	<html lang="en">
	  <head>
		<!-- Required meta tags -->
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

		<!-- Bootstrap CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

		<title>Hello, world!</title>
	  </head>
	  <body>
	  <div class="text-center">
		<h1>Hello, world!</h1>
	  </div>

		<!-- Optional JavaScript -->
		<!-- jQuery first, then Popper.js, then Bootstrap JS -->
		<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
	  </body>
	</html>
	"""
	return HttpResponse(html_)
