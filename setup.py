from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()

setup(
    name="css2json",
    version="0.0.1",
    license='MIT',
    description="Convert style sheets to json.",
    author='kaiix',
    author_email='kvn.hou@gmail.com',
    url='https://github.com/kaiix/css2json.py',
    py_modules=['css2json'],
    package_data={
        'css2json': ['README.rst', 'LICENSE']
    },
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description=long_description,
)
