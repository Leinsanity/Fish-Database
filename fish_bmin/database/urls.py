from django.urls import path, include
from .import views
# from .views import SearchResultsView
from rest_framework import routers

# admin.site.site_url = ''  # Removes the 'View Site' link
# admin.site.site_header = 'My Site'

router = routers.DefaultRouter()
router.register('Collection Dates', views.CollectionDateView)
router.register('Collectors', views.CollectorView)
router.register('Family', views.FamilyView)
router.register('Identifiers', views.IdentifierView)
router.register('Locations', views.LocationView)
router.register('Photographers', views.PhotographerView)
router.register('Preparation 1', views.Preparation1View)
router.register('Preparation 2', views.Preparation2View)
router.register('Specimens', views.SpecimenView)
router.register('Status', views.StatusView)
router.register('Tissue', views.TissueView)
router.register('Resultss', views.ResultsView)


urlpatterns = [
    path('', include(router.urls)),
    # path('search/', SearchResultsView.as_view(), name='search'),
    path('search1/', views.get_queryset, name='search'),
]