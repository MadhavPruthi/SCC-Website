# Generated by Django 3.0 on 2019-12-12 08:32

from django.db import migrations, models
import response.models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0002_auto_20191212_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponse',
            name='response_id',
            field=models.CharField(default=response.models.generate_random_string, editable=False, max_length=12, primary_key=True, serialize=False),
        ),
    ]