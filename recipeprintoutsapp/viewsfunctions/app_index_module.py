
from recipeprintoutsapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response

def app_index(request):
    
    
    if not request.user.is_authenticated():
        
        return HttpResponseRedirect(reverse('recipeprintoutsapp:app_login', args=()))
    
    interface_type_list = UserInterfaceType.objects.all()
    the_user = request.user
   
    context = {'uitype_list':interface_type_list,"the_user":the_user}
    return render(request,'recipeprintoutsapp/app_index.html',context)