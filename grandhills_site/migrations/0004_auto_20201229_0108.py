# Generated by Django 3.1.3 on 2020-12-28 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grandhills_site', '0003_auto_20201228_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfor',
            name='company_addi_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]