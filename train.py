from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import pickle



def train_model(fpath="train_data/train.csv"):

    load_data = pd.read_csv(fpath)
    #print(load_data.head())
    features = load_data.iloc[:,:-1].values
    target_data = load_data['target'].values
    print('features shape:',features.shape)
    print('target shape:',target_data.shape)
    
    ### feature scaling
    std = StandardScaler()
    std_train = std.fit_transform(features)

    ### training model
    model = LogisticRegression(multi_class="multinomial",solver="sag")

    model.fit(std_train,target_data)

    ### saved model

    with open('trained_model/model.pkl','wb') as f:
        pickle.dump(model,f)


    print("Training completed..! model saved")

if __name__=="__main__":

    fpath = "train_data/train.csv"
    train_model(fpath)

    



