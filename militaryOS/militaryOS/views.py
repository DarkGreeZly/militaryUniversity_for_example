import re

from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from .models import Contact


def index(request):
    return render(request, 'militaryOS/index.html', {
        'current': 'home'
    })

def about(request):
    return render(request, 'militaryOS/about.html', {
        'current': 'university'
    })

def history(request):
    return render(request, 'militaryOS/history.html', {
        'current': 'university'
    })

def fulltime(request):
    return render(request, 'militaryOS/fulltime_form.html', {
        'current': 'entrants'
    })

def distance_form(request):
    return render(request, 'militaryOS/distance_form.html', {
        'current': 'entrants'
    })

def distance_learning(request):
    return render(request, 'militaryOS/distance_learning.html', {
        'current': 'studying'
    })

def science(request):
    return render(request, 'militaryOS/science.html', {
        'current': 'science'
    })

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data_model = {'first_name': form.cleaned_data['first_name'],
                          'last_name': form.cleaned_data['last_name'],
                          'email': form.cleaned_data['email'],
                          'phone': form.cleaned_data['phone'],
                          'details': form.cleaned_data['details']}
            if len(data_model['first_name']) < 1:
                messages.error(request, 'First name must be at least 2 characters')
            elif len(data_model['last_name']) < 1:
                messages.error(request, 'Last name must be at least 2 characters')
            elif len(data_model['email']) < 4:
                messages.error(request, 'Email must be at least 5 characters')
            elif re.search(r'^\+?1?\d{9,15}$', data_model['phone']) == None:
                messages.error(request, 'Enter the correct number from 9 to 15 characters')
            elif len(data_model['details']) < 4:
                messages.error(request, 'Details must be at least 5 characters')
            else:
                contact = Contact(first_name=data_model['first_name'], last_name=data_model['last_name'], email=data_model['email'], phone=data_model['phone'], details=data_model['details'])
                contact.save()
                messages.success(request, 'You contacts successfully sent.')
        else:
            print('form non valid')
            return render(request, 'militaryOS/contact.html', {
                'current': 'contacts',
                'form': form
            })
    return render(request, 'militaryOS/contact.html', {
        'current': 'contacts',
        'form': ContactForm()
    })



class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    email = forms.EmailField(label='Your Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}))
    phone = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+380(xx)xxx-xx-xx'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Give us more detail...', 'row': '6'}))

