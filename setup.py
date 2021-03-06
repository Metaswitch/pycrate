# -*- coding: UTF−8 -*-

from setuptools import setup, find_packages

setup(
    name="pycrate",
    version="0.4.2",

    #packages=find_packages(),
    packages=["pycrate_core",
              "pycrate_ether",
              "pycrate_media",
              "pycrate_asn1c",
              "pycrate_asn1dir",
              "pycrate_asn1rt",
              "pycrate_csn1",
              "pycrate_csn1dir",
              "pycrate_mobile",
              "pycrate_diameter",
              "pycrate_sys",
              "pycrate_crypto",
              ],
    test_suite="test.test_pycrate",

    # no mandatory dependency
    install_requires=[],

    # optional dependencies
    extras_require={
        "NASLTE"  : ["CryptoMobile"],
        "corenet" : ["pysctp", "CryptoMobile"],
        "diameter_dict" : ["lxml"],
        },

    # for pycrate_asn1dir and pycrate_csn1dir:
    # .asn, .csn, .txt and .json files from asn1dir and csn1dir are not required
    # to be installed
    # only compiled .py modules are installed by default
    # for pycrate_diameter:
    # .xml files are converted to Python dicts and may be updated from time to
    # time
    # for pycrate_corenet:
    # the AuC.db file is the mobile subscriber authentication database
    # containing Ki and is required at runtime when using corenet
    package_data={
        #"pycrate_asn1dir"  : ["*.asn", "*.json"],
        #"pycrate_csn1dir"  : ["*.csn"],
        #"pycrate_diameter" : ["*.xml"],
        "pycrate_corenet"  : ["AuC.db"],
        },
    #include_package_data=False,

    author="Benoit Michau",
    author_email="michau.benoit@gmail.com",
    description="A software suite to handle various data formats",
    long_description=open("README.md", "r").read(),
    url="https://github.com/metaswitch/pycrate/",
    keywords="protocol format asn1 compiler csn1 encoder decoder mobile core network Diameter NAS S1AP NGAP TCAP MAP",
    license="LGPL v2.1+",
    )
