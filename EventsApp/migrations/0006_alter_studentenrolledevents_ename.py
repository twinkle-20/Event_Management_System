# Generated by Django 3.2.8 on 2022-02-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsApp', '0005_alter_studentenrolledevents_ename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentenrolledevents',
            name='EName',
            field=models.CharField(max_length=50),
        ),
    ]
