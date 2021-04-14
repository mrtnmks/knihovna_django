from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

def letosni_rok():
    return datetime.date.today().year


def maximalni_rok(hodnota):
    return MaxValueValidator(letosni_rok())(hodnota)

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=30, null=False, blank=False, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=30, verbose_name="Přijmení", blank=False, null=True)
    narozeni = models.DateTimeField(verbose_name="Narození")
    zivotopis = models.TextField(verbose_name="Životopis autora", default='')

    class Meta:
        ordering = ["jmeno", "-narozeni"]

    def __str__(self):
        return self.prijmeni

class Ctenar(models.Model):
    id = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=30, null=False, blank=False, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=30, verbose_name="Přijmení", blank=False, null=True)
    narozeni = models.DateTimeField(verbose_name="Narození")

    class Meta:
        ordering = ["jmeno", "-narozeni"]

    def __str__(self):
        return self.prijmeni

class Kniha(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=30, verbose_name="ISBN knihy")
    titul = models.CharField(max_length=100 , null=False, blank=False, verbose_name="Název díla")
    zanr = models.CharField(max_length=30, verbose_name="Žánr", blank=False, null=False)
    vydani = models.PositiveIntegerField(verbose_name="Vydání", default=letosni_rok(), validators=[MinValueValidator(1800), maximalni_rok])
    obsah = models.TextField(verbose_name="Obsah knihy", default='')
    ctenar = models.ForeignKey(Ctenar, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


    class Meta:
        ordering = ["-vydani", "titul"]

    def __str__(self):
        return self.titul