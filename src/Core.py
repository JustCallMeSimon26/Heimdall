from NodeInterface import NodeInterface

class Core():
	def __init__(self,pluginRegister,nodeEditor,debug=False) -> None:
		self.pluginRegister = pluginRegister
		self.nodeInterFace = NodeInterface(nodeEditor,debug)

	# todo