# Generated by Django 5.0.6 on 2024-05-08 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_providers_google_workspace", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="googleworkspaceprovidergroup",
            options={
                "verbose_name": "Google Workspace Provider Group",
                "verbose_name_plural": "Google Workspace Provider Groups",
            },
        ),
        migrations.AlterModelOptions(
            name="googleworkspaceprovideruser",
            options={
                "verbose_name": "Google Workspace Provider User",
                "verbose_name_plural": "Google Workspace Provider Users",
            },
        ),
    ]
