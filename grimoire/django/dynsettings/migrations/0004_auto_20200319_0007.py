# Generated by Django 2.2 on 2020-03-19 05:07

import collections
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynsettings', '0003_auto_20170910_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicsetting',
            name='name',
            field=models.CharField(help_text='Setting name. Since it will be accessed from python code, the syntax is the same as for any valid python identifier', max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z_][a-zA-Z0-9_]+', 'Setting name must consist in a-z letters, numbers, and underscores, and cannot start with a number')], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='dynamicsetting',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_dynsettings.dynamicsetting_set+', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='jsondynamicsetting',
            name='value',
            field=jsonfield.fields.JSONField(help_text='Setting value. It must be valid JSON. This setting type is intended only for developers and users who know how to compose valid JSON values. Do not edit them unless you know what are you doing. If, by other means / database access, you or someone corrupts the value of this field, enter by the same mean and restore its original value, or just {} (open and close curly bracers) to have a valid value.', load_kwargs={'object_pairs_hook': collections.OrderedDict}, verbose_name='Value'),
        ),
    ]