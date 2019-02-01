from onl.platform.base import *
from onl.platform.accton import *

class OnlPlatform_x86_64_accton_asxvolt16b_r0(OnlPlatformAccton,
                                             OnlPlatformPortConfig_20x100):
    PLATFORM='x86-64-accton-asxvolt16b-r0'
    MODEL="ASXvOLT16B"
    SYS_OBJECT_ID=".816.1"

    def baseconfig(self):
        #self.insmod('ym2651y')
        for m in [ 'fan', 'psu', 'leds', 'sfp', 'sys', 'thermal' ]:
            self.insmod("x86-64-accton-asxvolt16b-%s.ko" % m)

        return True
