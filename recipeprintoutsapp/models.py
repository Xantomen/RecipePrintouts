# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

#Table to organise the different possible views/interfaces (in case there are different tools)

class UserInterfaceType(models.Model):
    name = models.CharField(max_length=255,default='')
    redirection_url = models.CharField(max_length=255,default='')
    def __unicode__(self):
        return self.name





# Sources of Data File (file name = DATA_SRC). This file (Table 15) provides a citation 
# to the DataSrc_ID in the Sources of Data Link file. 

class DataSrc(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    datasrc_id = models.TextField(unique=True, db_column='DataSrc_ID', blank=True) # Field name made lowercase.
    authors = models.TextField(db_column='Authors', blank=True) # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True) # Field name made lowercase.
    year = models.TextField(db_column='Year', blank=True) # Field name made lowercase.
    journal = models.TextField(db_column='Journal', blank=True) # Field name made lowercase.
    vol_city = models.TextField(db_column='Vol_City', blank=True) # Field name made lowercase.
    issue_state = models.TextField(db_column='Issue_State', blank=True) # Field name made lowercase.
    start_page = models.TextField(db_column='Start_Page', blank=True) # Field name made lowercase.
    end_page = models.TextField(db_column='End_Page', blank=True) # Field name made lowercase.
    
    class Meta:
        db_table = 'data_src'
    def __unicode__(self):
        return self.datasrc_id

# Sources of Data Link File (file name = DATSRCLN). This file (Table 14) is used to link 
# the Nutrient Data file with the Sources of Data table. It is needed to resolve the many-to-many
 # relationship between the two tables.
        
class Datsrcln(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    ndb_no = models.TextField(db_column='NDB_No', blank=True) # Field name made lowercase.
    nutr_no = models.TextField(db_column='Nutr_No', blank=True) # Field name made lowercase.
    datasrc_id = models.TextField(db_column='DataSrc_ID', blank=True) # Field name made lowercase.
    
    DataSrc_Link = models.ForeignKey('DataSrc', blank=True,null =True)
    
    class Meta:
        db_table = 'datsrcln'
    def __unicode__(self):
        return self.datasrc_id
        
# Data Derivation Code Description File (file name = DERIV_CD). This file (Table 11) 
# provides information on how the nutrient values were determined. The file contains the 
# derivation codes and their descriptions.         
        
        
class DerivCd(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    deriv_cd = models.TextField(unique=True, db_column='Deriv_Cd', blank=True) # Field name made lowercase.
    deriv_desc = models.TextField(db_column='Deriv_Desc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'deriv_cd'
    def __unicode__(self):
        return self.deriv_desc
        
#Food Group Description File (file name = FD_GROUP). This file (Table 5) is a 
# support file to the Food Description file and contains a list of food groups used in SR26 
# and their descriptions.         
        
class FdGroup(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    fdgrp_cd = models.TextField(unique=True, db_column='FdGrp_Cd', blank=True) # Field name made lowercase.
    fdgrp_desc = models.TextField(db_column='FdGrp_Desc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'fd_group'
    def __unicode__(self):
        return self.fdgrp_desc
        
#Food Description File (file name = FOOD_DES). This file (Table 4) contains long and 
# short descriptions and food group designators for 8,463 food items, along with common 
# names, manufacturer name, scientific name, percentage and description of refuse, and 
# factors used for calculating protein and kilocalories, if applicable. Items used in the 
# FNDDS are also identified by value of "Y" in the Survey field.     
        
class FoodDes(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    ndb_no = models.TextField(unique=True, db_column='NDB_No', blank=True) # Field name made lowercase.
    fdgrp_cd = models.TextField(db_column='FdGrp_Cd', blank=True) # Field name made lowercase.
    long_desc = models.TextField(db_column='Long_Desc', blank=True) # Field name made lowercase.
    shrt_desc = models.TextField(db_column='Shrt_Desc', blank=True) # Field name made lowercase.
    comname = models.TextField(db_column='ComName', blank=True) # Field name made lowercase.
    manufacname = models.TextField(db_column='ManufacName', blank=True) # Field name made lowercase.
    survey = models.TextField(db_column='Survey', blank=True) # Field name made lowercase.
    ref_desc = models.TextField(db_column='Ref_desc', blank=True) # Field name made lowercase.
    refuse = models.TextField(db_column='Refuse', blank=True) # Field name made lowercase.
    sciname = models.TextField(db_column='SciName', blank=True) # Field name made lowercase.
    n_factor = models.TextField(db_column='N_Factor', blank=True) # Field name made lowercase.
    pro_factor = models.TextField(db_column='Pro_Factor', blank=True) # Field name made lowercase.
    fat_factor = models.TextField(db_column='Fat_Factor', blank=True) # Field name made lowercase.
    cho_factor = models.TextField(db_column='CHO_Factor', blank=True) # Field name made lowercase.
    
    FdGroup_Link = models.ForeignKey('FdGroup', blank=True,null =True)
    Footnote_Link = models.ForeignKey('Footnote', blank=True,null =True)
    NutData_Link = models.ManyToManyField('NutData', blank=True,null =True)
    Weight_Link = models.ForeignKey('Weight', blank=True,null =True)
    Langual_Link = models.ManyToManyField('Langual', blank=True,null =True)
    
    class Meta:
        db_table = 'food_des'
    def __unicode__(self):
        return self.long_desc
        
# Footnote File (file name = FOOTNOTE). This file (Table 13) contains additional 
# information about the food item, household weight, and nutrient value.         
        
class Footnote(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    ndb_no = models.TextField(db_column='NDB_No', blank=True) # Field name made lowercase.
    footnt_no = models.TextField(db_column='Footnt_No', blank=True) # Field name made lowercase.
    footnt_typ = models.TextField(db_column='Footnt_Typ', blank=True) # Field name made lowercase.
    nutr_no = models.TextField(db_column='Nutr_No', blank=True) # Field name made lowercase.
    footnt_txt = models.TextField(db_column='Footnt_Txt', blank=True) # Field name made lowercase.
    
    NutData_Link = models.ManyToManyField('NutData', blank=True,null =True)
    
    class Meta:
        db_table = 'footnote'
    def __unicode__(self):
        return self.footnt_txt
        
        
# LanguaL Factors Description File (File name = LANGDESC). This file (Table 7) is a 
# support file to the LanguaL Factor file and contains the descriptions for only those 
# factors used in coding the selected food items codes in this release of SR.         
        
class Langdesc(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    factor_code = models.TextField(db_column='Factor_Code', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'langdesc'
    def __unicode__(self):
        return self.description
        
# LanguaL Factor File (File name = LANGUAL). This file (Table 6) is a support file to the 
# Food Description file and contains the factors from the LanguaL Thesaurus used to 
# code a particular food.       
        
class Langual(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    ndb_no = models.TextField(db_column='NDB_No', blank=True) # Field name made lowercase.
    factor_code = models.TextField(db_column='Factor_Code', blank=True) # Field name made lowercase.
    
    Langdesc_Link = models.ForeignKey('Langdesc', blank=True,null =True)
    
    class Meta:
        db_table = 'langual'
    def __unicode__(self):
        return self.factor_code
        
# Nutrient Data File (file name = NUT_DATA). This file (Table 8) contains the nutrient 
# values and information about the values, including expanded statistical information.       
        
class NutData(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    ndb_no = models.TextField(db_column='NDB_No', blank=True) # Field name made lowercase.
    nutr_no = models.TextField(db_column='Nutr_No', blank=True) # Field name made lowercase.
    nutr_val = models.TextField(db_column='Nutr_Val', blank=True) # Field name made lowercase.
    num_data_pts = models.TextField(db_column='Num_Data_Pts', blank=True) # Field name made lowercase.
    std_error = models.TextField(db_column='Std_Error', blank=True) # Field name made lowercase.
    src_cd = models.TextField(db_column='Src_Cd', blank=True) # Field name made lowercase.
    deriv_cd = models.TextField(db_column='Deriv_Cd', blank=True) # Field name made lowercase.
    ref_ndb_no = models.TextField(db_column='Ref_NDB_No', blank=True) # Field name made lowercase.
    add_nutr_mark = models.TextField(db_column='Add_Nutr_Mark', blank=True) # Field name made lowercase.
    num_studies = models.TextField(db_column='Num_Studies', blank=True) # Field name made lowercase.
    min = models.TextField(db_column='Min', blank=True) # Field name made lowercase.
    max = models.TextField(db_column='Max', blank=True) # Field name made lowercase.
    df = models.TextField(db_column='DF', blank=True) # Field name made lowercase.
    low_eb = models.TextField(db_column='Low_EB', blank=True) # Field name made lowercase.
    up_eb = models.TextField(db_column='Up_EB', blank=True) # Field name made lowercase.
    stat_cmt = models.TextField(db_column='Stat_cmt', blank=True) # Field name made lowercase.
    addmod_date = models.TextField(db_column='AddMod_Date', blank=True) # Field name made lowercase.
    cc = models.TextField(db_column='CC', blank=True) # Field name made lowercase.
    
    NutrDef_Link = models.ForeignKey('NutrDef', blank=True,null =True)
    SrcCd_Link = models.ForeignKey('SrcCd', blank=True,null =True)
    DerivCd_Link = models.ForeignKey('DerivCd', blank=True,null =True)
    Datsrcln_Link = models.ForeignKey('Datsrcln', blank=True,null =True)
    
    class Meta:
        db_table = 'nut_data'
    def __unicode__(self):
        return self.nutr_no
        
# Nutrient Definition File (file name = NUTR_DEF). This file (Table 9) is a support file to 
# the Nutrient Data file. It provides the 3-digit nutrient code, unit of measure, INFOODS 
# tagname, and description.      
        
class NutrDef(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    nutr_no = models.TextField(unique=True, db_column='Nutr_No', blank=True) # Field name made lowercase.
    units = models.TextField(db_column='Units', blank=True) # Field name made lowercase.
    tagname = models.TextField(db_column='Tagname', blank=True) # Field name made lowercase.
    nutrdesc = models.TextField(db_column='NutrDesc', blank=True) # Field name made lowercase.
    num_dec = models.TextField(db_column='Num_Dec', blank=True) # Field name made lowercase.
    sr_order = models.TextField(db_column='SR_Order', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'nutr_def'
    def __unicode__(self):
        return self.nutrdesc
        
# Source Code File (file name = SRC_CD). This file (Table 10) contains codes indicating 
# the type of data (analytical, calculated, assumed zero, and so on) in the Nutrient Data 
# file. To improve the usability of the database and to provide values for the FNDDS, NDL 
# staff imputed nutrient values for a number of proximate components, total dietary fiber, 
# total sugar, and vitamin and mineral values.        
        
        
class SrcCd(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    src_cd = models.TextField(unique=True, db_column='Src_Cd', blank=True) # Field name made lowercase.
    srccd_desc = models.TextField(db_column='SrcCd_Desc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'src_cd'

    def __unicode__(self):
        return self.srccd_desc    
# Weight File (file name = WEIGHT). This file (Table 12) contains the weight in grams of 
# a number of common measures for each food item. 
       
class Weight(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    ndb_no = models.TextField(db_column='NDB_No', blank=True) # Field name made lowercase.
    seq = models.TextField(db_column='Seq', blank=True) # Field name made lowercase.
    amount = models.TextField(db_column='Amount', blank=True) # Field name made lowercase.
    msre_desc = models.TextField(db_column='Msre_Desc', blank=True) # Field name made lowercase.
    gm_wgt = models.TextField(db_column='Gm_Wgt', blank=True) # Field name made lowercase.
    num_data_pts = models.TextField(db_column='Num_Data_Pts', blank=True) # Field name made lowercase.
    std_dev = models.TextField(db_column='Std_Dev', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'weight'

    def __unicode__(self):
        return self.amount