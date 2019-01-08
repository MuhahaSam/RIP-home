from django import forms
from users.models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User





class userform(forms.ModelForm):
    class Meta:
        model = user
        fields = ['nickname', 'password', 'check','channel_name']
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
            'check': forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
            'channel_name': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_user(self):
        new_user_login = self.cleaned_data['nickname']
        if user.objects.filter(nickname__iexact=new_user_login).count():
            raise ValidationError('такой логин уже существует! придумайте другой')
        return new_user_login

    def clean_password(self):
        passwd = self.cleaned_data['password']
        if len(passwd) < 4:
            raise ValidationError('слишком короткий пароль')
        return passwd

    def clean_check(self):
        checking = self.cleaned_data['check']
        return checking

    def clean_channel_name(self):
        checking = self.cleaned_data['channel_name']
        if user.objects.filter(channel_name__iexact=checking).count():
            raise ValidationError('такой канал уже существует')
        return checking

    def save(self):
        new_user_1 = User.objects.create_user(
        self.cleaned_data['nickname'],
        'myemail@crazymail.com',
        self.cleaned_data['password'])
        new_user_2 = user.objects.create(nickname = self.cleaned_data['nickname'],
                                         password=self.cleaned_data['password'],
                                         channel_name=self.cleaned_data['channel_name'],
                                         check=self.cleaned_data['check']
                                         )
        return new_user_2


class Postform(forms.ModelForm):
    class Meta:
        model = posts
        fields = ['title','contents', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'contents': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_image(self):
        new_iamge = self.cleaned_data['image']
        return new_iamge

    def clean_contents(self):
        new_contents = self.cleaned_data['contents']
        return new_contents

    def clean_title(self):
        new_title = self.cleaned_data['title']
        return new_title


    def save(self, login_id):
        new_post = posts.objects.create(
            image=self.cleaned_data['image'],
            contents=self.cleaned_data['contents'],
            title=self.cleaned_data['title'],
            userid=login_id
        )
        return new_post









