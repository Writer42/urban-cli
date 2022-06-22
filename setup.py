import setuptools

setuptools.setup(
    name='UrbanCLI',
    version='0.0.1',
    packages=['urban_cli'],
    include_package_data=True,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    entry_points={
        "console_scripts": [
            "ucli=urban_cli.main:cli",
        ]
    
    },
    install_requires=['requests','rich','click'],
)