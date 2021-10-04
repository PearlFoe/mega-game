from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
	if request.method == 'POST':
		l_form = AuthenticationForm(request, request.POST)

		if l_form.is_valid():
			user_name = l_form.cleaned_data['username']
			password = l_form.cleaned_data['password']
			user = authenticate(username=user_name, password=password)
			if user:
				login(request, user)
				return redirect('user_personal_page', user_id=user.id)
	else:
		l_form = AuthenticationForm()

	context = {'form':l_form}
	return render(request, 'user_auth/login.html', context)

def logout_view(request):
	logout(request)
	return redirect('index_page')

def register_view(request):
	if request.method == 'POST':
		r_form = UserCreationForm(request.POST)	

		if r_form.is_valid():
			r_form.save()
			user_name = r_form.cleaned_data['username']
			password = r_form.cleaned_data['password1']
			user = authenticate(username=user_name, password=password)
			login(request, user)
			return redirect('user_personal_page', user_id=user.id)
	else:
		r_form = UserCreationForm()

	context = {'form':r_form}
	return render(request, 'user_auth/register.html', context)