from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class autor(models.Model):
    jmeno = models.CharField(max_length=30, null=False, blank=False, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=30, verbose_name="Přijmení", blank=False, null=True)
    narozeni = models.DateTimeField(verbose_name="Narození")
    zivotopis = models.TextField(verbose_name="Životopis autora")

    class Meta:
        ordering = ["jmeno", "-narozeni"]

    def __str__(self):
        return self.jmeno

class ctenar(models.Model):
    jmeno = models.CharField(max_length=30, null=False, blank=False, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=30, verbose_name="Přijmení", blank=False, null=True)
    narozeni = models.DateTimeField(verbose_name="Narození")

    class Meta:
        ordering = ["jmeno", "-narozeni"]

    def __str__(self):
        return self.jmeno

class kniha(models.Model):
    isbn = models.CharField(max_length=30, verbose_name="ISBN knihy")
    titul = models.CharField(max_length=100 , null=False, blank=False, verbose_name="Název díla")
    zanr = models.CharField(max_length=30, verbose_name="Žánr", blank=False, null=False)
    vydani = models.DateTimeField(verbose_name="Datum vydání knihy")
    obsah = models.TextField(verbose_name="Obsah knihy")



    class Meta:
        ordering = ["-vydani", "titul"]

    def __str__(self):
        return self.titul

