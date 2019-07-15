# Generated by Django 2.2.1 on 2019-06-02 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20190602_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='customer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer'),
        ),
        migrations.AlterField(
            model_name='register',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]
