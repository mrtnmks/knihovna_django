from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse



class Autor(models.Model):
    idautor = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=45)
    prijmeni = models.CharField(max_length=45)
    zivotopis = models.TextField(blank=True, null=True)



class AutorHasKniha(models.Model):
    autor_idautor = models.OneToOneField(Autor, models.DO_NOTHING, db_column='autor_idautor', primary_key=True)
    kniha_idkniha = models.ForeignKey('Kniha', models.DO_NOTHING, db_column='kniha_idkniha')

    class Meta:
        unique_together = (('autor_idautor', 'kniha_idkniha'),)


class Ctenar(models.Model):
    idctenar = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=45)
    prijmeni = models.CharField(max_length=45)



class Kniha(models.Model):
    idkniha = models.AutoField(primary_key=True)
    isbn = models.CharField(unique=True, max_length=30, blank=True, null=True)
    titul = models.CharField(max_length=100)
    jazyk = models.CharField(max_length=10, blank=True, null=True)
    cena = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    obsah = models.TextField(blank=True, null=True)
    strany = models.PositiveIntegerField(blank=True, null=True)
    zanr = models.CharField(max_length=25, blank=True, null=True)
    vydavatelstvi_idvydavatelstvi = models.ForeignKey('Vydavatelstvi', models.DO_NOTHING, db_column='vydavatelstvi_idvydavatelstvi')
    vypujcka_idvypujcka = models.ForeignKey('Vypujcka', models.DO_NOTHING, db_column='Vypujcka_idVypujcka')



class Vydavatelstvi(models.Model):
    idvydavatelstvi = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=45)



class Vypujcka(models.Model):
    idvypujcka = models.AutoField(db_column='idVypujcka', primary_key=True)
    datumvypujcky = models.DateField(db_column='DatumVypujcky')
    datumvraceni = models.DateField(db_column='DatumVraceni', blank=True, null=True)
    ctenar_idctenar = models.ForeignKey(Ctenar, models.DO_NOTHING, db_column='Ctenar_idctenar')
