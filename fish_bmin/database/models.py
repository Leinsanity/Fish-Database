from django.db import models
from datetime import datetime
# from author.decorators import with_author, updated_by
from django.contrib.auth.models import User
from numpy import identity

class Locations(models.Model):
    location = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    gps = models.CharField(max_length=50)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = "Locations"

class Collection_Date(models.Model):
    collection_date = models.DateField(default=datetime.now, help_text='Enter collection date')

    def __str__(self):
        return str(self.collection_date)

    class Meta:
        verbose_name_plural = "Collection Dates"

class Preparation1(models.Model):
    preparation = models.CharField(max_length=50)

    def __str__(self):
        return self.preparation

    class Meta:
        verbose_name_plural = "Preparation 1"

class Preparation2(models.Model):
    preparation = models.CharField(max_length=50)

    def __str__(self):
        return self.preparation

    class Meta:
        verbose_name_plural = "Preparation 2"

class Tissue(models.Model):
    tissue = models.CharField(max_length=100)

    def __str__(self):
        return self.tissue

    class Meta:
        verbose_name_plural = "Tissue"        

class Family(models.Model):
    family = models.CharField(max_length=50)

    def __str__(self):
        return self.family

    class Meta:
        verbose_name_plural = "Family"  

class Identifier(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Identifiers"     

class Collector(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Collectors"       

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Photographers"          

class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "Status"   

class Specimen(models.Model):
    collection_code = models.CharField(max_length=50, unique=True, help_text='Enter complete collection code')
    collection_date = models.ForeignKey(Collection_Date, on_delete=models.CASCADE)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, help_text='Select appropriate family')
    
    identifer = models.ForeignKey(Identifier, on_delete=models.CASCADE, null=False)
    initial_ID = models.CharField(max_length=50, null=False, default="")
    final_ID = models.CharField(max_length=50, null=False, default="")

    preparation_1 = models.ForeignKey(Preparation1, on_delete=models.CASCADE)
    preparation_2 = models.ForeignKey(Preparation2, on_delete=models.CASCADE)
    tissue = models.ForeignKey(Tissue, default=None, null=True, on_delete=models.CASCADE)

    
    collector = models.ManyToManyField(Collector)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=False, default="Encoded")
    dna_barcode = models.TextField(max_length = 700, blank=True, default="")

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # last_updated = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.collection_code

    class Meta:
        verbose_name_plural = "Specimens"

class Results(models.Model):
    initial = models.CharField(max_length=50, default="")
    collection_code = models.CharField(max_length=50)
    identity = models.TextField()

    def __str__(self):
        return self.collection_code

    class Meta:
        verbose_name_plural = "Results"

class Resultss(models.Model):
    initial = models.CharField(max_length=50, default="")
    collection_code = models.CharField(max_length=50)
    identity = models.FloatField()
    location = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.collection_code

    class Meta:
        verbose_name_plural = "Resultss"

