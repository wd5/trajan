# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Beer.abv'
        db.add_column('brew_beer', 'abv', self.gf('django.db.models.fields.DecimalField')(default='5.3', max_digits=5, decimal_places=2, blank=True), keep_default=False)

        # Adding field 'Beer.original_gravity'
        db.add_column('brew_beer', 'original_gravity', self.gf('django.db.models.fields.DecimalField')(default='1.012', max_digits=5, decimal_places=3, blank=True), keep_default=False)

        # Adding field 'Beer.final_gravity'
        db.add_column('brew_beer', 'final_gravity', self.gf('django.db.models.fields.DecimalField')(default='1.01', max_digits=5, decimal_places=3, blank=True), keep_default=False)

        # Adding field 'Beer.published'
        db.add_column('brew_beer', 'published', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Beer.abv'
        db.delete_column('brew_beer', 'abv')

        # Deleting field 'Beer.original_gravity'
        db.delete_column('brew_beer', 'original_gravity')

        # Deleting field 'Beer.final_gravity'
        db.delete_column('brew_beer', 'final_gravity')

        # Deleting field 'Beer.published'
        db.delete_column('brew_beer', 'published')


    models = {
        'brew.beer': {
            'Meta': {'object_name': 'Beer'},
            'abv': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'final_gravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'original_gravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['brew']
