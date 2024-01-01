# ml-orchestration
**Simple ML pipeline orchestration**

> Repo is focused primarily on orchestration rather than the ML part

Machine Learning Usecase - [Speech Emotion Recognition](https://data-flair.training/blogs/python-mini-project-speech-emotion-recognition/)

Orchestration - Prefect

## Usage

Clone the repo

`git clone https://github.com/sam99dave/ml-orchestration.git`

Install requirements ( *same directory as pyproject.toml* )

`poetry install`

Login to prefect cloud

`prefect cloud login -k <your-key>`

Want to create separate env? Run `poetry shell` before installing

`poetry run python ./ml_orchestration/start_flow.py`

## Deployment

Serve is recommended for most of the deployments

> Add `pipeline.serve(name="local-serve-deployment")` to the script 
>
> Normal run `poetry run python ./ml_orchestration/start_flow.py`
>
> This will create a deployment locally. To run this, either use UI or the command displayed once the deployment is created on the console


*ruff usage*

> ruff check .
> 
> ruff check --fix .
>
> ruff format .








