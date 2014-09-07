from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate

from django.shortcuts import get_object_or_404, render, redirect,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template import RequestContext
from django.views import generic
from django.utils import timezone
from datetime import timedelta
import datetime
from django.db import transaction
from django.db import connection
import re
import json,csv
from django.core import serializers
import random
from pyPdf import PdfFileWriter, PdfFileReader
from urllib2 import Request, urlopen
from StringIO import StringIO
from django.db.models import Count

from recipeprintoutsapp.viewsfunctions import (app_index_module,app_login_module,ingredient_search_module)

from recipeprintoutsapp.models import *

def maintenance_screen(request):
  
    return render(request,'recipeprintoutsapp/maintenance_screen.html',context)

def app_login(request):
  
    return app_login_module.app_login(request)

def app_index(request):
    
    return app_index_module.app_index(request)
    
def ingredient_search(request,ingredients_string = None):
    
    return ingredient_search_module.ingredient_search(request,ingredients_string)