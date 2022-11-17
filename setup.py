from setuptools import find_packages, setup

setup(name="laiarturs-ros_api",
      version="1.0.0",
      description="Connect to and use API interface of MikroTik RouterOS",
      long_description=open("README.md", "r", encoding="utf-8").read(),
      long_description_content_type="text/markdown",
      url="https://github.com/timerke/RouterOS_API",
      author="",
      author_email="",
      packages=find_packages(),
      install_requires=[],
      classifiers=["License :: OSI Approved :: MIT License",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Development Status :: 4 - Beta",
                   "Topic :: System :: Networking"],
      python_requires=">=3.4",
      )
