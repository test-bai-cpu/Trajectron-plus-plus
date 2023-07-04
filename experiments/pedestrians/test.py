import csv
import dill
import sys

sys.path.append("../../trajectron")
from environment import Environment, Scene, Node
from utils import maybe_makedirs
from environment import derivative_of

# Unpickle the object
with open('../processed/eth_train.pkl', 'rb') as f:
    data = dill.load(f)