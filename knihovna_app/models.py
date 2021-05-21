from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

def letosni_rok():
    return datetime.date.today().year

def attachment_path(instance, filename):
    return "kniha/" + str(instance.soubor) + "/attachments/" + filename

def maximalni_rok(hodnota):
    return MaxValueValidator(letosni_rok())(hodnota)

class Autor(models.Model):
    jmeno = models.CharField(max_length=30, null=False, blank=False, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=30, verbose_name="Přijmení", blank=False, null=True)
    narozeni = models.DateField(blank=True, null=True,
                                    help_text="Zadejte datum narození",
                                    verbose_name="Datum narození")
    zivotopis = models.TextField(verbose_name="Životopis autora", default='')

    class Meta:
        ordering = ["jmeno", "-narozeni"]

    def __str__(self):
        return self.prijmeni


class Zanr(models.Model):
    nazev = models.CharField(max_length=25, null=False,  unique=True, verbose_name="Název žánru", help_text='Zadej název žánru')

    class Meta:
        ordering = ["nazev"]


    def __str__(self):
        return self.nazev

    def pocet_knih(self, obj):
        return obj.kniha_set.count()

class Kniha(models.Model):
    isbn = models.CharField(max_length=30, verbose_name="ISBN knihy")
    titul = models.CharField(max_length=100 , null=False, blank=False, verbose_name="Název díla")
    zanr = models.ManyToManyField(Zanr, help_text='Vyber žánry knihy')
    strany = models.IntegerField(blank=True, null=True, help_text="Zadejte počet stránek díla", verbose_name="Počet stránek")
    hodnoceni = models.FloatField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)], null=True, help_text="Od 1 do 10", verbose_name="Hodnocení")
    vydani = models.DateField(blank=True, null=True,
                                    help_text="Zadejte datum vydání",
                                    verbose_name="Datum vydání")
    obsah = models.TextField(verbose_name="Obsah knihy", default='')
    obal = models.ImageField(upload_to='kniha/obal/%Y/%m/%d/', blank=True, null=True, verbose_name="Obal")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


    class Meta:
        ordering = ["-vydani", "titul"]

    def __str__(self):
        return f"{self.titul}, year: {str(self.vydani.year)}, rate: {str(self.hodnoceni)}"

    def get_absolute_url(self):
        return reverse('kniha-detail', args=[str(self.id)])

    def rok_vydani(self):
        return self.vydani.year


class Priloha(models.Model):
    titul = models.CharField(max_length=200, verbose_name="Titul")
    uprava = models.DateTimeField(auto_now=True)
    soubor = models.FileField(upload_to=attachment_path, null=True, verbose_name="Soubor")

    TYP_PRILOHY = (
        ('Audio', 'Audio'),
        ('Video', 'Video'),
        ('Text', 'Text'),
        ('Jiné', 'Jiné'),
    )

    typ = models.CharField(max_length=5, choices=TYP_PRILOHY, default='Image', help_text='Vyber povolenou přílohu',
                            verbose_name="Typ přílohy")
    kniha = models.ForeignKey(Kniha, on_delete=models.CASCADE, default='')

    class Meta:
        order_with_respect_to = 'kniha'

        def __str__(self):
            return f"{self.titul}, ({self.typ})"




