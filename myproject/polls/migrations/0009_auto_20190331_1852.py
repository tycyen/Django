# Generated by Django 2.1.7 on 2019-03-31 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190331_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issueinfo',
            old_name='MachineID',
            new_name='mach_cust_id',
        ),
        migrations.AlterField(
            model_name='issueinfo',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='polls.customer'),
        ),
    ]
