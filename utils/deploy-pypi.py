import os
import shutil
import xmlrpc.client
from subprocess import Popen, PIPE
from packaging import version as v


def version_compare(loc_version, rmt_version):
    return v.parse(loc_version) > v.parse(rmt_version)


pypi = xmlrpc.client.ServerProxy('https://pypi.org')

DIRECTORIES_TO_SEARCH_FORM = [
    os.path.join('libraries'),
    os.path.join('base'),
    os.path.join('plugins'),
]

CURRENT_DIRECTORY = os.getcwd()

Popen(['pip', 'install', '--upgrade', 'setuptools', 'wheel', 'twine'])

for search_dir in DIRECTORIES_TO_SEARCH_FORM:
    for dir_name in os.listdir(search_dir):
        dir_path = os.path.abspath(os.path.join(search_dir, dir_name))
        if not os.path.isdir(dir_path):
            continue

        setup_filepath = os.path.join(dir_path, 'setup.py')
        if not os.path.isfile(setup_filepath):
            continue

        os.chdir(dir_path)

        version = Popen(["python", setup_filepath, '--version'], stdout=PIPE).stdout.read()
        version = version.strip().decode()

        package_name = Popen(["python", setup_filepath, '--name'], stdout=PIPE).stdout.read()
        package_name = package_name.strip().decode().replace(' ', '-')

        remote_version = pypi.package_releases(package_name)

        print(dir_name, version, remote_version)

        if len(remote_version) == 0 or version_compare(version, remote_version[0]) is True:
            print('----- UPLOADING TO PYPI -----', package_name)

            if os.path.isdir('./dist'):
                shutil.rmtree('./dist')

            Popen(['python', 'setup.py', 'sdist', 'bdist_wheel'], stdout=PIPE).communicate()
            Popen(['twine', 'upload', os.path.join('dist', '*')]).communicate()

        os.chdir(CURRENT_DIRECTORY)

"""




    def get_pypi_distribution(self, name):

        new_version = self.pypi.package_releases(name)
        if not new_version:
            new_version = self.pypi.package_releases(name.capitalize())

        if new_version is None: return new_version

        new_version  = new_version[0]
        all_versions = self.pypi.package_releases(name, True)
        data = self.pypi.release_data(name, new_version)


        return new_version, all_versions, data.get('summary', '')
"""
