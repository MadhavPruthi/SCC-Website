# Generated by Django 3.0 on 2019-12-12 08:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assessment.Choice')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assessment.Question')),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('response_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('dateTime', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField()),
                ('answers', models.ManyToManyField(to='response.Response')),
            ],
        ),
    ]
