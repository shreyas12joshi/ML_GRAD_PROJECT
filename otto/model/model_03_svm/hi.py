import os

parentddir =os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir,os.path.pardir))
print(parentddir)


#common for all
import sys
sys.path.append(parentddir)
from otto_utils import consts, utils

# added in svm.py
# parentddir =os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir,os.path.pardir))
# added in utils.py
# parentddir =os.path.abspath(os.path.join(os.path.dirname(__file__)))
