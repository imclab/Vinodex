# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Wine.label_photo'
        db.alter_column(u'wine_wine', 'label_photo', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))
        # Deleting field 'UserProfile.email'
        db.delete_column(u'wine_userprofile', 'email')


    def backwards(self, orm):

        # Changing field 'Wine.label_photo'
        db.alter_column(u'wine_wine', 'label_photo', self.gf('django.db.models.fields.TextField')(null=True))

        # User chose to not deal with backwards NULL issues for 'UserProfile.email'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.email' and its values cannot be restored.")

    models = {
        u'wine.annotation': {
            'Meta': {'object_name': 'Annotation'},
            'bottle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wine.Bottle']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.TextField', [], {}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'wine.bottle': {
            'Meta': {'object_name': 'Bottle'},
            'cellar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wine.Cellar']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wine.Wine']"})
        },
        u'wine.cellar': {
            'Meta': {'object_name': 'Cellar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wine.UserProfile']"}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'wine.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'avatar': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.TextField', [], {})
        },
        u'wine.wine': {
            'Meta': {'object_name': 'Wine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_photo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'max_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'retail_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'vintage': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wine_type': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'winery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wine.Winery']"})
        },
        u'wine.winery': {
            'Meta': {'object_name': 'Winery'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['wine']