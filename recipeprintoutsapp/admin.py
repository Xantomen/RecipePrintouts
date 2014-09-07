from django import forms
from django.forms import ModelMultipleChoiceField
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from recipeprintoutsapp.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User,Group
from django.utils.translation import ugettext, ugettext_lazy as _
from django.shortcuts import render


class DataSrcAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Data Source Details",               {'fields': ['id','datasrc_id','authors','title','year','journal','vol_city','issue_state','start_page','end_page']}),
    ]
    list_display = ('id','datasrc_id','authors','title','year','journal','vol_city','issue_state','start_page','end_page')
    
    search_fields = ['id','datasrc_id','authors','title','year','journal','vol_city','issue_state','start_page','end_page']

class DatsrclnAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Data Source ln Details",               {'fields': ['id','ndb_no','nutr_no','datasrc_id']}),
    ]
    list_display = ('id','ndb_no','nutr_no','datasrc_id')
    
    search_fields = ['id','ndb_no','nutr_no','datasrc_id']

class DerivCdAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Deriv Cd Details",               {'fields': ['id','deriv_cd','deriv_desc']}),
    ]
    list_display = ('id','deriv_cd','deriv_desc')
    
    search_fields = ['id','deriv_cd','deriv_desc']

class FdGroupAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Food Group Details",               {'fields': ['id','fdgrp_cd','fdgrp_desc']}),
    ]
    list_display = ('id','fdgrp_cd','fdgrp_desc')
    
    search_fields = ['id','fdgrp_cd','fdgrp_desc']  
    
class FoodDesAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Food Details",               {'fields': ['id','ndb_no','fdgrp_cd','comname','long_desc','shrt_desc','manufacname','survey','ref_desc','refuse','sciname','n_factor','pro_factor','fat_factor','cho_factor']}),
    ]
    list_display = ('id','ndb_no','fdgrp_cd','comname','long_desc','shrt_desc','manufacname','survey','ref_desc','refuse','sciname','n_factor','pro_factor','fat_factor','cho_factor')
    
    search_fields = ['ndb_no','fdgrp_cd','long_desc','shrt_desc']        
        

class FootnoteAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Foot Note Details",               {'fields': ['id','ndb_no','footnt_no','footnt_typ','nutr_no','footnt_txt']}),
    ]
    list_display = ('id','ndb_no','footnt_no','footnt_typ','nutr_no','footnt_txt')
    
    search_fields = ['id','ndb_no','footnt_no','footnt_typ','nutr_no','footnt_txt']        


class LangdescAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Language Description Details",               {'fields': ['id','factor_code','description']}),
    ]
    list_display = ('id','factor_code','description')
    
    search_fields = ['id','factor_code','description']         
        

class LangualAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Language Al Details",               {'fields': ['id','ndb_no','factor_code']}),
    ]
    list_display = ('id','ndb_no','factor_code')
    
    search_fields = ['id','ndb_no','factor_code']   
    

class NutDataAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Nutritional Data Details",               {'fields': ['id','ndb_no','nutr_no','nutr_val','num_data_pts','std_error','src_cd','deriv_cd',
    'ref_ndb_no','add_nutr_mark','num_studies',
    'min','max','df','low_eb','up_eb','stat_cmt','addmod_date','cc']}),
    ]
    list_display = ('id','ndb_no','nutr_no','nutr_val','num_data_pts','std_error','src_cd','deriv_cd',
    'ref_ndb_no','add_nutr_mark','num_studies',
    'min','max','df','low_eb','up_eb','stat_cmt','addmod_date','cc')
    
    search_fields = ['id','ndb_no','nutr_no','nutr_val','num_data_pts','std_error','src_cd','deriv_cd',
    'ref_ndb_no','add_nutr_mark','num_studies',
    'min','max','df','low_eb','up_eb','stat_cmt','addmod_date','cc']           
        
class NutrDefAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Nutritional Def Details",               {'fields': ['id','nutr_no','units','tagname','nutrdesc','num_dec','sr_order']}),
    ]
    list_display = ('id','nutr_no','units','tagname','nutrdesc','num_dec','sr_order')
    
    search_fields = ['id','nutr_no','units','tagname','nutrdesc','num_dec','sr_order']     
        

class SrcCdAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Source Cd Details",               {'fields': ['id','src_cd','srccd_desc']}),
    ]
    list_display = ('id','src_cd','srccd_desc')
    
    search_fields = ['id','src_cd','srccd_desc']           
        

class WeightAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Source Cd Details",               {'fields': ['id','ndb_no','seq','amount','msre_desc','gm_wgt','num_data_pts','std_dev']}),
    ]
    list_display = ('id','ndb_no','seq','amount','msre_desc','gm_wgt','num_data_pts','std_dev')
    
    search_fields = ['id','ndb_no','seq','amount','msre_desc','gm_wgt','num_data_pts','std_dev']             
        

admin.site.register(UserInterfaceType)
        
admin.site.register(DataSrc, DataSrcAdmin)    
admin.site.register(Datsrcln, DatsrclnAdmin)    
admin.site.register(DerivCd, DerivCdAdmin) 
admin.site.register(FoodDes, FoodDesAdmin)   
admin.site.register(FdGroup, FdGroupAdmin) 
admin.site.register(Footnote, FootnoteAdmin)
admin.site.register(Langdesc, LangdescAdmin)
admin.site.register(Langual, LangualAdmin)
admin.site.register(NutData, NutDataAdmin)
admin.site.register(NutrDef, NutrDefAdmin)
admin.site.register(SrcCd, SrcCdAdmin)
admin.site.register(Weight, WeightAdmin)







