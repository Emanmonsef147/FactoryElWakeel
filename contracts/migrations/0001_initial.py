# Generated by Django 4.0.2 on 2022-03-31 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_id', models.CharField(blank=True, max_length=255, null=True)),
                ('contract_status', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B')], max_length=255, null=True)),
                ('item_type', models.CharField(blank=True, max_length=255, null=True)),
                ('no_items', models.CharField(blank=True, max_length=255, null=True)),
                ('item_details', models.CharField(blank=True, max_length=255, null=True)),
                ('fn_width', models.FloatField(blank=True, null=True)),
                ('fn_height', models.FloatField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('contract_start_date', models.DateField(blank=True, null=True)),
                ('contract_delivery_date', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='create_contract', to=settings.AUTH_USER_MODEL)),
                ('proposal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposal_contract', to='proposals.proposal')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='update_contract', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]