from setuptools import setup, find_packages

setup(
    name="deoldify_project",
    version="0.1.0",
    packages=find_packages(),
    url="https://github.com/yourusername/deoldify_project",
    license="MIT",
    description="Project for training and using DeOldify for image colorization",
    author="Your Name",
    author_email="your.email@example.com",
    install_requires=[
        "deoldify",
        "fastai==1.0.60",
        "torch>=2.0.1",
        "torchvision>=0.15.2",
        "Pillow==9.3.0",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)