from django.db import models

# kita akan membuat relasi antara tabel dan user bawaan django dengan biodata yang kita buat
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here

class Biodata(models.Model):
    #Cascada berarti ketika user kita delete maka biodatanya juga akan terhapus
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField(blank=True, null=True)
    telp = models.CharField(max_length=14, blank=True, null=True)
    nama = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.nama)

    #agar penulisan didashbord admin tidak ada penambahan s seoerti biodatas
    class Meta:
        verbose_name_plural ="Biodata"

class API(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username