from sklearn.metrics import accuracy_score
from prefect import task


@task
def validate(model, x_test, y_test):
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
    print(f"Accuracy: {'{:.2f}'.format(accuracy*100)}")  # type: ignore
