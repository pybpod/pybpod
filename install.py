import pip, os


def install():
	pip.main(['install', '--upgrade', os.path.join('logging-bootstrap','.')])
	pip.main(['install', '--upgrade', os.path.join('pysettings','.')])
	pip.main(['install', '--upgrade', os.path.join('pyforms','.')])
	pip.main(['install', '--upgrade', os.path.join('pyforms-generic-editor','.')])
	pip.main(['install', '--upgrade', os.path.join('pybpod-api','.')])
	pip.main(['install', '--upgrade', os.path.join('pybpod-gui-api','.')])
	pip.main(['install', '--upgrade', os.path.join('pybpod-gui-plugin','.')])
	pip.main(['install', '--upgrade', os.path.join('pybpod-gui-plugin-session-history','.')])
	pip.main(['install', '--upgrade', os.path.join('pybpod-gui-plugin-timeline','.')])
	pip.main(['install', '--upgrade', os.path.join('pybpod-rotary-encoder-module','.')])


if __name__=='__main__': 
	install()