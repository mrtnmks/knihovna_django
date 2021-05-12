# Generated by Django 3.2 on 2021-05-12 19:07

from django.db import migrations, models
import django.db.models.deletion
import knihovna_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('knihovna_app', '0003_auto_20210512_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priloha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(null=True, upload_to=knihovna_app.models.attachment_path, verbose_name='File')),
                ('type', models.CharField(choices=[('Obal', 'Obal'), ('Video', 'Video'), ('Jiné', 'Jiné')], default='Obal', help_text='Vyber povolenou přílohu', max_length=5, verbose_name='Typ přílohy')),
            ],
        ),
        migrations.RemoveField(
            model_name='kniha',
            name='attachment',
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
        migrations.AddField(
            model_name='kniha',
            name='priloha',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='knihovna_app.priloha'),
        ),
    ]