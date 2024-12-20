# Fuel Cell Performance Prediction

## Dataset
Initially, the dataset (`Fuel_cell_performance_data-Full.csv`) contained 1000 samples with 15 features (F1 to F15) and 5 target columns (`Target1` to `Target5`). To simplify the analysis, we filtered the dataset to retain only the `Target5` column (as my Roll no ends with '9'), creating a new dataset named `Filtered_Fuel_cell_performance_data.csv` using the script `filter_csv.py`.

The features include various measurements related to fuel cell performance. The `Target5` variable represents a specific performance metric to be predicted.

### Dataset Summary
- **Original Dataset**: `Fuel_cell_performance_data-Full.csv`
  - **Features**: F1 to F15
  - **Targets**: Target1, Target2, Target3, Target4, Target5
- **Filtered Dataset**: `Filtered_Fuel_cell_performance_data.csv`
  - **Features**: F1 to F15
  - **Target**: Target5
- **Key Statistics**:
  - Mean of `Target5`: 57.61
  - Standard deviation of `Target5`: 44.42
  - Range of `Target5`: 2.84 to 271.45

## Models and Results
The following models were tested on the filtered dataset:
- **Linear Regression**: A simple linear approach to model the relationship between input features and the target variable.
- **Decision Tree**: A tree-based model that splits data into branches to make predictions.
- **Random Forest**: An ensemble method that builds multiple decision trees and averages their results.
- **Support Vector Regressor (SVR)**: A regression method that uses support vector machines to find the optimal hyperplane.

### Performance Metrics
| Model                    |   MAE   |    MSE   |   RMSE   | R2 Score   |
|--------------------------|---------|----------|----------|------------|
| Linear Regression        | 19.285  |  622.364 | 24.9472  |  0.694349  |
| Decision Tree            | 20.1521 |  818.861 | 28.6157  |  0.597847  |
| Random Forest            | 14.8214 |  455.734 | 21.3479  |  0.776183  |
| Support Vector Regressor | 32.6715 | 2202.180 | 46.9274  | -0.0815214 |

## Conclusion
- **Random Forest** performed the best, achieving the lowest error rates and highest R2 score, making it suitable for complex data with non-linear relationships.
- **Linear Regression** provided a good baseline performance and is easy to interpret but struggled with non-linear dependencies.
- **Decision Tree** offered moderate performance but was prone to overfitting.
- **SVR** struggled with this dataset and produced the lowest R2 score.

## How to Run the Project
1. Install required libraries
2. Use `filter_csv.py` to preprocess the full dataset and generate the filtered dataset (`Filtered_Fuel_cell_performance_data.csv`).
3. Load the filtered dataset and split it into training and testing sets.
4. Run the script to train models and evaluate performance metrics.
5. View results in the `model_performance.csv` file.

## Files Included
- `filter_csv.py`: Script to filter the full dataset and retain only `Target5`.
- `fuel_cell_analysis.py`: Contains the code to train and evaluate models.
- `Fuel_cell_performance_data-Full.csv`: Original dataset with all target columns.
- `Filtered_Fuel_cell_performance_data.csv`: The filtered dataset used for training and evaluation.
- `model_performance.csv`: CSV file with performance metrics.
- `README.md`: This documentation file.


