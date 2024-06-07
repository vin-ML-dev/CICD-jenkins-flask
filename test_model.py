import pickle
import pandas as pd



def validate_model(fpath='test_data/test.csv'):
    
    # load model
    with open('trained_model/model.pkl', 'rb') as f:
        model = pickle.load(f)

    ### load test data

    test_data = pd.read_csv(fpath)

    #test_data.head()
    test = test_data.values
    print('test data shape:',test.shape)

    pred = model.predict(test)
    print('predicted values:',pred)


if __name__=="__main__":

    fpath = 'test_data/test.csv'

    validate_model(fpath)

    




