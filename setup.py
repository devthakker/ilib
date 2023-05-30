from setuptools import setup, find_packages

setup( 
        name='ilib',
        version='0.1',
        packages=find_packages(exclude=['tests*']),
        license='MIT',
        description='A package for various technical indicators',
        long_description=open('README.md').read(),
        install_requires=['numpy', 'pandas'],
        author='Devin Thakker',
        author_email='devin.thakker@outlook.com',
        url='',
        keywords=['Tilib', 'technical indicators', 'finance', 'trading', 'stocks', 'crypto'],
        classifiers=[
            'Programming Language :: Python :: 3.7',
            'Intended Audience :: Algorithmic Traders',
            'License :: MIT License',
            ],
        python_requires='>=3.7'
)