from django.views.generic.edit import DetailView
from django.urls import reverse_lazy

from ExampleApp.models import ExampleModel

class ExampleModelDetailView(DetailView):
    model = ExampleModel
    template_name = "example_model/example_model_detail.html"
    
     //
    