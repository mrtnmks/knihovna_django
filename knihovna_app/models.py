from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

def letosni_rok():
    return datetime.date.today().year

def attachment_path(instance, filename):
    return "kniha/" + str(instance.file) + "/attachments/" + filename

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

class Priloha(models.Model):
     title = models.CharField(max_length=200, verbose_name="Title")
     last_update = models.DateTimeField(auto_now=True)
     file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")

     TYPE_OF_ATTACHMENT = (
     ('Obal', 'Obal'),
     ('Video', 'Video'),
     ('Jiné', 'Jiné'),
     )

     type = models.CharField(max_length=5, choices= TYPE_OF_ATTACHMENT, default='Obal', help_text='Vyber povolenou přílohu', verbose_name="Typ přílohy")

class Kniha(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=30, verbose_name="ISBN knihy")
    titul = models.CharField(max_length=100 , null=False, blank=False, verbose_name="Název díla")
    zanr = models.CharField(max_length=30, verbose_name="Žánr", blank=False, null=False)
    hodnoceni = models.FloatField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)], null=True,
                               help_text="Od 1 do 10", verbose_name="Hodnoceni")
    vydani = models.PositiveIntegerField(verbose_name="Vydání", default=letosni_rok(), validators=[MinValueValidator(1800), maximalni_rok])
    obsah = models.TextField(verbose_name="Obsah knihy", default='')
    obal = models.ImageField(upload_to='kniha/obal/%Y/%m/%d/', blank=True, null=True, verbose_name="Obal")
    priloha = models.ForeignKey(Priloha, on_delete=models.CASCADE, null=True)
    ctenar = models.ForeignKey(Ctenar, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


    class Meta:
        ordering = ["-vydani", "titul"]

    def __str__(self):
        return self.titul



