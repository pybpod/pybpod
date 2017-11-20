import pip


def install():
	pip.main(['install', '--upgrade', 'logging-bootstrap/.'])
	pip.main(['install', '--upgrade', 'pysettings/.'])
	pip.main(['install', '--upgrade', 'pyforms/.'])
	pip.main(['install', '--upgrade', 'pyforms-generic-editor/.'])
	pip.main(['install', '--upgrade', 'pybpod-api/.'])
	pip.main(['install', '--upgrade', 'pybpod-gui-api/.'])
	pip.main(['install', '--upgrade', 'pybpod-gui-plugin/.'])
	pip.main(['install', '--upgrade', 'pybpod-gui-plugin-session-history/.'])
	pip.main(['install', '--upgrade', 'pybpod-gui-plugin-timeline/.'])
	pip.main(['install', '--upgrade', 'pybpod-rotary-encoder-module/.'])


if __name__=='__main__': 
	install()