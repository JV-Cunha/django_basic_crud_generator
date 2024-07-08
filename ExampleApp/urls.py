
from ExampleApp.views import ExampleModelDeleteView

from ExampleApp.views import ExampleModelUpdateView

from ExampleApp.views import ExampleModelDetailView

from ExampleApp.views import ExampleModelCreateView

from ExampleApp.views import ExampleModelListView




path('example_model/Delete/<int:pk>/', ExampleModelDeleteView.as_view(), name='example_model_delete')



path('example_model/Update/<int:pk>/', ExampleModelUpdateView.as_view(), name='example_model_update')



path('example_model/Detail/<int:pk>/', ExampleModelDetailView.as_view(), name='example_model_detail')



path('example_model/Create/', ExampleModelCreateView.as_view(), name='example_model_create')



path('example_model/List/', ExampleModelListView.as_view(), name='example_model_list')

