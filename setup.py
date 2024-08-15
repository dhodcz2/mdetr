from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name="mdetr",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires='>=3.11',
    include_package_data=True,
    install_requires=install_requires,
    entry_points={},
)
