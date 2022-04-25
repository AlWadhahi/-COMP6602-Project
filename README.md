# COMP6602-Project
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/alwadhahi/comp6602-project/main/app/app.py)



This repository will contain all relevant work for the project.

## Installing Packages
if you would like to run the project locally on your machine, then you need to download the dataset first then follow these steps: 

1. Make sure you have `Poetry` installed in your Environment (run `pip install Poetry`).
2. Once installed, you can now install the dependencies by running `poetry install`. 
3. Once your dependencies are installed, access the project's virtual environment by running `poetry shell`.
4. To run the app `streamlit run .\app\app.py`

## Repository Structure

- `\app`: folder includes streamlit app that runs the project
- `\notebooks`: folder includes notebook that explores the data and builds the model
- `\saved-models`: folder includes saved models using pickle that is used in the streamlit app


## Dataset used

The dataset used for this experiment is [car-damage-dataset](https://github.com/neokt/car-damage-detective)