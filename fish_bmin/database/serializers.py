from rest_framework import serializers

from .models import Specimen, Preparation1, Preparation2, Collection_Date, Collector, Photographer, Locations, Status, Family, Tissue, Identifier, Results

class CollectionDateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Collection_Date
            fields = ('id', 'url', 'collection_date')

class Collectorserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Collector
            fields = ('id', 'url', 'name')

class FamilySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Family
            fields = ('id', 'url', 'family')          

class IdentifierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Family
            fields = ('id', 'url', 'name') 

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Locations
            fields = ('id', 'url', 'location', 'locality')

class PhotographerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Photographer
            fields = ('id', 'url', 'name')   

class Preparation1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Preparation1
            fields = ('id', 'url', 'preparation')

class Preparation2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Preparation2
            fields = ('id', 'url', 'preparation')         

class SpecimenSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
            model = Specimen
            fields = ('url', 'collection_code', 'initial_ID', 'location', 'date_created', 'last_updated')

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Status
            fields = ('id', 'url', 'status')   

class TissueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Tissue
            fields = ('id', 'url', 'tissue')
            
class ResultsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
            model = Specimen
            fields = ('collection_code')                     