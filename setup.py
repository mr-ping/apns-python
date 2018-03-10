from distutils.core import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="apns-python",
    packages=["apns_python"],
    version="0.1.2",
    description="A Python client for Apple Push Notification service(APNs)",
    author="Ping",
    author_email="yuanta11@gmail.com",
    url="https://github.com/mr-ping/apns-python",
    download_url="https://github.com/mr-ping/apns-python/archive/master.zip",
    keywords=["apns", "python", "python2", "http2", "http2.0"],
    install_requires=["hyper", "ujson"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description=read('README'),
)
