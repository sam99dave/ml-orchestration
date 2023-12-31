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

*ruff usage*

> ruff check .
> 
> ruff check --fix .
>
> ruff format .








