from django.db import models

# Create your models here.
class Teks(models.Model):
    teks_id = models.AutoField(primary_key=True)
    teks = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.teks}"
    
class Preprocessing(models.Model):
    teks_id = models.ForeignKey(Teks, on_delete=models.CASCADE, null=True, blank=True)
    case_folding = models.TextField(null=True, blank=True)
    tokenisasi = models.TextField(null=True, blank=True)
    stopword_removal = models.TextField(null=True, blank=True)
    slangword_removal = models.TextField(null=True, blank=True)
    stemming = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.teks_id}"
    
class Stopword(models.Model):
    stopword_id = models.AutoField(primary_key=True)
    kata = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.kata}"

class Slangword(models.Model):
    slangword_id = models.AutoField(primary_key=True)
    kata = models.TextField(null=True, blank=True)
    kata_baku = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.kata}"
    
