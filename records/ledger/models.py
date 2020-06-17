from django.contrib.auth.models import User
from django.db import models


class TblJamabandi(models.Model):
    fid = models.CharField(max_length=255, blank=True, null=True)
    khewat_no = models.CharField(max_length=255, blank=True, null=True)
    khtoni_no = models.CharField(max_length=255, blank=True, null=True)
    old_khasra = models.CharField(max_length=255, blank=True, null=True)
    new_khasra = models.CharField(max_length=255, blank=True, null=True)
    area_kanal = models.FloatField(blank=True, null=True)
    area_marla = models.FloatField(blank=True, null=True)
    landuse_code = models.CharField(max_length=255, blank=True, null=True)
    landuse_type = models.CharField(max_length=255, blank=True, null=True)
    khewat_kanal = models.FloatField(blank=True, null=True)
    khewat_marla = models.FloatField(blank=True, null=True)
    mauza_code = models.CharField(max_length=255, blank=True, null=True)
    mauza_name = models.CharField(max_length=255, blank=True, null=True)
    jamabandi = models.CharField(max_length=255, blank=True, null=True)
    enter_by = models.CharField(max_length=255, blank=True, null=True)
    patwari = models.CharField(max_length=255, blank=True, null=True)
    jamabandi_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_jamabandi'


class TblLandTypes(models.Model):
    code = models.CharField(primary_key=True, max_length=255)
    land_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_land_types'


class TblMauza(models.Model):
    id = models.IntegerField(primary_key=True)
    mauza_code_lis = models.IntegerField(blank=True, null=True)
    phase = models.TextField(blank=True, null=True)
    mauza_name = models.TextField(blank=True, null=True)
    tehsil_name = models.TextField(blank=True, null=True)
    tehsil_id = models.TextField(blank=True, null=True)
    distt_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_mauza'


class TblPurchasedDetail(models.Model):
    jamabandi_code = models.ForeignKey(TblJamabandi, on_delete=models.CASCADE, db_column='jamabandi_code', blank=True,
                                       null=True)
    file_no = models.CharField(max_length=255, blank=True, null=True)
    land_owner = models.CharField(max_length=255, blank=True, null=True)
    land_owner_cnic = models.CharField(max_length=255, blank=True, null=True)
    acq_area_kanal = models.FloatField(blank=True, null=True)
    acq_area_marla = models.FloatField(blank=True, null=True)
    acq_area_sqft = models.FloatField(blank=True, null=True)
    sale_deed_no = models.CharField(max_length=255, blank=True, null=True)
    sale_deed_date = models.DateField(blank=True, null=True)
    mutation_no = models.CharField(max_length=255, blank=True, null=True)
    mutation_date = models.DateField(blank=True, null=True)
    pos_reg_no = models.CharField(max_length=255, blank=True, null=True)
    pos_page_no = models.CharField(max_length=255, blank=True, null=True)
    pos_letter_refrenece_no = models.CharField(max_length=255, blank=True, null=True)
    pos_date = models.DateField(blank=True, null=True)
    pos_phase = models.CharField(max_length=255, blank=True, null=True)
    pos_sector = models.CharField(max_length=255, blank=True, null=True)
    investor = models.CharField(max_length=255, blank=True, null=True)
    patwari = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, db_column='created_by', blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_purchased_detail'


class TblTehsil(models.Model):
    tehsil_id = models.IntegerField(primary_key=True)
    tehsil_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tehsil'
