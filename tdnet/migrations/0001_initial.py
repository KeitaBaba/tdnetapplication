# Generated by Django 3.2.6 on 2021-10-14 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tekijikaiji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(blank=True, null=True)),
                ('company_name', models.TextField(blank=True, null=True)),
                ('company_title', models.TextField(blank=True, null=True)),
                ('pdf', models.TextField(blank=True, null=True)),
                ('disclosure_date', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
    ]