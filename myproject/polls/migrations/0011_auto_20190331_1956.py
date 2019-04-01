# Generated by Django 2.1.7 on 2019-03-31 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20190331_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='issueinfo',
            name='Loacation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='polls.Location'),
        ),
        migrations.AddField(
            model_name='issueinfo',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issueinfo',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='polls.customer'),
        ),
        migrations.AlterUniqueTogether(
            name='issueinfo',
            unique_together={('customer', 'Loacation')},
        ),
    ]