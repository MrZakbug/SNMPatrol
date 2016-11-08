class Device:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.system = kwargs.get('system')
        self.address_Ip = kwargs.get('ip')