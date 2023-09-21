from setuptools import setup, find_packages
from pathlib import Path
import subprocess


def get_version_from_git_tag() -> str:
    version = (
        subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .strip()
    )

    if "-" in version:
        # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
        # pip has gotten strict with version numbers
        # so change it to: "1.3.3+22.git.gdf81228"
        # See: https://peps.python.org/pep-0440/#local-version-segments
        v,i,s = version.split("-")
        version = v + "+" + i + ".git." + s

    assert "-" not in version
    assert "." in version

    return version


nettime_py_version: str = get_version_from_git_tag()

# write version on VERSION file
assert Path('nettime_py/version.py').is_file()
with open("nettime_py/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % nettime_py_version)


# get description from README
with open('README.md', 'r', encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='nettime_py',
    version=nettime_py_version,
    description='Python package to consume netTime application by SPEC, SA.',
    packages=find_packages(),
    package_data={"nettime_py": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],

    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.8",
    install_requires=[
        'requests',
        'pydantic>=2.3.0',
        'pydantic-core>=2.6.3',
        'pydantic-settings>=2.0.3'
    ],
    url='https://gitlab.com/spec-sa-ar/nettime-py',
    author='Lucas Lucyk',
    author_email='lucaslucyk@gmail.com',
)
