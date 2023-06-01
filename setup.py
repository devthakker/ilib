from setuptools import setup, find_packages

setup( 
        name='ilib',
        version='0.2',
        # packages=find_packages(exclude=['tests*']),
        packages=find_packages(),
        license='MIT',
        description='A package for various technical indicators',
        install_requires=['numpy', 'pandas', 'matplotlib'],
        author='Devin Thakker',
        author_email='devin.thakker@outlook.com',
        url='https://github.com/devthakker/ilib',
        download_url='https://github.com/devthakker/ilib/archive/refs/tags/v0.2.tar.gz',
        keywords=['ilib', 'technical indicators', 'finance', 'trading', 'stocks', 'crypto'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 3.7',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            ],
        python_requires='>=3.7'
)