################################################################################ 
#                        Run the Program to see the flag!                      #
################################################################################

import base64

MABSVDF = "03SDNDSD9VW3EjT0M1XOBDS3kFU7VVROdFU"
MABSVDF = MABSVDF[::-1]
JZLTNQJZBS = base64.b64decode(MABSVDF + '=' * (-len(MABSVDF) % 4)).decode('utf-8')
print("FLAG:", JZLTNQJZBS)

