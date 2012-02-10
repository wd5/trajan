# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Beer.location'
        db.add_column('brew_beer', 'location', self.gf('django.db.models.fields.related.ForeignKey')(default='1', to=orm['newsfeed.Location']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Beer.location'
        db.delete_column('brew_beer', 'location_id')


    models = {
        'brew.beer': {
            'Meta': {'object_name': 'Beer'},
            'abv': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'final_gravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'ibu': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['newsfeed.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'original_gravity': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'newsfeed.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['brew']
