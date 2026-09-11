def get_predicted_data(csvFile):
    import pandas as pd

    data = pd.read_csv(csvFile)
    X = data[['PRECTOTCORR','RH2M','T2M_MIN','WS2M']]
    y = data['T2M_MAX']

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train, y_train)

    from sklearn.metrics import mean_squared_error
    pred = model.predict(X_test)
    error = mean_squared_error(y_test, pred)
    # print("Error:", error)

    new_data = [[0, 40, 22, 1.2]] # Predict New Weather
    prediction = model.predict(new_data)
    # print("Predicted Max Temp:", prediction)

    return (error, prediction)

