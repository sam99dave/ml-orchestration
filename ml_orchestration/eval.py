from sklearn.metrics import accuracy_score
from prefect import task
from prefect.artifacts import create_markdown_artifact


@task
def validate(model, x_test, y_test):
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
    print(f"Accuracy: {'{:.2f}'.format(accuracy*100)}")  # type: ignore

    markdown_report = f"""## Validation Accuracy: {'{:.2f}'.format(accuracy*100)}"""  # type: ignore
    status = create_markdown_artifact(
        key="validation-metric",
        markdown=markdown_report,
        description="Validation Accuracy",
    )
