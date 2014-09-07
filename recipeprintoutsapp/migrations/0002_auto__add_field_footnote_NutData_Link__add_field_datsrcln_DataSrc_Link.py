# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Footnote.NutData_Link'
        db.add_column(u'footnote', 'NutData_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.NutData'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Datsrcln.DataSrc_Link'
        db.add_column(u'datsrcln', 'DataSrc_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.DataSrc'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Langual.Langdesc_Link'
        db.add_column(u'langual', 'Langdesc_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.Langdesc'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'NutData.NutrDef_Link'
        db.add_column(u'nut_data', 'NutrDef_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.NutrDef'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'NutData.SrcCd_Link'
        db.add_column(u'nut_data', 'SrcCd_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.SrcCd'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'NutData.DerivCd_Link'
        db.add_column(u'nut_data', 'DerivCd_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.DerivCd'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'NutData.Datsrcln_Link'
        db.add_column(u'nut_data', 'Datsrcln_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.Datsrcln'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'FoodDes.FdGroup_Link'
        db.add_column(u'food_des', 'FdGroup_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.FdGroup'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'FoodDes.Footnote_Link'
        db.add_column(u'food_des', 'Footnote_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.Footnote'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'FoodDes.NutData_Link'
        db.add_column(u'food_des', 'NutData_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.NutData'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'FoodDes.Weight_Link'
        db.add_column(u'food_des', 'Weight_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.Weight'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'FoodDes.Langual_Link'
        db.add_column(u'food_des', 'Langual_Link',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipeprintoutsapp.Langual'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Footnote.NutData_Link'
        db.delete_column(u'footnote', 'NutData_Link_id')

        # Deleting field 'Datsrcln.DataSrc_Link'
        db.delete_column(u'datsrcln', 'DataSrc_Link_id')

        # Deleting field 'Langual.Langdesc_Link'
        db.delete_column(u'langual', 'Langdesc_Link_id')

        # Deleting field 'NutData.NutrDef_Link'
        db.delete_column(u'nut_data', 'NutrDef_Link_id')

        # Deleting field 'NutData.SrcCd_Link'
        db.delete_column(u'nut_data', 'SrcCd_Link_id')

        # Deleting field 'NutData.DerivCd_Link'
        db.delete_column(u'nut_data', 'DerivCd_Link_id')

        # Deleting field 'NutData.Datsrcln_Link'
        db.delete_column(u'nut_data', 'Datsrcln_Link_id')

        # Deleting field 'FoodDes.FdGroup_Link'
        db.delete_column(u'food_des', 'FdGroup_Link_id')

        # Deleting field 'FoodDes.Footnote_Link'
        db.delete_column(u'food_des', 'Footnote_Link_id')

        # Deleting field 'FoodDes.NutData_Link'
        db.delete_column(u'food_des', 'NutData_Link_id')

        # Deleting field 'FoodDes.Weight_Link'
        db.delete_column(u'food_des', 'Weight_Link_id')

        # Deleting field 'FoodDes.Langual_Link'
        db.delete_column(u'food_des', 'Langual_Link_id')


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
            'DataSrc_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.DataSrc']", 'null': 'True', 'blank': 'True'}),
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
            'FdGroup_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.FdGroup']", 'null': 'True', 'blank': 'True'}),
            'Footnote_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.Footnote']", 'null': 'True', 'blank': 'True'}),
            'Langual_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.Langual']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'FoodDes', 'db_table': "u'food_des'"},
            'NutData_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.NutData']", 'null': 'True', 'blank': 'True'}),
            'Weight_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.Weight']", 'null': 'True', 'blank': 'True'}),
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
            'NutData_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.NutData']", 'null': 'True', 'blank': 'True'}),
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
            'Langdesc_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.Langdesc']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Langual', 'db_table': "u'langual'"},
            'factor_code': ('django.db.models.fields.TextField', [], {'db_column': "u'Factor_Code'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'ndb_no': ('django.db.models.fields.TextField', [], {'db_column': "u'NDB_No'", 'blank': 'True'})
        },
        u'recipeprintoutsapp.nutdata': {
            'Datsrcln_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.Datsrcln']", 'null': 'True', 'blank': 'True'}),
            'DerivCd_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.DerivCd']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'NutData', 'db_table': "u'nut_data'"},
            'NutrDef_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.NutrDef']", 'null': 'True', 'blank': 'True'}),
            'SrcCd_Link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipeprintoutsapp.SrcCd']", 'null': 'True', 'blank': 'True'}),
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