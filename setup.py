from setuptools import setup, find_packages

setup(
    name="lcd_meter_reader",
    version="0.1.0",
    description="Tool to capture and extract readings from LCD meter displays",
    author="LCD Meter Team",
    py_modules=["capture_meter"],
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.20.0",
        "requests>=2.25.0",
    ],
    entry_points={
        'console_scripts': [
            'lcd-meter=capture_meter:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
