# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DataSrc'
        db.create_table(u'data_src', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('datasrc_id', self.gf('django.db.models.fields.TextField')(unique=True, db_column=u'DataSrc_ID', blank=True)),
            ('authors', self.gf('django.db.models.fields.TextField')(db_column=u'Authors', blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')(db_column=u'Title', blank=True)),
            ('year', self.gf('django.db.models.fields.TextField')(db_column=u'Year', blank=True)),
            ('journal', self.gf('django.db.models.fields.TextField')(db_column=u'Journal', blank=True)),
            ('vol_city', self.gf('django.db.models.fields.TextField')(db_column=u'Vol_City', blank=True)),
            ('issue_state', self.gf('django.db.models.fields.TextField')(db_column=u'Issue_State', blank=True)),
            ('start_page', self.gf('django.db.models.fields.TextField')(db_column=u'Start_Page', blank=True)),
            ('end_page', self.gf('django.db.models.fields.TextField')(db_column=u'End_Page', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['DataSrc'])

        # Adding model 'Datsrcln'
        db.create_table(u'datsrcln', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('ndb_no', self.gf('django.db.models.fields.TextField')(db_column=u'NDB_No', blank=True)),
            ('nutr_no', self.gf('django.db.models.fields.TextField')(db_column=u'Nutr_No', blank=True)),
            ('datasrc_id', self.gf('django.db.models.fields.TextField')(db_column=u'DataSrc_ID', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['Datsrcln'])

        # Adding model 'DerivCd'
        db.create_table(u'deriv_cd', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('deriv_cd', self.gf('django.db.models.fields.TextField')(unique=True, db_column=u'Deriv_Cd', blank=True)),
            ('deriv_desc', self.gf('django.db.models.fields.TextField')(db_column=u'Deriv_Desc', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['DerivCd'])

        # Adding model 'FdGroup'
        db.create_table(u'fd_group', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('fdgrp_cd', self.gf('django.db.models.fields.TextField')(unique=True, db_column=u'FdGrp_Cd', blank=True)),
            ('fdgrp_desc', self.gf('django.db.models.fields.TextField')(db_column=u'FdGrp_Desc', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['FdGroup'])

        # Adding model 'FoodDes'
        db.create_table(u'food_des', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('ndb_no', self.gf('django.db.models.fields.TextField')(unique=True, db_column=u'NDB_No', blank=True)),
            ('fdgrp_cd', self.gf('django.db.models.fields.TextField')(db_column=u'FdGrp_Cd', blank=True)),
            ('long_desc', self.gf('django.db.models.fields.TextField')(db_column=u'Long_Desc', blank=True)),
            ('shrt_desc', self.gf('django.db.models.fields.TextField')(db_column=u'Shrt_Desc', blank=True)),
            ('comname', self.gf('django.db.models.fields.TextField')(db_column=u'ComName', blank=True)),
            ('manufacname', self.gf('django.db.models.fields.TextField')(db_column=u'ManufacName', blank=True)),
            ('survey', self.gf('django.db.models.fields.TextField')(db_column=u'Survey', blank=True)),
            ('ref_desc', self.gf('django.db.models.fields.TextField')(db_column=u'Ref_desc', blank=True)),
            ('refuse', self.gf('django.db.models.fields.TextField')(db_column=u'Refuse', blank=True)),
            ('sciname', self.gf('django.db.models.fields.TextField')(db_column=u'SciName', blank=True)),
            ('n_factor', self.gf('django.db.models.fields.TextField')(db_column=u'N_Factor', blank=True)),
            ('pro_factor', self.gf('django.db.models.fields.TextField')(db_column=u'Pro_Factor', blank=True)),
            ('fat_factor', self.gf('django.db.models.fields.TextField')(db_column=u'Fat_Factor', blank=True)),
            ('cho_factor', self.gf('django.db.models.fields.TextField')(db_column=u'CHO_Factor', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['FoodDes'])

        # Adding model 'Footnote'
        db.create_table(u'footnote', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('ndb_no', self.gf('django.db.models.fields.TextField')(db_column=u'NDB_No', blank=True)),
            ('footnt_no', self.gf('django.db.models.fields.TextField')(db_column=u'Footnt_No', blank=True)),
            ('footnt_typ', self.gf('django.db.models.fields.TextField')(db_column=u'Footnt_Typ', blank=True)),
            ('nutr_no', self.gf('django.db.models.fields.TextField')(db_column=u'Nutr_No', blank=True)),
            ('footnt_txt', self.gf('django.db.models.fields.TextField')(db_column=u'Footnt_Txt', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['Footnote'])

        # Adding model 'Langdesc'
        db.create_table(u'langdesc', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('factor_code', self.gf('django.db.models.fields.TextField')(db_column=u'Factor_Code', blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(db_column=u'Description', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['Langdesc'])

        # Adding model 'Langual'
        db.create_table(u'langual', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('ndb_no', self.gf('django.db.models.fields.TextField')(db_column=u'NDB_No', blank=True)),
            ('factor_code', self.gf('django.db.models.fields.TextField')(db_column=u'Factor_Code', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['Langual'])

        # Adding model 'NutData'
        db.create_table(u'nut_data', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('ndb_no', self.gf('django.db.models.fields.TextField')(db_column=u'NDB_No', blank=True)),
            ('nutr_no', self.gf('django.db.models.fields.TextField')(db_column=u'Nutr_No', blank=True)),
            ('nutr_val', self.gf('django.db.models.fields.TextField')(db_column=u'Nutr_Val', blank=True)),
            ('num_data_pts', self.gf('django.db.models.fields.TextField')(db_column=u'Num_Data_Pts', blank=True)),
            ('std_error', self.gf('django.db.models.fields.TextField')(db_column=u'Std_Error', blank=True)),
            ('src_cd', self.gf('django.db.models.fields.TextField')(db_column=u'Src_Cd', blank=True)),
            ('deriv_cd', self.gf('django.db.models.fields.TextField')(db_column=u'Deriv_Cd', blank=True)),
            ('ref_ndb_no', self.gf('django.db.models.fields.TextField')(db_column=u'Ref_NDB_No', blank=True)),
            ('add_nutr_mark', self.gf('django.db.models.fields.TextField')(db_column=u'Add_Nutr_Mark', blank=True)),
            ('num_studies', self.gf('django.db.models.fields.TextField')(db_column=u'Num_Studies', blank=True)),
            ('min', self.gf('django.db.models.fields.TextField')(db_column=u'Min', blank=True)),
            ('max', self.gf('django.db.models.fields.TextField')(db_column=u'Max', blank=True)),
            ('df', self.gf('django.db.models.fields.TextField')(db_column=u'DF', blank=True)),
            ('low_eb', self.gf('django.db.models.fields.TextField')(db_column=u'Low_EB', blank=True)),
            ('up_eb', self.gf('django.db.models.fields.TextField')(db_column=u'Up_EB', blank=True)),
            ('stat_cmt', self.gf('django.db.models.fields.TextField')(db_column=u'Stat_cmt', blank=True)),
            ('addmod_date', self.gf('django.db.models.fields.TextField')(db_column=u'AddMod_Date', blank=True)),
            ('cc', self.gf('django.db.models.fields.TextField')(db_column=u'CC', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['NutData'])

        # Adding model 'NutrDef'
        db.create_table(u'nutr_def', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nutr_no', self.gf('django.db.models.fields.TextField')(unique=True, db_column=u'Nutr_No', blank=True)),
            ('units', self.gf('django.db.models.fields.TextField')(db_column=u'Units', blank=True)),
            ('tagname', self.gf('django.db.models.fields.TextField')(db_column=u'Tagname', blank=True)),
            ('nutrdesc', self.gf('django.db.models.fields.TextField')(db_column=u'NutrDesc', blank=True)),
            ('num_dec', self.gf('django.db.models.fields.TextField')(db_column=u'Num_Dec', blank=True)),
            ('sr_order', self.gf('django.db.models.fields.TextField')(db_column=u'SR_Order', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['NutrDef'])

        # Adding model 'SrcCd'
        db.create_table(u'src_cd', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('src_cd', self.gf('django.db.models.fields.TextField')(unique=True, db_column=u'Src_Cd', blank=True)),
            ('srccd_desc', self.gf('django.db.models.fields.TextField')(db_column=u'SrcCd_Desc', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['SrcCd'])

        # Adding model 'Weight'
        db.create_table(u'weight', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('ndb_no', self.gf('django.db.models.fields.TextField')(db_column=u'NDB_No', blank=True)),
            ('seq', self.gf('django.db.models.fields.TextField')(db_column=u'Seq', blank=True)),
            ('amount', self.gf('django.db.models.fields.TextField')(db_column=u'Amount', blank=True)),
            ('msre_desc', self.gf('django.db.models.fields.TextField')(db_column=u'Msre_Desc', blank=True)),
            ('gm_wgt', self.gf('django.db.models.fields.TextField')(db_column=u'Gm_Wgt', blank=True)),
            ('num_data_pts', self.gf('django.db.models.fields.TextField')(db_column=u'Num_Data_Pts', blank=True)),
            ('std_dev', self.gf('django.db.models.fields.TextField')(db_column=u'Std_Dev', blank=True)),
        ))
        db.send_create_signal(u'recipeprintoutsapp', ['Weight'])


    def backwards(self, orm):
        # Deleting model 'DataSrc'
        db.delete_table(u'data_src')

        # Deleting model 'Datsrcln'
        db.delete_table(u'datsrcln')

        # Deleting model 'DerivCd'
        db.delete_table(u'deriv_cd')

        # Deleting model 'FdGroup'
        db.delete_table(u'fd_group')

        # Deleting model 'FoodDes'
        db.delete_table(u'food_des')

        # Deleting model 'Footnote'
        db.delete_table(u'footnote')

        # Deleting model 'Langdesc'
        db.delete_table(u'langdesc')

        # Deleting model 'Langual'
        db.delete_table(u'langual')

        # Deleting model 'NutData'
        db.delete_table(u'nut_data')

        # Deleting model 'NutrDef'
        db.delete_table(u'nutr_def')

        # Deleting model 'SrcCd'
        db.delete_table(u'src_cd')

        # Deleting model 'Weight'
        db.delete_table(u'weight')


    models = {
        u'recipeprintoutsapp.datasrc': {
            'Meta': {'object_name': 'DataSrc', 'db_table': "u'data_src'"},
            'authors': ('django.db.models.fields.TextField', [], {'db_column': "u'Authors'", 'blank': 'True'}),
            'datasrc_id': ('django.db.models.fields.TextField', [], {'unique': 'True', 'db_column': "u'DataSrc_ID'", 'blank': 'True'}),
            'end_page': ('django.db.models.fields.TextField', [], {'db_column': "u'End_Page'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'issue_state': ('django.db.models.fields.TextField', [], {'db_column': "u'Issue_State'", 'blank': 'True'}),
            'journal': ('django.db.models.fields.TextField', [], {'db_column': "u'Journal'", 'blank': 'True'}),
            'start_page': ('django.db.models.fields.TextField', [], {'db_column': "u'Start_Page'", 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "u'Title'", 'blank': 'True'}),
            'vol_city': ('django.db.models.fields.TextField', [], {'db_column': "u'Vol_City'", 'blank': 'True'}),
            'year': ('django.db.models.fields.TextField', [], {'db_column': "u'Year'", 'blank': 'True'})
        },
        u'recipeprintoutsapp.datsrcln': {
            'Meta': {'object_name': 'Datsrcln', 'db_table': "u'datsrcln'"},
            'datasrc_id': ('django.db.models.fields.TextField', [], {'db_column': "u'DataSrc_ID'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'ndb_no': ('django.db.models.fields.TextField', [], {'db_column': "u'NDB_No'", 'blank': 'True'}),
            'nutr_no': ('django.db.models.fields.TextField', [], {'db_column': "u'Nutr_No'", 'blank': 'True'})
        },
        u'recipeprintoutsapp.derivcd': {
            'Meta': {'object_name': 'DerivCd', 'db_table': "u'deriv_cd'"},
            'deriv_cd': ('django.db.models.fields.TextField', [], {'unique': 'True', 'db_column': "u'Deriv_Cd'", 'blank': 'True'}),
            'deriv_desc': ('django.db.models.fields.TextField', [], {'db_column': "u'Deriv_Desc'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'recipeprintoutsapp.fdgroup': {
            'Meta': {'object_name': 'FdGroup', 'db_table': "u'fd_group'"},
            'fdgrp_cd': ('django.db.models.fields.TextField', [], {'unique': 'True', 'db_column': "u'FdGrp_Cd'", 'blank': 'True'}),
            'fdgrp_desc': ('django.db.models.fields.TextField', [], {'db_column': "u'FdGrp_Desc'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'recipeprintoutsapp.fooddes': {
            'Meta': {'object_name': 'FoodDes', 'db_table': "u'food_des'"},
            'cho_factor': ('django.db.models.fields.TextField', [], {'db_column': "u'CHO_Factor'", 'blank': 'True'}),
            'comname': ('django.db.models.fields.TextField', [], {'db_column': "u'ComName'", 'blank': 'True'}),
            'fat_factor': ('django.db.models.fields.TextField', [], {'db_column': "u'Fat_Factor'", 'blank': 'True'}),
            'fdgrp_cd': ('django.db.models.fields.TextField', [], {'db_column': "u'FdGrp_Cd'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'long_desc': ('django.db.models.fields.TextField', [], {'db_column': "u'Long_Desc'", 'blank': 'True'}),
            'manufacname': ('django.db.models.fields.TextField', [], {'db_column': "u'ManufacName'", 'blank': 'True'}),
            'n_factor': ('django.db.models.fields.TextField', [], {'db_column': "u'N_Factor'", 'blank': 'True'}),
            'ndb_no': ('django.db.models.fields.TextField', [], {'unique': 'True', 'db_column': "u'NDB_No'", 'blank': 'True'}),
            'pro_factor': ('django.db.models.fields.TextField', [], {'db_column': "u'Pro_Factor'", 'blank': 'True'}),
            'ref_desc': ('django.db.models.fields.TextField', [], {'db_column': "u'Ref_desc'", 'blank': 'True'}),
            'refuse': ('django.db.models.fields.TextField', [], {'db_column': "u'Refuse'", 'blank': 'True'}),
            'sciname': ('django.db.models.fields.TextField', [], {'db_column': "u'SciName'", 'blank': 'True'}),
            'shrt_desc': ('django.db.models.fields.TextField', [], {'db_column': "u'Shrt_Desc'", 'blank': 'True'}),
            'survey': ('django.db.models.fields.TextField', [], {'db_column': "u'Survey'", 'blank': 'True'})
        },
        u'recipeprintoutsapp.footnote': {
            'Meta': {'object_name': 'Footnote', 'db_table': "u'footnote'"},
            'footnt_no': ('django.db.models.fields.TextField', [], {'db_column': "u'Footnt_No'", 'blank': 'True'}),
            'footnt_txt': ('django.db.models.fields.TextField', [], {'db_column': "u'Footnt_Txt'", 'blank': 'True'}),
            'footnt_typ': ('django.db.models.fields.TextField', [], {'db_column': "u'Footnt_Typ'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'ndb_no': ('django.db.models.fields.TextField', [], {'db_column': "u'NDB_No'", 'blank': 'True'}),
            'nutr_no': ('django.db.models.fields.TextField', [], {'db_column': "u'Nutr_No'", 'blank': 'True'})
        },
        u'recipeprintoutsapp.langdesc': {
            'Meta': {'object_name': 'Langdesc', 'db_table': "u'langdesc'"},
            'description': ('django.db.models.fields.TextField', [], {'db_column': "u'Description'", 'blank': 'True'}),
            'factor_code': ('django.db.models.fields.TextField', [], {'db_column': "u'Factor_Code'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'recipeprintoutsapp.langual': {
            'Meta': {'object_name': 'Langual', 'db_table': "u'langual'"},
            'factor_code': ('django.db.models.fields.TextField', [], {'db_column': "u'Factor_Code'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'ndb_no': ('django.db.models.fields.TextField', [], {'db_column': "u'NDB_No'", 'blank': 'True'})
        },
        u'recipeprintoutsapp.nutdata': {
            'Meta': {'object_name': 'NutData', 'db_table': "u'nut_data'"},
            'add_nutr_mark': ('django.db.models.fields.TextField', [], {'db_column': "u'Add_Nutr_Mark'", 'blank': 'True'}),
            'addmod_date': ('django.db.models.fields.TextField', [], {'db_column': "u'AddMod_Date'", 'blank': 'True'}),
            'cc': ('django.db.models.fields.TextField', [], {'db_column': "u'CC'", 'blank': 'True'}),
            'deriv_cd': ('django.db.models.fields.TextField', [], {'db_column': "u'Deriv_Cd'", 'blank': 'True'}),
            'df': ('django.db.models.fields.TextField', [], {'db_column': "u'DF'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'low_eb': ('django.db.models.fields.TextField', [], {'db_column': "u'Low_EB'", 'blank': 'True'}),
            'max': ('django.db.models.fields.TextField', [], {'db_column': "u'Max'", 'blank': 'True'}),
            'min': ('django.db.models.fields.TextField', [], {'db_column': "u'Min'", 'blank': 'True'}),
            'ndb_no': ('django.db.models.fields.TextField', [], {'db_column': "u'NDB_No'", 'blank': 'True'}),
            'num_data_pts': ('django.db.models.fields.TextField', [], {'db_column': "u'Num_Data_Pts'", 'blank': 'True'}),
            'num_studies': ('django.db.models.fields.TextField', [], {'db_column': "u'Num_Studies'", 'blank': 'True'}),
            'nutr_no': ('django.db.models.fields.TextField', [], {'db_column': "u'Nutr_No'", 'blank': 'True'}),
            'nutr_val': ('django.db.models.fields.TextField', [], {'db_column': "u'Nutr_Val'", 'blank': 'True'}),
            'ref_ndb_no': ('django.db.models.fields.TextField', [], {'db_column': "u'Ref_NDB_No'", 'blank': 'True'}),
            'src_cd': ('django.db.models.fields.TextField', [], {'db_column': "u'Src_Cd'", 'blank': 'True'}),
            'stat_cmt': ('django.db.models.fields.TextField', [], {'db_column': "u'Stat_cmt'", 'blank': 'True'}),
            'std_error': ('django.db.models.fields.TextField', [], {'db_column': "u'Std_Error'", 'blank': 'True'}),
            'up_eb': ('django.db.models.fields.TextField', [], {'db_column': "u'Up_EB'", 'blank': 'True'})
        },
        u'recipeprintoutsapp.nutrdef': {
            'Meta': {'object_name': 'NutrDef', 'db_table': "u'nutr_def'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'num_dec': ('django.db.models.fields.TextField', [], {'db_column': "u'Num_Dec'", 'blank': 'True'}),
            'nutr_no': ('django.db.models.fields.TextField', [], {'unique': 'True', 'db_column': "u'Nutr_No'", 'blank': 'True'}),
            'nutrdesc': ('django.db.models.fields.TextField', [], {'db_column': "u'NutrDesc'", 'blank': 'True'}),
            'sr_order': ('django.db.models.fields.TextField', [], {'db_column': "u'SR_Order'", 'blank': 'True'}),
            'tagname': ('django.db.models.fields.TextField', [], {'db_column': "u'Tagname'", 'blank': 'True'}),
            'units': ('django.db.models.fields.TextField', [], {'db_column': "u'Units'", 'blank': 'True'})
        },
        u'recipeprintoutsapp.srccd': {
            'Meta': {'object_name': 'SrcCd', 'db_table': "u'src_cd'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'src_cd': ('django.db.models.fields.TextField', [], {'unique': 'True', 'db_column': "u'Src_Cd'", 'blank': 'True'}),
            'srccd_desc': ('django.db.models.fields.TextField', [], {'db_column': "u'SrcCd_Desc'", 'blank': 'True'})
        },
        u'recipeprintoutsapp.weight': {
            'Meta': {'object_name': 'Weight', 'db_table': "u'weight'"},
            'amount': ('django.db.models.fields.TextField', [], {'db_column': "u'Amount'", 'blank': 'True'}),
            'gm_wgt': ('django.db.models.fields.TextField', [], {'db_column': "u'Gm_Wgt'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'msre_desc': ('django.db.models.fields.TextField', [], {'db_column': "u'Msre_Desc'", 'blank': 'True'}),
            'ndb_no': ('django.db.models.fields.TextField', [], {'db_column': "u'NDB_No'", 'blank': 'True'}),
            'num_data_pts': ('django.db.models.fields.TextField', [], {'db_column': "u'Num_Data_Pts'", 'blank': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {'db_column': "u'Seq'", 'blank': 'True'}),
            'std_dev': ('django.db.models.fields.TextField', [], {'db_column': "u'Std_Dev'", 'blank': 'True'})
        }
    }

    complete_apps = ['recipeprintoutsapp']