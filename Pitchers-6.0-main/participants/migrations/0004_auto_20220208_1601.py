# Generated by Django 3.0.7 on 2022-02-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0003_auto_20220208_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preevent',
            name='Member1_roll_no',
            field=models.CharField(default='', help_text='Enter your Roll No. if you are studying in TIET otherwise enter your college name', max_length=100, verbose_name='Roll no/ College Name'),
        ),
        migrations.AlterField(
            model_name='preevent',
            name='Member2_are_you_a_thapar_student',
            field=models.BooleanField(blank=True, verbose_name='Are you a thapar student?'),
        ),
    ]
