from subprocess import call
from install import install


call(["git", "pull", "--recurse-submodules"])
install()

