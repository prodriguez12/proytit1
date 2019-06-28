from django.db import models

def input_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/input_<id>/<filename>
    # obtenido de https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
   return 'input_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class Input(models.Model):
	red_vial_layer = models.CharField(max_length = 500, null=False, blank=False)
	GPS_layer = models.CharField(max_length = 500, null=False, blank=False)
	gbd = models.FileField(blank=False, upload_to='uploads/%Y_%M_%d/')
	description = models.TextField(default='')
	gbd_root = models.CharField(max_length = 500)
	metrica = models.CharField(max_length =500, blank=False)		