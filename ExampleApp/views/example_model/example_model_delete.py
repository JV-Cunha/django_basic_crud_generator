from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from ExampleApp.models import ExampleModel

class ExampleModelDeleteView(DeleteView):
    model = ExampleModel
    template_name = "example_model/example_model_delete.html"
    success_url = reverse_lazy('example_model_list')