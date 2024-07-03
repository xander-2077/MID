import pickle
import sys
sys.path.append('.')
from dataset import EnvironmentDataset, collate, get_timesteps_data, restore
from environment import Environment, Scene, Node, derivative_of
import dill

train_data_path = '/home/zdj/Codes/MID/processed_data_noise/eth_train.pkl'
# with open(train_data_path, 'rb') as f:
#     train_env = pickle.load(f)

df = dill.load(open(train_data_path, "rb"))

import pdb; pdb.set_trace()