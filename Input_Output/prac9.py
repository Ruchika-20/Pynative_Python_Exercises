############################################################################
# QUESTION 9 : Check file is empty or not                                  #
############################################################################

import os

size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')
