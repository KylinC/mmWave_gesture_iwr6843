import os
import pickle

import numpy as np
from utils.path_utils import idp_preprocess, generate_path

specimen_list = [
    # generate_path('zr', 0), generate_path('zr', 1),
    # generate_path('zy', 0), generate_path('zy', 1),
    # generate_path('zy', 2),generate_path('zy', 3)

    # generate_path('zl', 0),generate_path('zl', 1),
    # generate_path('zl', 2),generate_path('zl', 3)
    # generate_path('py', 0),#generate_path('py', 3)
    generate_path('zl', 0, mode='idp'), generate_path('zl', 1, mode='idp'),
    generate_path('zy', 0, mode='idp'), generate_path('zy', 1, mode='idp'),
    generate_path('ya', 0, mode='idp'), generate_path('ya', 1, mode='idp'),
]

# use data augmentation

isDataGen = True

# for i, path in enumerate(specimen_list):
#     # generate orignial data
#     print('Processing specimen #' + str(i) + '__________________________________')
#     idp_preprocess(path)
#     idp_preprocess(path,  augmentation=['trans'])
#     idp_preprocess(path, augmentation=['rot'])
#     idp_preprocess(path,  augmentation=['scale'])
#
#     idp_preprocess(path, augmentation=['trans', 'rot'])
#     idp_preprocess(path, augmentation=['trans', 'scale'])
#     idp_preprocess(path,  augmentation=['rot', 'scale'])
#
#     idp_preprocess(path,  augmentation=['trans', 'rot', 'scale'])

# just plot the thing
for i, path in enumerate(specimen_list):
    # generate orignial data
    print('Processing specimen #' + str(i) + '__________________________________')
    idp_preprocess(path)