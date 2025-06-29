# OPTIMIZATION-MODEL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: PAVITHRA K

*INTERN ID*: CT04DF2827

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

## DESCRIPTION:

The end-to-end Iris classification project was designed to demonstrate how raw data can be transformed into a fully functional prediction system, all developed in Python. The workflow begins with a data extraction step, continues with preprocessing and model training, and finishes with deployment through a Flask API to serve predictions in real time.

The process starts by loading the famous Iris dataset, which contains 150 records of iris flowers with four measured features: sepal length, sepal width, petal length, and petal width. Each record belongs to one of three classes: setosa, versicolor, or virginica. In the training script (train_model.py), this data is read using scikit-learn’s built-in dataset loader. The dataset is split into input features (X) and labels (y), then further divided into training and testing subsets to validate the model’s performance.

A critical step in machine learning is preprocessing. For this project, a StandardScaler was used to standardize the numeric feature values so they all have mean zero and unit variance. This helps the logistic regression algorithm converge more quickly and accurately. After scaling, the model was trained using scikit-learn’s LogisticRegression. This algorithm is well-suited for multi-class classification problems and produces a simple, interpretable model.

Once training was complete, the model’s accuracy was evaluated on the test set, and the resulting score (usually close to 95–100%) was printed. To preserve the model for future use, both the trained logistic regression model and the scaler were saved to disk as .joblib files. This step is essential in any production pipeline because it avoids retraining every time the application starts.

The deployment portion of the project was built using Flask, a lightweight Python web framework. The Flask app (app.py) begins by loading the previously saved model and scaler. An HTTP endpoint /predict is defined to accept JSON-formatted input. This endpoint expects the user to send a list of four numeric feature values, which will be used to generate a prediction.

When a request is received, the app first validates that input features were provided. It converts the input into a NumPy array, applies the scaler transformation to standardize it in the same way as during training, and then passes it to the logistic regression model to obtain a predicted class label. The prediction is converted from a numeric code to a human-readable class name—setosa, versicolor, or virginica—and returned as a JSON response to the client.

This approach demonstrates a true end-to-end pipeline, beginning with raw data, going through preprocessing and training, and finishing with deployment as a web service. The model can now be queried by any system capable of making HTTP POST requests. For example, you can test it using tools such as curl or Postman, or even build a frontend interface that connects to the API.

Overall, this code encapsulates all the essential parts of a professional data science project: loading data, transforming it into features the model can understand, training and validating a classifier, persisting the trained components, and creating an accessible prediction endpoint. This pattern is widely applicable across domains, from finance to healthcare to e-commerce.
