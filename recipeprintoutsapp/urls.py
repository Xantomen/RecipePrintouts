#This is the enersectapp urls file

from django.conf.urls import patterns, url

from recipeprintoutsapp import views

urlpatterns = patterns('',

    # Maintenance Screen
    # ex: recipeprintoutsapp/maintenance_screen
    #url(r'^maintenance_screen/$', views.maintenance_screen, name='maintenance_screen'),

    #Log In View when not authentificated
    #return redirect('/login/' % request.path)
    #ex: /recipeprintoutsapp/login/
    url(r'^login/$', views.app_login, name='app_login'),
        
    # Note: To access to admin panel, the url is simply /admin
    # Admin already has an authentification mode built in.

    # Main (app_index). Shows the four available modes. Can't access them at the moment
    # ex: /recipeprintoutsapp/
    url(r'^$', views.app_index, name='app_index'),   
    
        # Ingredient Nutritional Showcase (Ingredient Search)
        # Shows you an input in which you can search the ingredient you want to look up.
        # (For example, "raw turtle"). When accepted, it will show you the nutritional profile of raw turtle.
        # ex: /subtool/ingredient_search/10021&20030&
        # Note: /subtool/ingredient_search/none when no ingredients are selected
        url(r'^subtool/ingredient_search/(?P<ingredients_string>\w+)/$', views.ingredient_search, name='ingredient_search'),

)
