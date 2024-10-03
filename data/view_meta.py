import pickle
import pprint

file = "data/shakespeare_char/meta.pkl"

meta = None
with open(file, "rb") as f:
    meta = pickle.load(f)


pprint.pprint(meta)