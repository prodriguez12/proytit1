from django.db import models
from django.core.files import File

def output_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/output_<id>/<filename>
    # obtenido de https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
    return 'output_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class Output(models.Model):
	root = models.FileField(blank=True, upload_to='uploads/')
	description = models.TextField(default='')

	def save_file(self):
		f = open('pages/salida.txt')
		file = File(f)
		self.root.save(str(self.id)+"salida.txt", file)
		f.close()


