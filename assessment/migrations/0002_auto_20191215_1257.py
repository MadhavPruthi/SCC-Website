# Generated by Django 3.0 on 2019-12-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='english_text',
            field=models.CharField(default='Question', max_length=200, verbose_name='Question(English)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='hindi_text',
            field=models.CharField(default='Hindi Question', max_length=200, verbose_name='Question(Hindi)'),
            preserve_default=False,
        ),
    ]
