from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='ploneconf2014.policy',
      version=version,
      description="Plone policy for Ploneconf2014 demo",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='ploneconf policy demo training Cantv.com.ve',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/Covantec/ploneconf2014.policy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneconf2014'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.api',
          'collective.plonetruegallery==3.4.4',
          'collective.geo.bundle==2.1',
          'Products.PloneFormGen==1.7.14',
      ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
