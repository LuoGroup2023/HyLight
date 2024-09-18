import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
    name="HyLight",
    version="1.0.0",
    author="Xiongbin Kang; Xiao Luo",
    author_email="kangxiongbin@163.com",
    description="Strain aware assembly of low coverage metagenomes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LuoGroup2023/HyLight.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        "HyLight":[
            "tools/miniasm/miniasm",
            "tools/HaploConduct/bin/ViralQuasispecies",
            "script/stageb_abun_v2.sh",
            "tools/HaploConduct/quick-cliques/bin/compdegen",
            "tools/HaploConduct/quick-cliques/bin/printnm",
            "tools/HaploConduct/quick-cliques/bin/qc"
            ]
    },
    install_requires=[
        "scipy==1.5.3",
        "numpy==1.19.5",
        "pandas==1.1.5",
    ],
    entry_points={
        'console_scripts':[
        "hylight = HyLight.script.HyLight:main",
        ]
    },
    python_requires='~=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
    ],
)