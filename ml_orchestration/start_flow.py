from data_prep import load_data
from model import get_model
from train import start_training
from eval import validate
from prefect import flow


@flow(log_prints=True)
def pipeline():
    print("Loading data..")
    x_train, x_test, y_train, y_test = load_data(test_size=0.25)
    print("Model initialization..")
    MLPmodel = get_model(
        alpha=0.01,
        batch_size=256,
        epsilon=1e-08,
        hidden_layer_sizes=(300,),
        learning_rate="adaptive",
        max_iter=2,
    )
    print("Starting training...")
    start_training(MLPmodel, x_train, y_train)
    print("Validation...")
    validate(MLPmodel, x_test, y_test)

    # TODO: Save model


if __name__ == "__main__":
    pipeline()


"""
Further
- Make the extract_feature a concurrent task
- Revert load_data to flow
- Track metrics in WandB & prefect
- Save model artifacts in WandB & prefect 
- Deploy to prefect managed ( downloading data from drive for training )
- Try out CRON for the pipeline
"""
