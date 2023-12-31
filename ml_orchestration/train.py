from prefect import task


@task
def start_training(model, x_train, y_train):
    model.fit(x_train, y_train)
