# Generated by Django 4.2.4 on 2023-08-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transactions", "0002_rename_track_id_transaction_pay_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="pay_id",
            field=models.CharField(max_length=255),
        ),
    ]
