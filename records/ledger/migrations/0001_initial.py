# Generated by Django 3.0.7 on 2020-06-16 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblJamabandi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(blank=True, max_length=255, null=True)),
                ('khewat_no', models.CharField(blank=True, max_length=255, null=True)),
                ('khtoni_no', models.CharField(blank=True, max_length=255, null=True)),
                ('old_khasra', models.CharField(blank=True, max_length=255, null=True)),
                ('new_khasra', models.CharField(blank=True, max_length=255, null=True)),
                ('area_kanal', models.FloatField(blank=True, null=True)),
                ('area_marla', models.FloatField(blank=True, null=True)),
                ('landuse_code', models.CharField(blank=True, max_length=255, null=True)),
                ('landuse_type', models.CharField(blank=True, max_length=255, null=True)),
                ('khewat_kanal', models.FloatField(blank=True, null=True)),
                ('khewat_marla', models.FloatField(blank=True, null=True)),
                ('mauza_code', models.CharField(blank=True, max_length=255, null=True)),
                ('mauza_name', models.CharField(blank=True, max_length=255, null=True)),
                ('jamabandi', models.CharField(blank=True, max_length=255, null=True)),
                ('enter_by', models.CharField(blank=True, max_length=255, null=True)),
                ('patwari', models.CharField(blank=True, max_length=255, null=True)),
                ('jamabandi_code', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_jamabandi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblLandTypes',
            fields=[
                ('code', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('land_type', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_land_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMauza',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mauza_code_lis', models.IntegerField(blank=True, null=True)),
                ('phase', models.TextField(blank=True, null=True)),
                ('mauza_name', models.TextField(blank=True, null=True)),
                ('tehsil_name', models.TextField(blank=True, null=True)),
                ('tehsil_id', models.TextField(blank=True, null=True)),
                ('distt_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_mauza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblPurchasedDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_no', models.CharField(blank=True, max_length=255, null=True)),
                ('land_owner', models.CharField(blank=True, max_length=255, null=True)),
                ('land_owner_cnic', models.CharField(blank=True, max_length=255, null=True)),
                ('acq_area_kanal', models.FloatField(blank=True, null=True)),
                ('acq_area_marla', models.FloatField(blank=True, null=True)),
                ('acq_area_sqft', models.FloatField(blank=True, null=True)),
                ('sale_deed_no', models.CharField(blank=True, max_length=255, null=True)),
                ('sale_deed_date', models.DateField(blank=True, null=True)),
                ('mutation_no', models.CharField(blank=True, max_length=255, null=True)),
                ('mutation_date', models.DateField(blank=True, null=True)),
                ('pos_reg_no', models.CharField(blank=True, max_length=255, null=True)),
                ('pos_page_no', models.CharField(blank=True, max_length=255, null=True)),
                ('pos_letter_refrenece_no', models.CharField(blank=True, max_length=255, null=True)),
                ('pos_date', models.DateField(blank=True, null=True)),
                ('pos_phase', models.CharField(blank=True, max_length=255, null=True)),
                ('pos_sector', models.CharField(blank=True, max_length=255, null=True)),
                ('investor', models.CharField(blank=True, max_length=255, null=True)),
                ('patwari', models.CharField(blank=True, max_length=255, null=True)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_purchased_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblTehsil',
            fields=[
                ('tehsil_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tehsil_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_tehsil',
                'managed': False,
            },
        ),
    ]
