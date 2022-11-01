import pickle
def loadModel():
    pickle_a = open("model.pkl","rb")
    regressor = pickle.load(pickle_a)
    return regressor

def convertNeighbourhood(neighbourhood):
    if neighbourhood == 'Allston-Brighton':
        return 0
    elif neighbourhood == 'Back Bay':
        return 1
    elif neighbourhood == 'Beacon Hill':
        return 2
    elif neighbourhood == 'Brookline':
        return 3
    elif neighbourhood == 'Cambridge':
        return 4
    elif neighbourhood == 'Charlestown':
        return 5
    elif neighbourhood == 'Chestnut Hill':
        return 6
    elif neighbourhood == 'Chinatown':
        return 7
    elif neighbourhood == 'Dorchester':
        return 8
    elif neighbourhood == 'Downtown':
        return 9
    elif neighbourhood == 'Downtown Crossing':
        return 10
    elif neighbourhood == 'East Boston':
        return 11
    elif neighbourhood == 'Fenway/Kenmore':
        return 12
    elif neighbourhood == 'Financial District':
        return 13
    elif neighbourhood == 'Government Center':
        return 14
    elif neighbourhood == 'Harvard Square':
        return 15
    elif neighbourhood == 'Hyde Park':
        return 16
    elif neighbourhood == 'Jamaica Plain':
        return 17
    elif neighbourhood == 'Leather District':
        return 18
    elif neighbourhood == 'Mattapan':
        return 19
    elif neighbourhood == 'Mission Hill':
        return 20
    elif neighbourhood == 'North End':
        return 21
    elif neighbourhood == 'Roslindale':
        return 22
    elif neighbourhood == 'Roxbury':
        return 23
    elif neighbourhood == 'Somerville':
        return 24
    elif neighbourhood == 'South Boston':
        return 25
    elif neighbourhood == 'South End':
        return 26
    elif neighbourhood == 'Theater District':
        return 27
    elif neighbourhood == 'West End':
        return 28
    elif neighbourhood == 'West Roxbury':
        return 29
