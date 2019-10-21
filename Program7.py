import numpy as np
import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

heart_data = pd.read_csv("Data7.csv")
heart_data = heart_data.replace("?", np.nan)
model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('exang', 'trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'), ('heartdisease','thalach'), ('heartdisease','chol')])
model.fit(heart_data, estimator=MaximumLikelihoodEstimator)
infer = VariableElimination(model)
q = infer.query(variables=['heartdisease'], evidence={'chol':100})
print(q["heartdisease"])