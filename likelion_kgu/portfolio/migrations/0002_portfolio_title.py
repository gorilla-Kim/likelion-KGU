# Generated by Django 2.1.5 on 2019-02-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(default='제목을 입력해주세요.', max_length=125),
        ),
    ]
