# Generated by Django 2.1.7 on 2019-03-31 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20190331_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issueinfo',
            old_name='IssueDescribe',
            new_name='Issue_Describe',
        ),
        migrations.RenameField(
            model_name='issueinfo',
            old_name='IssueTopic',
            new_name='Issue_Topic',
        ),
        migrations.RenameField(
            model_name='issueinfo',
            old_name='MachineJamStatus',
            new_name='Machine_Jam_Status',
        ),
        migrations.RenameField(
            model_name='issueinfo',
            old_name='MachineModelName',
            new_name='Machine_Model_Name',
        ),
    ]
