class device:
	def __init__(self, **kwargs):
		self.name = kwargs.get('name')
        self.system = kwargs.get('system')
        self.adressIP = kwargs.get('ip')