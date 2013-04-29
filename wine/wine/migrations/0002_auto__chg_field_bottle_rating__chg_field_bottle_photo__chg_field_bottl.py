# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Bottle.rating'
        db.alter_column(u'wine_bottle', 'rating', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Bottle.photo'
        db.alter_column(u'wine_bottle', 'photo', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Bottle.price'
        db.alter_column(u'wine_bottle', 'price', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Winery.url'
        db.alter_column(u'wine_winery', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Winery.location'
        db.alter_column(u'wine_winery', 'location', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True))

        # Changing field 'Winery.address'
        db.alter_column(u'wine_winery', 'address', self.gf('django.db.models.fields.TextField')(null=True))
        # Adding field 'Wine.name'
        db.add_column(u'wine_wine', 'name',
                      self.gf('django.db.models.fields.TextField')(default='Wine'),
                      keep_default=False)


        # Changing field 'Wine.label_photo'
        db.alter_column(u'wine_wine', 'label_photo', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Wine.wine_type'
        db.alter_column(u'wine_wine', 'wine_type', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Wine.url'
        db.alter_column(u'wine_wine', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Wine.photo'
        db.alter_column(u'wine_wine', 'photo', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Wine.min_price'
        db.alter_column(u'wine_wine', 'min_price', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Wine.vintage'
        db.alter_column(u'wine_wine', 'vintage', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Wine.retail_price'
        db.alter_column(u'wine_wine', 'retail_price', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Wine.max_price'
        db.alter_column(u'wine_wine', 'max_price', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Cellar.photo'
        db.alter_column(u'wine_cellar', 'photo', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Bottle.rating'
        raise RuntimeError("Cannot reverse this migration. 'Bottle.rating' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Bottle.photo'
        raise RuntimeError("Cannot reverse this migration. 'Bottle.photo' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Bottle.price'
        raise RuntimeError("Cannot reverse this migration. 'Bottle.price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Winery.url'
        raise RuntimeError("Cannot reverse this migration. 'Winery.url' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Winery.location'
        raise RuntimeError("Cannot reverse this migration. 'Winery.location' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Winery.address'
        raise RuntimeError("Cannot reverse this migration. 'Winery.address' and its values cannot be restored.")
        # Deleting field 'Wine.name'
        db.delete_column(u'wine_wine', 'name')


        # User chose to not deal with backwards NULL issues for 'Wine.label_photo'
        raise RuntimeError("Cannot reverse this migration. 'Wine.label_photo' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Wine.wine_type'
        raise RuntimeError("Cannot reverse this migration. 'Wine.wine_type' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Wine.url'
        raise RuntimeError("Cannot reverse this migration. 'Wine.url' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Wine.photo'
        raise RuntimeError("Cannot reverse this migration. 'Wine.photo' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Wine.min_price'
        raise RuntimeError("Cannot reverse this migration. 'Wine.min_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Wine.vintage'
        raise RuntimeError("Cannot reverse this migration. 'Wine.vintage' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Wine.retail_price'
        raise RuntimeError("Cannot reverse this migration. 'Wine.retail_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Wine.max_price'
        raise RuntimeError("Cannot reverse this migration. 'Wine.max_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Cellar.photo'
        raise RuntimeError("Cannot reverse this migration. 'Cellar.photo' and its values cannot be restored.")

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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.TextField', [], {})
        },
        u'wine.wine': {
            'Meta': {'object_name': 'Wine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_photo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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