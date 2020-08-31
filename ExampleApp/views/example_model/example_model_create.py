from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from ExampleApp.models import ExampleModel

class ExampleModelCreateView(CreateView):
    model = ExampleModel
    fields = '__all__'
    template_name = "example_model/example_model_create.html"
    success_url = reverse_lazy('example_model_list')
