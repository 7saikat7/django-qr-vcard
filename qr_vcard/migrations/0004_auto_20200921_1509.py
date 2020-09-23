# Generated by Django 3.1.1 on 2020-09-21 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_vcard', '0003_auto_20200916_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='vcard',
            name='logo',
            field=models.URLField(blank=True, default='', verbose_name='Logo'),
        ),
        migrations.AddField(
            model_name='vcard',
            name='organization',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Organization'),
        ),
        migrations.AlterUniqueTogether(
            name='vcard',
            unique_together={('name_first', 'name_last', 'organization')},
        ),
        migrations.RemoveField(
            model_name='vcard',
            name='image',
        ),
        migrations.RemoveField(
            model_name='vcard',
            name='title',
        ),
    ]