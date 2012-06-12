# -*- coding:Utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	return render_to_response('index.html', locals(), context_instance=RequestContext(request))