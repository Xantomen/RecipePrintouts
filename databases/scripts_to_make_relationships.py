
#Steps followed to turn all conceptual/model references of
#the different tables in the USDA Database s25 into actual references,
#in ForeignKey/ManytoMany fields

#This are the relationships to cover in the loops:

FoodDes relationships to fill:

FdGroup_Link = models.ForeignKey('FdGroup', blank=True,null =True) based on fdgrp_cd
Footnote_Link = models.ForeignKey('Footnote', blank=True,null =True) based on ndb_no
NutData_Link = models.ManyToManyField('NutData', blank=True,null =True) based on ndb_no
Weight_Link = models.ForeignKey('Weight', blank=True,null =True) based on ndb_no
Langual_Link = models.ManyToManyField('Langual', blank=True,null =True) based on ndb_no

Footnote relationships to fill:

NutData_Link = models.ForeignKey('NutData', blank=True,null =True) based on ndb_no

NutData relationships to fill:

NutrDef_Link = models.ForeignKey('NutrDef', blank=True,null =True) based on nutr_no
SrcCd_Link = models.ForeignKey('SrcCd', blank=True,null =True) based on src_cd
DerivCd_Link = models.ForeignKey('DerivCd', blank=True,null =True) based on deriv_cd
Datsrcln_Link = models.ForeignKey('Datsrcln', blank=True,null =True) based on ndb_no

Langual relationships to fill:

Langdesc_Link = models.ForeignKey('Langdesc', blank=True,null =True) based on factor_code

Datsrcln relationships to fill:

DataSrc_Link = models.ForeignKey('DataSrc', blank=True,null =True) based on datasrc_id

#################

#The actual loops to cover those relationships. Copy into django shell from this point on:

from recipeprintoutsapp.models import *
from django.db import transaction
from django import db

#FoodDes relationships:

count = 0

with transaction.commit_on_success():
    for item in FoodDes.objects.all():
        count+=1
        if count % 500 == 0:
            print count
            db.reset_queries()
        #FdGroup_Link
        try:
            FdGroup_Link = FdGroup.objects.get(fdgrp_cd = item.fdgrp_cd)
            item.FdGroup_Link = FdGroup_Link
        except:
            nothing_happens = ""
        #Footnote_Link
        try:
            Footnote_Link = Footnote.objects.get(ndb_no = item.ndb_no)
            item.Footnote_Link = Footnote_Link
        except:
            nothing_happens = ""
        #NutData_Link
        try:
            NutData_Link = NutData.objects.filter(ndb_no = item.ndb_no)
            for nutrient in NutData_Link:
                item.NutData_Link.add(nutrient)
        except:
            nothing_happens = ""
        #Weight_Link
        try:
            Weight_Link = Weight.objects.get(ndb_no = item.ndb_no)
            item.Weight_Link = Weight_Link
        except:
            nothing_happens = ""
        #Langual_Link
        try:
            Langual_Link = Langual.objects.filter(ndb_no = item.ndb_no)
            for langual in Langual_Link:
                item.Langual_Link.add(langual)
        except:
            nothing_happens = ""
            
        item.save()

      
#Footnote relationships:

count = 0

with transaction.commit_on_success():
    for item in Footnote.objects.all():
        count+=1
        if count % 500 == 0:
            print count
            db.reset_queries()
        #NutData_Link
        try:
            NutData_Link = NutData.objects.filter(ndb_no = item.ndb_no)
            for nutrient in NutData_Link:
                item.NutData_Link.add(nutrient)
        except:
            nothing_happens = ""
            
        item.save()
        
#NutData relationships:

count = 0

with transaction.commit_on_success():
    for item in NutData.objects.all():
        count+=1
        if count % 500 == 0:
            print count
            db.reset_queries()
        #NutrDef_Link
        try:
            NutrDef_Link = NutrDef.objects.get(nutr_no = item.nutr_no)
            item.NutrDef_Link = NutrDef_Link
        except:
            nothing_happens = ""
        #SrcCd_Link
        try:
            SrcCd_Link = SrcCd.objects.get(src_cd = item.src_cd)
            item.SrcCd_Link = SrcCd_Link
        except:
            nothing_happens = ""
        #DerivCd_Link
        try:
            DerivCd_Link = DerivCd.objects.get(deriv_cd = item.deriv_cd)
            item.DerivCd_Link = DerivCd_Link
        except:
            nothing_happens = ""
        #Datsrcln_Link
        try:
            Datsrcln_Link = Datsrcln.objects.get(ndb_no = item.ndb_no)
            item.Datsrcln_Link = Datsrcln_Link
        except:
            nothing_happens = ""
            
        item.save()

#Langual relationships:

count = 0

with transaction.commit_on_success():
    for item in Langual.objects.all():
        count+=1
        if count % 500 == 0:
            print count
            db.reset_queries()
        #Langdesc_Link
        try:
            Langdesc_Link = Langdesc.objects.get(factor_code = item.factor_code)
            item.Langdesc_Link = Langdesc_Link
        except:
            nothing_happens = ""
            
        item.save()   

#Datsrcln relationships:

count = 0

with transaction.commit_on_success():
    for item in Datsrcln.objects.all():
        count+=1
        if count % 500 == 0:
            print count
            db.reset_queries()
        #DataSrc_Link
        try:
            DataSrc_Link = DataSrc.objects.get(datasrc_id = item.datasrc_id)
            item.DataSrc_Link = DataSrc_Link
        except:
            nothing_happens = ""
            
        item.save()        