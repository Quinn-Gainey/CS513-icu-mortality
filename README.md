# WiDS ICU Mortality Prediction Dataset

This repository contains the **WiDS Datathon 2020 ICU Mortality dataset** and supporting files for exploration and analysis.

## Contents

- `data/training_v2.csv` — main dataset
- `data/WiDS Datathon 2020 Dictionary.csv` — feature descriptions from WiDS
- `notebooks/dataset_overview.ipynb` — Jupyter notebook summarizing dataset properties

## Dataset Description

The dataset contains clinical features collected during ICU stays. The target variable is `hospital_death` indicating in-hospital mortality.

**Key notes:**

- Many lab values are missing for patients who were not tested.
- Core features like `icu_type`, `pre_icu_los_days`, `apache_post_operative`, and `encounter_id` have no missing values.
- This dataset is derived from [MIMIC-III](https://mimic.mit.edu/) and designed for predictive modeling.

## Citation

WiDS Datathon 2020: [https://www.kaggle.com/c/widsdatathon2020](https://www.kaggle.com/c/widsdatathon2020)

If you use this dataset, please cite:

> WiDS Datathon 2020 ICU Mortality Prediction Dataset, derived from MIMIC-III, Stanford University, MIT, and Harvard. Retrieved from Kaggle.

[Karen Matthys, Marzyeh Ghassemi, Meredith Lee, NehaGoel, Sharada Kalanidhi, and sumalaika. WiDS Datathon 2020. https://kaggle.com/competitions/widsdatathon2020, 2020. Kaggle.] 

## License

Check Kaggle's dataset license. This repository is for **educational purposes only**.
