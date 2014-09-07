
from recipeprintoutsapp.models import *

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response
from django.db import transaction

import random

from django.views import generic
from django.utils import timezone
from datetime import timedelta
import datetime

import json

def ingredient_search(request,ingredients_string = None):

    the_user = request.user

    if not the_user.is_authenticated():
        
        return HttpResponseRedirect(reverse('recipeprintoutsapp:app_login', args=()))
    
    
    user_type= ""
    
    all_food = FoodDes.objects.all()
    
    all_food_content = all_food.values('id','ndb_no','fdgrp_cd','shrt_desc','long_desc')
    all_food_descriptions = all_food.values_list('long_desc',flat=True)
    
    all_food_descriptions = json.dumps(list(all_food_descriptions))
    all_food_content = json.dumps(list(all_food_content))
    
    ingredients_dictionary_list = []
    
    if ingredients_string != "" and ingredients_string != "none":
    
        ingredients_ndb_array = ingredients_string.split("_")
        
        ingredients_dictionary = {}
        
        # Example: [{"1002":{"long_desc":"Turtle","fdgrp_cd":"20","fdgrp_desc":"Dairy Products",
        # "nutrients_dictionary":{"Protein":{"nutr_no":"100","nutr_val":"20","units":"gr"},
        # "Energy":"{"nutr_no":"101","nutr_val":"85","units":"gr"}}}}]
        
        #Variables structure
        #ingredients_dictionary_list = [ingredients_dictionary]
        #ingredients_dictionary = {"1002":ingredient_info,"1001":ingredient_info}
        #ingredient_info = {"long_desc":"Turtle","fdgrp_cd":"20","fdgrp_desc":"Dairy Products","nutrients_dictionary":nutrients_dictionary}
        #nutrients_dictionary = {"Protein":nutrient_info,"Energy":nutrient_info}
        #nutrient_info = {"nutr_no":"100","nutr_val":"20","units":"gr"}
        
        for ndb in ingredients_ndb_array:
            try:
  
                food_item = FoodDes.objects.get(ndb_no = ndb)
    
                if food_item:
       
                    all_nutrients = food_item.NutData_Link.all()

                    ingredient_info = {}

                    ingredient_info["long_desc"] = food_item.long_desc
                    ingredient_info["fdgrp_cd"] = food_item.FdGroup_Link.fdgrp_cd
                    ingredient_info["fdgrp_desc"] = food_item.FdGroup_Link.fdgrp_desc

                    nutrients_dictionary = {}

                    for nutrient in all_nutrients:
        
                        nutrient_info = {}
      
                        nutrient_info["nutr_no"] = nutrient.nutr_no
                        nutrient_info["nutr_val"] = nutrient.nutr_val
                        nutrient_info["units"] = nutrient.NutrDef_Link.units

                        #Control for when the nutrient field has already been filled.
                        #For example, the nutrient "Energy" appears twice per every ingredient, for some reason
                        #This way, we can save both instances
                        
                        try:
                            nutrients_dictionary[nutrient.NutrDef_Link.nutrdesc]
                            nutrients_dictionary[nutrient.NutrDef_Link.nutrdesc+"_2"] = nutrient_info
 
                        except:
                            nutrients_dictionary[nutrient.NutrDef_Link.nutrdesc] = nutrient_info
         
  
                    
                    ingredient_info["nutrients_dictionary"] = nutrients_dictionary
                    ingredients_dictionary[ndb] = ingredient_info

            except:
                nothing_happens = ""
                
        ingredients_dictionary_list.append(ingredients_dictionary)
   
    ingredients_dictionary_list = json.dumps(list(ingredients_dictionary_list))
    
    if ingredients_string == "":
        ingredients_string = "none"
    
    context = {'all_food_content':all_food_content,'all_food_descriptions':all_food_descriptions,
    'ingredients_dictionary_list':ingredients_dictionary_list,'ingredients_string':ingredients_string}
    
    return render(request,'recipeprintoutsapp/ingredient_search.html',context)
    