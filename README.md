# Solar-Flare-Classification-Model

One hot encoding replaced mapping due to how mapping affected the scores given by models after tuning. After consultation from online and AI tools, this decision was taken. 

tech stack: 
pandas, scikit learn for ml and eda
joblib for model saving
flask ui + fastapi backend 



## Sources and References: 
https://www.youtube.com/watch?v=luJ64trcCwc - reference to overall structure of an end to end ML project --
https://www.kaggle.com/datasets/stealthtechnologies/solar-flares-dataset - dataset - source - UCI ML Repo --
https://www.youtube.com/watch?v=xi0vhXFPegw - EDA walkthrough --
https://www.aavso.org/zurich-classification-system-sunspot-groups - Zurich Classification of sunspot groups --
https://www.stce.be/educational/classification - McIntosh classification system for sunspots --
Pandas Documentation, sklearn documenetation , streamlit documentation
https://www.geeksforgeeks.org/pandas/pandas-replace-multiple-values-in-python/
https://medium.com/@fraidoonomarzai99/hyperparameters-tunning-and-cross-validation-in-depth-d0918b62d986 - CV and Hyperparameter tuning 
Details for variable information- https://archive.ics.uci.edu/dataset/89/solar+flare - according to the authors, the dataset is intended for the purpose of predicting the number of each type of solar flare in a particular 24H period. 
https://www.youtube.com/watch?v=wwfCZz3VKlY - gridsearch
https://www.geeksforgeeks.org/machine-learning/multioutput-regression-in-machine-learning/ - multi output regression
https://stackoverflow.com/questions/71276813/difference-between-ridgecv-and-gridsearchcv - ridge cv vs grid search cv 
https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall ml metrics 
https://medium.com/@faheemsiddiqi789/how-can-i-determine-if-my-data-is-balanced-or-imbalanced-080819af408c - class imbalance
https://stackoverflow.com/questions/54953967/your-session-crashed-after-using-all-available-ram-in-google-collab kernal/ram crashes
https://stackoverflow.com/questions/72101295/python-gridsearchcv-taking-too-long-to-finish-running time
https://scikit-learn.org/stable/model_persistence.html - model persistence
https://www.youtube.com/watch?v=-WfuEJfItjY - joblib
https://www.youtube.com/watch?v=c1n5iCMzr9E - streamlit
https://www.youtube.com/watch?v=ZnDmTGgYMn0 fast api
https://datascience.stackexchange.com/questions/124959/use-prediction-after-using-get-dummies-in-pandas get dummies
https://www.geeksforgeeks.org/machine-learning/deploying-ml-models-as-api-using-fastapi/ - fastapi 