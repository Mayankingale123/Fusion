# Generated by Django 3.1.5 on 2021-05-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establishment', '0009_auto_20210509_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='appraisal',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appraisal',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appraisal',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected'), ('outstanding', 'Outstanding'), ('excellant', 'Excellant'), ('very good', 'Very Good'), ('good', 'Good'), ('poor', 'Poor')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='appraisalrequest',
            name='status_director',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected'), ('outstanding', 'Outstanding'), ('excellant', 'Excellant'), ('very good', 'Very Good'), ('good', 'Good'), ('poor', 'Poor')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='appraisalrequest',
            name='status_hod',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected'), ('outstanding', 'Outstanding'), ('excellant', 'Excellant'), ('very good', 'Very Good'), ('good', 'Good'), ('poor', 'Poor')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='cpda_application',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected'), ('outstanding', 'Outstanding'), ('excellant', 'Excellant'), ('very good', 'Very Good'), ('good', 'Good'), ('poor', 'Poor')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ltc_application',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected'), ('outstanding', 'Outstanding'), ('excellant', 'Excellant'), ('very good', 'Very Good'), ('good', 'Good'), ('poor', 'Poor')], max_length=20, null=True),
        ),
    ]