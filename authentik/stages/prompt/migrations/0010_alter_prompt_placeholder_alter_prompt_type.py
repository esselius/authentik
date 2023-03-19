# Generated by Django 4.1.7 on 2023-03-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_stages_prompt", "0009_prompt_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prompt",
            name="placeholder",
            field=models.TextField(
                blank=True,
                help_text="When creating a Radio Button Group or Dropdown, enable interpreting as expression and return a list to return multiple choices.",
            ),
        ),
        migrations.AlterField(
            model_name="prompt",
            name="type",
            field=models.CharField(
                choices=[
                    ("text", "Text: Simple Text input"),
                    ("text_area", "Text area: Multiline Text Input."),
                    (
                        "text_read_only",
                        "Text (read-only): Simple Text input, but cannot be edited.",
                    ),
                    (
                        "text_area_read_only",
                        "Text area (read-only): Multiline Text input, but cannot be edited.",
                    ),
                    (
                        "username",
                        "Username: Same as Text input, but checks for and prevents duplicate usernames.",
                    ),
                    ("email", "Email: Text field with Email type."),
                    (
                        "password",
                        "Password: Masked input, password is validated against sources. Policies still have to be applied to this Stage. If two of these are used in the same stage, they are ensured to be identical.",
                    ),
                    ("number", "Number"),
                    ("checkbox", "Checkbox"),
                    (
                        "radio-button-group",
                        "Fixed choice field rendered as a group of radio buttons.",
                    ),
                    ("dropdown", "Fixed choice field rendered as a dropdown."),
                    ("date", "Date"),
                    ("date-time", "Date Time"),
                    (
                        "file",
                        "File: File upload for arbitrary files. File content will be available in flow context as data-URI",
                    ),
                    ("separator", "Separator: Static Separator Line"),
                    ("hidden", "Hidden: Hidden field, can be used to insert data into form."),
                    ("static", "Static: Static value, displayed as-is."),
                    ("ak-locale", "authentik: Selection of locales authentik supports"),
                ],
                max_length=100,
            ),
        ),
    ]
