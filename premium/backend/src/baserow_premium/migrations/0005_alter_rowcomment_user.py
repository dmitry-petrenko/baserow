# Generated by Django 3.2.12 on 2022-05-10 14:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("baserow_premium", "0004_kanbanview_card_cover_image_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rowcomment",
            name="user",
            field=models.ForeignKey(
                help_text="The user who made the comment.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]