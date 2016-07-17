import hotswappy

import plugins


hotswap = hotswappy.Controller(plugins)
hotswap.load()

while True:
    print '\n', hotswap.plugins['test_plugin'].hello_world
    response = raw_input('>>> Press Enter to reload (Y to quit): ')
    if response.lower() == 'y': break
    hotswap.hotswap()
