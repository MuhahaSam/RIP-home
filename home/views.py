from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views import View



# read about UpdateForm, CreateForm, ModelForm (?)


class log_out(View):
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect('/')






