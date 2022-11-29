from django.db import models

# Create your models here.
class ModelProduct(models.Model):
      title = models.CharField(max_length=255)
      price = models.IntegerField()
      description = models.TextField()
      active = models.BooleanField(default=True)
      created = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.title

class Clients(models.Model):
      name = models.CharField(max_length=255, db_index=True)
      age = models.IntegerField()

      def __str__(self):
            return self.name
