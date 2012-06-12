# -*- coding:Utf-8 -*-
from django import forms
from django.forms.models import ModelForm
from models import *

class createMenu(ModelForm):
	name = forms.CharField(widget=forms.TextInput,max_length=100)

	class Meta:
		exclude = 'enable'
		model = Menu

class createStarter(ModelForm):
	name = forms.CharField(widget=forms.TextInput,max_length=100)
	price = forms.IntegerField(widget=forms.TextInput)

	class Meta:
		exclude = 'menu'
		model = Starter

class createDish(ModelForm):
	name = forms.CharField(widget=forms.TextInput,max_length=100)
	price = forms.IntegerField(widget=forms.TextInput)

	class Meta:
		exclude = 'menu'
		model = Dishes

class createDessert(ModelForm):
	name = forms.CharField(widget=forms.TextInput,max_length=100)
	price = forms.IntegerField(widget=forms.TextInput)

	class Meta:
		exclude = 'menu'
		model = Dessert


