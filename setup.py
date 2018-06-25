from setuptools import setup

with open("README", 'r') as f:
    longDescription = f.read()

setup(name='substring',
      version='0.2',
      description='Multi-Operational and Flexible Substring Package',
      long_description=longDescription,
      url='https://github.com/VETURISRIRAM/SUBSTRING',
      author='Sriram Veturi',
      author_email='sriram.tutu@gmail.com',
      license='MIT',
      packages=['substring'],
      classifiers=(
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Topic :: Software Development :: Libraries :: Python Modules"
      ),
)
