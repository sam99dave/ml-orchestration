from sklearn.neural_network import MLPClassifier
from prefect import task


# Flow
@task
def get_model(
    alpha=0.01,
    batch_size=256,
    epsilon=1e-08,
    hidden_layer_sizes=(300,),
    learning_rate="adaptive",
    max_iter=500,
):
    model = MLPClassifier(
        alpha=alpha,
        batch_size=batch_size,
        epsilon=epsilon,
        hidden_layer_sizes=hidden_layer_sizes,
        learning_rate=learning_rate,  # type: ignore
        max_iter=max_iter,
    )

    return model
