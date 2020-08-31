import setuptools

long_description =  open("README.md", "r").read()

setuptools.setup(
    name='Django Basic CRUD Generator',
    version='0.2',
    description='Script to generate views, templates and tests files for a given Django Model',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/J-hanks/django_basic_crud_generator.git',
    author='Joao Cunha  ',
    author_email='jvsdc1992@gmail.com',
    license='None',
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Development Status :: 3 - Alpha',
        "Operating System :: OS Independent",
    ],
    keywords='django crud generator scaffolding scaffold',
)
