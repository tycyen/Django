# Generated by Django 2.1.7 on 2019-03-31 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20190331_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueinfo',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='polls.customer'),
        ),
    ]
