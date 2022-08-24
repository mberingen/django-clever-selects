from django.urls import include, path
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin

from cars.views import (AjaxChainedCities, AjaxChainedColors,
                        AjaxChainedCountries, AjaxChainedModels,
                        AjaxChainedNames, DeleteCarView, EditCarView,
                        HomeView, ModelChainView, MultipleChainView,
                        SimpleChainView)

# admin.autodiscover()

urlpatterns = [
    path('ajax/chained-names/',
        AjaxChainedNames.as_view(),
        name='ajax_chained_names'),
    path('ajax/chained-countries/',
        AjaxChainedCountries.as_view(),
        name='ajax_chained_countries'),
    path('ajax/chained-cities/',
        AjaxChainedCities.as_view(),
        name='ajax_chained_cities'),
    path('ajax/chained-brand-models/',
        AjaxChainedModels.as_view(),
        name='ajax_chained_models'),
    path('ajax/chained-colors/',
        AjaxChainedColors.as_view(),
        name='ajax_chained_colors'),
    path('simple-chain/', SimpleChainView.as_view(), name='simple_chain'),
    path('multiple-chain/',
        MultipleChainView.as_view(),
        name='multiple_chain'),
    path('model-chain/', ModelChainView.as_view(), name='model_chain'),
    path('edit-car/<int:pk>/', EditCarView.as_view(), name='edit_car'),
    path('delete-car/<int:pk>/',
        DeleteCarView.as_view(),
        name='delete_car'),
    path('', HomeView.as_view(), name='home'),
]
