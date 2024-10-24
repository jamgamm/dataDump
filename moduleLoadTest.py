import pandas as pd
from pvlib import pvsystem

module_list_test = pvsystem.retrieve_sam(path='https://raw.githubusercontent.com/jamgamm/dataDump/refs/heads/main/TestModule.csv')
print(module_list_test.JA_Solar_JAM72D30_550_MB)
#NOTE: currently missing length and width (in meters) for this panel