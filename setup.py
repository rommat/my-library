
from setuptools import setup

setup(
    name="my-library",
    version="0.1",
    py_modules=["my_library"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        my-library=my_library:cli
    """,
)
