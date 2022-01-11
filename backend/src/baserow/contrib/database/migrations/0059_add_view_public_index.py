# Generated by Django 3.2.6 on 2022-01-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0058_fix_hanging_formula_field_metadata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="view",
            name="public",
            field=models.BooleanField(
                db_index=True,
                default=False,
                help_text="Indicates whether the view is publicly accessible to "
                "visitors.",
            ),
        ),
    ]
