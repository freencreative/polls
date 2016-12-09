from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	return HttpResponse("Hello, world")

def redirect_test(request):
	return redirect('/polls')

