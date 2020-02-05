from .base_settings import *

if os.environ.get('DEV_MODE', 'True') == 'True':
    print(os.environ.get('DEV_MODE', 'True'))
    from .dev_settings import *
else:
    from .production_settings import *
