from setuptools import setup, find_packages

setup(
    name="markify",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask>=2.3.3",
        "markitdown>=0.0.1a3",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "isort>=5.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "markify=markify.app:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A service that converts web pages to Markdown format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/markify",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
) 