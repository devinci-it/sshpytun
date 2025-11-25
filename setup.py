from setuptools import setup, find_packages

setup(
    name="sshpytun",
    version="0.1.0",
    description="Python SSH tunnel builder utility with fluent interface for local, remote, and dynamic tunnels.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/sshpytun",  # Update with your repo
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
        "Topic :: System :: Networking",
    ],
    keywords="ssh tunnel dynamic local remote fluent-interface",
    license="MIT",
    include_package_data=True,

    entry_points={
        'console_scripts': [
           
	    "sshpytun = sshpytun.app:main", 
	    
	     # Individual tunnel command shortcuts calling centralized handlers
            "sshpytun-dyn = sshpytun.app:main_dyn",
            "sshpytun-loc = sshpytun.app:main_loc",
            "sshpytun-rem = sshpytun.app:main_rem",

        ],
    },
)
