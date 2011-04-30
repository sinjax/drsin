try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='drsin',
    version='0.1',
    description='',
    author='',
    author_email='',
    url='',
    install_requires=[
		"Pylons>=0.9.7",
		"SQLAlchemy>=0.5",
		"textile>=2.1.4",
		"FormBuild==2.2.0",
		"Elixir>=0.7.1","Routes>=1.12","pycurl==7.19.0","PyRSS2Gen","httpagentparser","pisa","reportlab","html5lib"],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'drsin': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'drsin': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = drsin.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
