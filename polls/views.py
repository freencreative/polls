#-*- coding: utf-8 -*-

from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	return HttpResponse("Hello, world")

def redirect_test(request):
	return redirect('/django/polls')

@login_required
def redirect1(request):
        return HttpResponse("Hello, world1")

@login_required
def redirect2(request):
        return HttpResponse("Hello, world2")

def successlogin(request):
        return HttpResponse("이미 로그인 된 상태입니다.")

@login_required
def querystring(request):
	return redirect('/?aa=bb&cc=dd')
