from setuptools import setup

setup(
        name='calculator',
        version='0.0.1',
        description='mathematics calculator with one memory slot',
        py_modules=["calc"],
        package_dir={'': 'calculator'},
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: MIT",
            "Operating System :: OS Independent",
            ],
        )
