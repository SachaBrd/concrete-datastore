# Generated by Django 2.2.10 on 2020-03-03 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('concrete', '0003_passwordchangetoken_expiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPack',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('public', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('status', models.CharField(default='PENDING', max_length=255)),
                ('nb_articles', models.IntegerField(default=0)),
                ('cost', models.DecimalField(decimal_places=2, default=10.0, max_digits=20)),
                ('sold', models.BooleanField(default=False)),
                ('additional_filtering', models.BooleanField(default=False)),
                ('can_admin_groups', models.ManyToManyField(blank=True, related_name='group_administrable_itempacks', to='concrete.Group')),
                ('can_admin_users', models.ManyToManyField(blank=True, related_name='administrable_itempacks', to=settings.AUTH_USER_MODEL)),
                ('can_view_groups', models.ManyToManyField(blank=True, related_name='group_viewable_itempacks', to='concrete.Group')),
                ('can_view_users', models.ManyToManyField(blank=True, related_name='viewable_itempacks', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='owned_itempacks', to=settings.AUTH_USER_MODEL)),
                ('defaultdivider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='divider_itempacks', to='concrete.DefaultDivider')),
            ],
            options={
                'verbose_name': 'ItemPack',
                'verbose_name_plural': 'ItemPacks',
                'ordering': ('-modification_date', '-creation_date'),
            },
        ),
    ]
