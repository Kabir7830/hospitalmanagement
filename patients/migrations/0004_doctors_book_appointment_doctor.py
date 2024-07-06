# Generated by Django 4.0.6 on 2023-04-22 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_remove_doctors_department_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('specialization', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='book_appointment',
            name='doctor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='patients.doctors'),
            preserve_default=False,
        ),
    ]