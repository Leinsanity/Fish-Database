from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.contrib import admin
from .resources import SpecimenResource
from .models import Specimen, Preparation1, Preparation2, Collection_Date, Collector, Photographer, Locations, Status, Family, Tissue, Identifier, Resultss

admin.site.site_header = 'Fish BMin'
admin.site.site_title = 'Fish Barcode in Mindanao'
admin.site.index_title = 'Fish Barcode in Mindanao'
admin.site.site_url = "http://127.0.0.1:8000/search1/"


class SpecimenViewer(ImportExportModelAdmin):
    resource_class = SpecimenResource
    list_per_page = 10
    list_display = ('collection_code', 'initial_ID', 'location', 'date_created', 'author', 'status')
    readonly_fields = ('date_created', 'author')
    # list_editable = ('status',)

    list_filter = (
        ('location', RelatedDropdownFilter), 
        ('collection_date', RelatedDropdownFilter),
        ('family', RelatedDropdownFilter),
        ('author', RelatedDropdownFilter)
        )

    search_fields = ('collection_code', 'initial_ID', 'final_ID')
    view_on_site = False


#config for the collection_date filter
    def get_rangefilter_collection_date_at_title(self, request, field_path):
        return 'Filter by collection date'

# Only Admin can see all entries in the database 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

            
# attaching author to CRUD operations in admin page
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()    

# admin.site.disable_action('delete_selected')
admin.site.register(Specimen, SpecimenViewer)
admin.site.register(Preparation1)
admin.site.register(Preparation2)
admin.site.register(Tissue)
admin.site.register(Collection_Date)
admin.site.register(Locations)
admin.site.register(Family)
admin.site.register(Identifier)
admin.site.register(Collector)
admin.site.register(Photographer)
admin.site.register(Status)
# admin.site.register(Resultss)

