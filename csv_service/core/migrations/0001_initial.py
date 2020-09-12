# Generated by Django 3.0.3 on 2020-09-01 01:52

import core.models.csv_model
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterprise_name', models.CharField(max_length=100, verbose_name='Enterprise Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('csv_file', models.FileField(upload_to='csvs', validators=[core.models.csv_model._validate_file_csv_extension], verbose_name='CSV')),
            ],
        ),
        migrations.AddConstraint(
            model_name='csvmodel',
            constraint=models.CheckConstraint(check=models.Q(enterprise_name__length__gt=0), name='csv_model_enterprise_name_length_greater_than_0'),
        ),
        migrations.AddConstraint(
            model_name='csvmodel',
            constraint=models.CheckConstraint(check=models.Q(enterprise_name__length__lte=100), name='csv_model_enterprise_name_title_length_less_or_equal_than_100'),
        ),
    ]