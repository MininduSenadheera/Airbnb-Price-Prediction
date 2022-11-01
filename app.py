import pickle
def loadModel():
    pickle_a = open("model.pkl","rb")
    regressor = pickle.load(pickle_a)
    return regressor
