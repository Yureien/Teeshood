from setuptools import setup

setup(name='django-payments-instamojo',
      version='0.1.3',
      description='Instamojo Provider for django-payments',
      url='http://github.com/FadedCoder/django-payments-instamojo',
      author='Soham Sen',
      author_email='contact@sohamsen.me',
      maintainer='Soham Sen',
      license='BSD License',
      packages=['django_payments_instamojo'],
      long_description=open('README.md').read(),
      include_package_data=True,
      zip_safe=False,
      keywords='django,payments,ecommerce,saleor,delivery',
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      )
