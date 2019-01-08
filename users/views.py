from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from users.models import *
from django.views import View
from users.forms import *
from django.contrib.auth import authenticate, login, logout
from users.common import Common
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from home.settings import MEDIA_URL, BASE_DIR

class base(Common, View):
    def get(self, request):
        return render(request, 'base.html', context={'errorrr': request.session.get('error')})


class new_user(Common,View):
    def get(self,request):
        form = userform
        return render(request, 'registration/regis.html' , context={'form': form })

    def post(self, request):
        bound_form = userform(request.POST)
        if bound_form.is_valid():
            newuser = bound_form.save()
            return HttpResponseRedirect('/')
        return render(request, 'registration/regis.html', context={'form': bound_form })



class loginpage(Common,View):
    def get(self, request):
        #print(request.session['login_id'])
        return render(request, 'mypage.html')



    def post(self, request):
        #session_key = request.session.session_key
        user_name = request.POST['login']
        password = request.POST['passwd']
        user = authenticate(username=user_name, password=password)
        if user is not None:
            request.session['error'] = False
            login(request, user)
            request.session['login_id'] = user_name
            print(request.session['login_id'])
            return redirect('/mypage')
        else:
            request.session['error'] = True
            print('it is i,possible to login')
            return HttpResponseRedirect('/')

class upload(LoginRequiredMixin,Common, View):
    raise_exception = False
    def get(self, request):
        form = Postform
        return render(request, 'upload.html', context={'form': form})

    def post(self, request):
        form = Postform(request.POST,request.FILES)
        if form.is_valid():
            print(form.errors)
            logined_user = user.objects.get(nickname=request.session['login_id'])
            form.save(logined_user)
            print("it's saved")
        return HttpResponseRedirect('/mypage')

class ajax_upload(View):
    def get(self, request):
        form = Postform
        return render(request, 'upload.html', context={'form': form})


class show_posts(LoginRequiredMixin,Common, View):
    raise_exception = False
    def get(self, request):
        post = posts.objects.all()
        paginator = Paginator(post, 2)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        print(request.GET.get('page', 1))
        return render(request, 'posts.html', context={'page':page, 'MEDIA_URL':MEDIA_URL})

    def post(self, request):
        return None

class show_posts2(LoginRequiredMixin,Common, View):
    raise_exception = False
    def get(self, request):
        post = posts.objects.all()
        paginator = Paginator(post, 2)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        print(request.GET.get('page', 1))
        return render(request, 'posts.html', context={'page':page, 'MEDIA_URL':MEDIA_URL})

    def post(self, request):
        return None



class show_my_posts(LoginRequiredMixin,Common, View):
    raise_exception = False
    def get(self, request):
        post = posts.objects.filter(userid=user.objects.get(nickname=request.session['login_id']))
        paginator = Paginator(post, 2)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        print(request.GET.get('page', 1))
        return render(request, 'posts.html', context={'page':page, 'MEDIA_URL':MEDIA_URL})

    def post(self, request):
        return None









