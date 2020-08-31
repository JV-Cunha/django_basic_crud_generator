# Django Basic Crud Generator
Django Basic CRUD Generator is a simple python script to generate views, templates and tests files for a given Django Model


## Installation:
Download the repository 
```bash
git clone https://github.com/J-hanks/django_basic_crud_generator.git
```
Install using pip
```bash
pip install django_basic_crud_generator
```
## Usage:
You must set app_name and model_name options
```bash
python -m django_basic_crud_generator --app_name YOUR_APP --model_name YOUR_MODEL
```

## Options:
- `--app_name`: Your Django application name
- `--model_name`: Your Django model name you want crud generated

## Manually fix urls file:
- The urls.py file will need mannualy inspection

