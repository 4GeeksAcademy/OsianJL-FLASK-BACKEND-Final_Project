import os
from common import app
from get_endpoints import *
from post_endpoints import *
from put_endpoints import *
from delete_endpoints import *
from token_endpoints import *
from favorites_endpoints import *



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
