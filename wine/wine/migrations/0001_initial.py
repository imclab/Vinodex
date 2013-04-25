# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'wine_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.TextField')()),
            ('password', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('first_name', self.gf('django.db.models.fields.TextField')()),
            ('last_name', self.gf('django.db.models.fields.TextField')()),
            ('avatar', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'wine', ['User'])

        # Adding model 'Winery'
        db.create_table(u'wine_winery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'wine', ['Winery'])

        # Adding model 'Cellar'
        db.create_table(u'wine_cellar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wine.User'])),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'wine', ['Cellar'])

        # Adding model 'Wine'
        db.create_table(u'wine_wine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.TextField')()),
            ('winery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wine.Winery'])),
            ('vintage', self.gf('django.db.models.fields.TextField')()),
            ('wine_type', self.gf('django.db.models.fields.TextField')()),
            ('min_price', self.gf('django.db.models.fields.IntegerField')()),
            ('max_price', self.gf('django.db.models.fields.IntegerField')()),
            ('retail_price', self.gf('django.db.models.fields.IntegerField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('label_photo', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'wine', ['Wine'])

        # Adding model 'Bottle'
        db.create_table(u'wine_bottle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wine.Wine'])),
            ('cellar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wine.Cellar'])),
            ('photo', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'wine', ['Bottle'])

        # Adding model 'Annotation'
        db.create_table(u'wine_annotation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bottle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wine.Bottle'])),
            ('key', self.gf('django.db.models.fields.TextField')()),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'wine', ['Annotation'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'wine_user')

        # Deleting model 'Winery'
        db.delete_table(u'wine_winery')

        # Deleting model 'Cellar'
        db.delete_table(u'wine_cellar')

        # Deleting model 'Wine'
        db.delete_table(u'wine_wine')

        # Deleting model 'Bottle'
        db.delete_table(u'wine_bottle')

        # Deleting model 'Annotation'
        db.delete_table(u'wine_annotation')


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
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'wine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wine.Wine']"})
        },
        u'wine.cellar': {
            'Meta': {'object_name': 'Cellar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wine.User']"}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'wine.user': {
            'Meta': {'object_name': 'User'},
            'avatar': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.TextField', [], {}),
            'password': ('django.db.models.fields.TextField', [], {}),
            'username': ('django.db.models.fields.TextField', [], {})
        },
        u'wine.wine': {
            'Meta': {'object_name': 'Wine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_photo': ('django.db.models.fields.TextField', [], {}),
            'max_price': ('django.db.models.fields.IntegerField', [], {}),
            'min_price': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.TextField', [], {}),
            'retail_price': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'vintage': ('django.db.models.fields.TextField', [], {}),
            'wine_type': ('django.db.models.fields.TextField', [], {}),
            'winery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wine.Winery']"})
        },
        u'wine.winery': {
            'Meta': {'object_name': 'Winery'},
            'address': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['wine']