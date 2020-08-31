from setuptools import setup

setup(
    name='Django Basic CRUD Generator',
    version='0.1',
    description='Script to generate views, templates and tests files for a given Django Model',
    url='https://github.com/J-hanks/django_basic_crud_generator.git',
    author='Joao Cunha  ',
    author_email='jvsdc1992@gmail.com',
    license='None',
    packages=['django_basic_crud_generator'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Development Status :: 3 - Alpha',
    ],
    keywords='Django CRUD scaffolding scaffold',
)
