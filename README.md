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

> line 29 for no deployed runs
>
> line 30 for local deployment
>
> line 31 for work pool deployment. In our case prefect:managed

Work pool setup

`prefect work-pool create my-managed-pool --type prefect:managed `

Make sure the updated code is present in the github, Run the script as usual to create deployment

*ruff usage*

> ruff check .
> 
> ruff check --fix .
>
> ruff format .








