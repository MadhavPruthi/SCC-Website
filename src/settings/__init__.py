from .base_settings import *

if os.environ.get('DEV_MODE', 'True') == 'True':
    from .local_settings import *
else:
    from .production_settings import *
