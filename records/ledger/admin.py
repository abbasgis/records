from django.contrib import admin

# Register your models here.
from django.shortcuts import redirect

from records.ledger.models import TblPurchasedDetail, TblJamabandi


@admin.register(TblPurchasedDetail)
class TblPurchasedDetailAdmin(admin.ModelAdmin):
    save_as_continue = False
    list_display = (
    'jamabandi_code', 'file_no', 'land_owner', 'land_owner_cnic', 'acq_area_kanal', 'acq_area_marla', 'acq_area_sqft',
    'sale_deed_no', 'sale_deed_date', 'mutation_no', 'mutation_date', 'pos_reg_no', 'pos_page_no',
    'pos_letter_refrenece_no', 'pos_date', 'pos_phase', 'investor', 'patwari', 'remarks'
    )

    # search_fields = ('name', 'cnic',)
    # list_filter = ('created_at', 'relation')
    # fields = ('name', 'relation', 'father_name', 'address', 'cnic', 'photo_path', 'mobile_no', 'email_id')
    # ordering = ('name',)

    # def save_model(self, request, obj, form, change):
    #     if change == False:
    #         name = obj.photo_path.name
    #         ext = name.split(".")[1]
    #         obj.photo_path.name = obj.cnic + '.' + ext
    #     obj.save()

    def changelist_view(self, request, extra_context=None):

        return super(TblPurchasedDetailAdmin, self).changelist_view(request, extra_context=extra_context)

    def response_add(self, request, obj, post_url_continue=None):
        redirect_url = request.GET.get('next')
        if redirect_url is None:
            redirect_url = request.path + '../'
        return redirect(redirect_url)

    def response_change(self, request, obj):
        redirect_url = request.GET.get('next')
        if redirect_url is None:
            redirect_url = request.path + '../../'
        return redirect(redirect_url)

    def response_delete(self, request, obj, post_url_continue=None):
        redirect_url = request.GET.get('next')
        if redirect_url is None:
            redirect_url = request.path + '../../'
        return redirect(redirect_url)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


@admin.register(TblJamabandi)
class TblJamabandiAdmin(admin.ModelAdmin):
    save_as_continue = False
    list_display = ('jamabandi_code', 'khewat_no', 'khtoni_no', 'old_khasra', 'new_khasra', 'area_kanal', 'area_marla',
                    'landuse_code', 'landuse_type', 'khewat_kanal', 'khewat_marla', 'mauza_code', 'mauza_name',
                    'jamabandi', 'enter_by', 'patwari', 'jamabandi_code')

    # search_fields = ('name', 'cnic',)
    # list_filter = ('created_at', 'relation')
    # fields = ('name', 'relation', 'father_name', 'address', 'cnic', 'photo_path', 'mobile_no', 'email_id')
    # ordering = ('name',)

    # def save_model(self, request, obj, form, change):
    #     if change == False:
    #         name = obj.photo_path.name
    #         ext = name.split(".")[1]
    #         obj.photo_path.name = obj.cnic + '.' + ext
    #     obj.save()

    def changelist_view(self, request, extra_context=None):

        return super(TblJamabandiAdmin, self).changelist_view(request, extra_context=extra_context)

    def response_add(self, request, obj, post_url_continue=None):
        redirect_url = request.GET.get('next')
        if redirect_url is None:
            redirect_url = request.path + '../'
        return redirect(redirect_url)

    def response_change(self, request, obj):
        redirect_url = request.GET.get('next')
        if redirect_url is None:
            redirect_url = request.path + '../../'
        return redirect(redirect_url)

    def response_delete(self, request, obj, post_url_continue=None):
        redirect_url = request.GET.get('next')
        if redirect_url is None:
            redirect_url = request.path + '../../'
        return redirect(redirect_url)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
