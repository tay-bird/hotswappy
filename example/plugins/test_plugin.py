from hotswappy import Plugin


class TestPlugin(Plugin):

    name = 'test_plugin'

    def __init__(self):
        self.hello_world = 'Hello world!'
