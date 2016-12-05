from django import forms
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RADIUSAuthenticationForm, NameForm
from django.http import HttpResponse,HttpResponseRedirect

def getlogin(request):
	form = NameForm()
	return render(request, 'users/getlogin.html', {'form':form})

class RADIUSAuthenticationForm(AuthenticationForm):
    def __init__(self, realm, request, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(request, *args, **kwargs)
        self.realm = realm

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if self.realm and username and password:
            self.user_cache = authenticate(realm=self.realm,
                                           username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    'Please enter a correct username and password. '
                    'Note that both fields are case-sensitive.')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('This account is inactive.')
        self.check_for_test_cookie()
        return self.cleaned_data

    def get_user(self):
        return self.user_cache

#def login(request):
#	form = NameForm(request.POST)
#	if form.is_valid():
#		username = form.cleaned_data['username']
#		password = form.cleaned_data['password']
#		loginresult(username,password)
	

#def login(request):
#	#self.realm = realm
#	form = NameForm(request.POST)
#	form_radi = RADIUSAuthenticationForm(form))
#	username = form_radi.cleaned_data['username']
#	password = form_radi.cleaned_data['password']
#	
#	if self.realm and username and password:
#           self.user_cache = authenticate(realm=self.realm,
#                                           username=username,
#                                           password=password)
#            if self.user_cache is None:
#                raise forms.ValidationError(
#                    'Please enter a correct username and password. '
#                    'Note that both fields are case-sensitive.')
#            elif not self.user_cache.is_active:
#                raise forms.ValidationError('This account is inactive.')
#        self.check_for_test_cookie()
#        return self.cleaned_data
