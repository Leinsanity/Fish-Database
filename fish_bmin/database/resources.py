from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget, CharWidget
from .models import User, Specimen, Preparation1, Preparation2, Collection_Date, Collector, Photographer, Locations, Status, Family, Tissue, Identifier

class SpecimenResource(resources.ModelResource):

    # def import_row(self, row, instance_loader, **kwargs):
    #         # overriding import_row to ignore errors and skip rows that fail to import
    #         # without failing the entire import
    #         import_result = super(SpecimenResource, self).import_row(row, instance_loader, **kwargs)
    #         if import_result.import_type == RowResult.IMPORT_TYPE_ERROR:
    #             # Copy the values to display in the preview report
    #             import_result.diff = [row[val] for val in row]
    #             # Add a column with the error message
    #             import_result.diff.append('Errors: {}'.format([err.error for err in import_result.errors]))
    #             # clear errors and mark the record to skip
    #             import_result.errors = []
    #             import_result.import_type = RowResult.IMPORT_TYPE_SKIP

    #         return import_result

    id = fields.Field(
        column_name='Database ID',
        attribute='id'
    )

    collection_code = fields.Field(
        column_name='Collection Code',
        attribute='collection_code',
    )

    collection_date = fields.Field(
        column_name='Collection Date',
        attribute='collection_date',
        widget=ForeignKeyWidget(Collection_Date, 'collection_date'))

    location = fields.Field(
        column_name='Location',
        attribute='location',
        widget=ForeignKeyWidget(Locations, 'location'))

    family = fields.Field(
        column_name='Family',
        attribute='family',
        widget=ForeignKeyWidget(Family, 'family'))

    identifier = fields.Field(
        column_name='Identifier',
        attribute='identifer',
        widget=ForeignKeyWidget(Identifier, 'name'))

    initial_id = fields.Field(
        column_name='Initial ID',
        attribute='initial_ID',
    )

    final_id = fields.Field(
        column_name='Final ID',
        attribute='final_ID'
    )  

    preparation_1 = fields.Field(
        column_name='Preparation1',
        attribute='preparation_1',
        widget=ForeignKeyWidget(Preparation1, 'preparation'))   

    preparation_2 = fields.Field(
        column_name='Preparation2',
        attribute='preparation_2',
        widget=ForeignKeyWidget(Preparation2, 'preparation'))   

    # tissue = fields.Field(
    #     column_name='Tissue',
    #     attribute='tissue',
    #     widget=CharWidget()
    #     )

    collector = fields.Field(
        column_name='Collector/s',
        attribute='collector',
        widget=ManyToManyWidget(Collector, field = 'name'))

    photographer = fields.Field(
        column_name='Photographer/s',
        attribute='photographer',
        widget=ForeignKeyWidget(Photographer, 'name'))    

    status = fields.Field(
        column_name='Status',
        attribute='status',
        widget=ForeignKeyWidget(Status, 'status'))   

    barcode = fields.Field(
        column_name='DNA Barcode',
        attribute='dna_barcode',
        )

    author = fields.Field(
        column_name='author',
        attribute='author',
        widget=ForeignKeyWidget(User, 'username')
    )

    class Meta:
        skip_unchanged = True
        report_skipped = True
        model = Specimen
        fields = ('id', 'collection_code', 'collection_date', 'location', 'family', 'identifier', 'preparation_1',
        'preparation_2', 'status', 'author')
        # fields = ('collection_code', 'collection_date', 'location', 'family')
        # export_order = ('collection_code', 'collection_date', 'location', 'family')
        