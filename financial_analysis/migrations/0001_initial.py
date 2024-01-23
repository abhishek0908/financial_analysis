# Generated by Django 4.1.5 on 2024-01-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialAnalysisResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_revenue_5cr_flag', models.IntegerField()),
                ('borrowing_to_revenue_flag', models.IntegerField()),
                ('iscr_flag', models.IntegerField()),
            ],
        ),
    ]