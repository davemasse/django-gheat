# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Point'
        db.create_table('gheat_point', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(db_column='lat', blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(db_column='lng', blank=True)),
            ('modtime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('density', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('gheat', ['Point'])

        # Adding unique constraint on 'Point', fields ['uid']
        db.create_unique('gheat_point', ['uid'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Point', fields ['uid']
        db.delete_unique('gheat_point', ['uid'])

        # Deleting model 'Point'
        db.delete_table('gheat_point')


    models = {
        'gheat.point': {
            'Meta': {'unique_together': "(('uid',),)", 'object_name': 'Point'},
            'density': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'db_column': "'lat'", 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'db_column': "'lng'", 'blank': 'True'}),
            'modtime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['gheat']
