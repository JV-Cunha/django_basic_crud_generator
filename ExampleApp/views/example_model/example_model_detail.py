from django.views.generic import DetailView

from ExampleApp.models import ExampleModel


class ExampleModelDetailView(DetailView):
    model = ExampleModel
    template_name = "example_model/example_model_detail.html"
