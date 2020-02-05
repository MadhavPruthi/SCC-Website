from .base_settings import *

if config('DEV_MODE') == 'True':
    from .dev_settings import *
else:
    from .production_settings import *
