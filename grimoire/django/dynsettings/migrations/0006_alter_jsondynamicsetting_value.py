# Generated by Django 4.2 on 2023-05-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dynsettings", "0005_alter_booleandynamicsetting_value_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jsondynamicsetting",
            name="value",
            field=models.JSONField(
                help_text="Setting value. It must be valid JSON. This setting type is intended only for developers and users who know how to compose valid JSON values. Do not edit them unless you know what are you doing. If, by other means / database access, you or someone corrupts the value of this field, enter by the same mean and restore its original value, or just {} (open and close curly bracers) to have a valid value.",
                verbose_name="Value",
            ),
        ),
    ]
