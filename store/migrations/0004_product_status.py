# Generated by Django 4.1.5 on 2023-02-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_alter_product_options_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("waitingapproval", "Waitinga approval"),
                    ("active", "Active"),
                    ("deleted", "Deleted"),
                ],
                default="active",
                max_length=50,
            ),
        ),
    ]