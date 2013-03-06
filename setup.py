from setuptools import setup, find_packages

setup(
    name = "redmine-printer",
    version = "0.01",
    author = "Ulas Tuerkmen ",
    install_requires = ["reportlab==2.6"],
    packages=find_packages(),
    zip_safe=False,
    entry_points = {'console_scripts': ['print-stories = redmine_printer:print_stories']}
)
