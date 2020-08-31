from ExampleApp.views import ExampleModelDeleteView
from ExampleApp.views import ExampleModelUpdateView
from ExampleApp.views import ExampleModelDetailView
from ExampleApp.views import ExampleModelCreateView
from ExampleApp.views import ExampleModelListView
path('example_model/list/', ExampleModelListView.as_view(), name='example_model_list')
path('example_model/create/', ExampleModelCreateView.as_view(), name='example_model_create')
path('example_model/detail/<int:pk>/', ExampleModelDetailView.as_view(), name='example_model_detail')
path('example_model/update/<int:pk>/', ExampleModelUpdateView.as_view(), name='example_model_update')
path('example_model/delete/<int:pk>/', ExampleModelDeleteView.as_view(), name='example_model_delete')
