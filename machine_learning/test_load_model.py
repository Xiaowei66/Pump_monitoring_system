import pickle 
import numpy as np 
loaded_model = pickle.load(open('model.pkl', 'rb'))

test = "23.0776,1492.5928,170.7463,1.0346,0.4215,0.4215"
matrix = []
for i in test.split(","):
    matrix.append(i)
a = np.array(matrix,dtype="float64")
print(loaded_model.predict_proba(a.reshape(1,-1))[0][1]) # broken prop