# Generated by Django 2.1.7 on 2019-03-31 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20190331_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issueinfo',
            name='Loacation',
        ),
        migrations.RemoveField(
            model_name='issueinfo',
            name='MachineModelName',
        ),
        migrations.AlterField(
            model_name='issueinfo',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='polls.customer'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Machine',
        ),
    ]