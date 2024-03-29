from django.db import models
from django.core.files import File

def output_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/output_<id>/<filename>
    # obtenido de https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
    return 'output_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class Output(models.Model):
	start = models.DateTimeField(auto_now=False,auto_now_add=False)
	finish = models.DateTimeField(auto_now=False,auto_now_add=False)
	clean_layer = models.CharField(max_length = 500, null=False, blank=False)
	spd_tol = models.IntegerField()
	buffr = models.IntegerField()
	n_freq = models.IntegerField()
	n_points = models.IntegerField()
	d_gps = models.FileField(blank=True, upload_to='uploads/%Y_%m_%d/')
	d_res = models.FileField(blank=True, upload_to='uploads/%Y_%m_%d/')
	


	#def save_file(self):
	#	f = open('pages/salida.txt')
	#	file = File(f)
	#	self.root.save(str(self.id)+"salida.txt", file)
	#	f.close()


