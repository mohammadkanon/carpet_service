# Generated by Django 2.2.1 on 2019-06-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SndWall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snd_img', models.ImageField(upload_to='f_wall')),
                ('snd_content', models.CharField(blank=True, max_length=100, null=True)),
                ('snd_description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
