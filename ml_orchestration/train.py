from prefect import task
import pickle


@task
def start_training(model, x_train, y_train):
    model.fit(x_train, y_train)


@task
def save_model(model, save_path):
    pickle.dump(model, open(save_path, "wb"))
