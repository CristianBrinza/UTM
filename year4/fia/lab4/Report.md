# Luna-City Salary System - Final Report
## Project Overview
In Luna-City, the salary computation system has faced public scrutiny due to discrepancies in pay fairness. The Economic Council has assigned the task of building a new, accurate, and fair salary computation system. This report details the methodology, analysis, and conclusions based on the given dataset to address this challenge.





## Tasks and Solutions
- **Task 1:** Data Import and Analysis 
  - Dataset Overview:
    - The dataset was imported and analyzed using pandas. It contains key variables such as `BasePay`, `OvertimePay`, `Benefits`, `TotalPay`, and `TotalPayBenefits`.
    - Missing values were handled, and data types were converted appropriately. 
  - Descriptive Statistics:
    - `BasePay` ranged from `-166` (anomalous negative value) to 319,275.
    - `OvertimePay` ranged from `0` to `220`,`909`, indicating variability in employee contributions.
    - `Benefits` had a high correlation (`0.93`) with TotalPayBenefits, signifying its importance.
  - Visualizations:
    - Histograms showed the distribution of `BasePay`, `OvertimePay`, and other pay components.
    - Boxplots identified outliers in key variables like `BasePay` and `Benefits`.
    - A **heatmap** illustrated strong correlations, helping in feature selection.
- **Task 2:** Feature Selection and Linear Regression
  - Feature Selection:
    - Chosen features:
      - BasePay (strong correlation with TotalPayBenefits: 0.97).
      - OvertimePay (impact on total pay variability).
      - Encoded JobTitle (categorical representation of job type).
    - Justification: These features directly impact the salary computation based on job type and contributions.
  - Linear Regression:
    - Trained a Linear Regression model using the selected features.
    - Model formula:
    ```
    TotalPayBenefits = BasePay × β₁ + OvertimePay × β₂ + JobTitle Coefficient
    ```
- Task 3: Additional Models
  - Ridge Regression:
    - Added L2 regularization to avoid overfitting.
    - Adjusted the contribution of features by penalizing large coefficients.
  - Lasso Regression:
    - Added L1 regularization for feature selection.
    - Sparse model reduced less important coefficients to zero.
  - Performance Comparison:
    - Metrics: MAE, MSE, RMSE, and R² were used for comparison.
    - Ridge Regression slightly outperformed others with the highest R² value (`0.9622`).
- **Task 4:** Model Performance
  - Metrics Used:
    - MAE: Average absolute error between predicted and actual values.
    - MSE: Penalized larger errors more heavily.
    - RMSE: Square root of MSE for interpretability.
    - R²: Variance explained by the model.
  - Results:
    - Linear Regression: R² = 0.9621, RMSE = 12,753.60.
    - Ridge Regression: R² = 0.9622, RMSE = 12,741.14.
    - Lasso Regression: R² = 0.9621, RMSE = 12,754.10.
  - Conclusions:
    - Ridge Regression was the best-performing model due to its balance between complexity and accuracy.
- **Task 5:** Clustering
  - Clustering Algorithm:
    - K-Means Clustering:
      - Features used: BasePay and selected job title coefficients.
      - Excluded TotalPayBenefits to avoid bias.
    - Visualization:
    - PCA was applied to reduce dimensionality.
    - Scatter plot of clusters showed clear separation of employee groups.
- **Task 6:** Conclusions on Clusters
  - Cluster Analysis:
    - `Cluster 0`: High BasePay and TotalPayBenefits (Average TotalPayBenefits = 160,067).
    - `Cluster 1`: Moderate pay group (`Average TotalPayBenefits = 63,246`).
    - `Cluster 2`: Lower pay group (`Average TotalPayBenefits = 58,473`).
  - Prediction Analysis:
    - Best predictions were aligned with Cluster 0 for high-paying jobs like Chief of Police and Fire Chief.
    - Anomalies in `Cluster 2` highlighted discrepancies in low `BasePay` jobs with higher `OvertimePay`.


## Key Deliverables
- Fairness Formula:
```
TotalPayBenefits = BasePay × β₁ + OvertimePay × β₂ + JobTitle Coefficient
```


## Explanation of Implementation for Each Task
### Task 1: Import and Dataset Analysis
- Implementation:
  - Imported the dataset using `pandas.read_csv`.
  - Displayed the first and last two rows to understand the structure.
  - Converted numeric columns (`BasePay`, `OvertimePay`, etc.) to appropriate types.
  - Removed rows with missing values in important columns.
  - Generated basic statistics using `describe()` to understand the range, mean, and outliers.
  - Created distribution plots using `seaborn.histplot` to visualize salary distributions.
  - Created `boxplots` with `sns.boxplot` to detect outliers.
  - Generated a heatmap using `sns.heatmap` to show correlations between variables.
- Explanation:
  - This step helps understand the data and detect inconsistencies or trends, such as strong correlations or outliers in salary components.

### Task 2: Feature Selection and Linear Regression
- Implementation:
  - Selected BasePay, OvertimePay, and encoded JobTitle as features.
  - Used OneHotEncoder to transform JobTitle into numerical columns.
  - Prepared X (features) and y (target: TotalPayBenefits).
  - Split the data into training (80%) and testing (20%) sets using train_test_split.
  - Trained a Linear Regression model using LinearRegression.fit.
  - Extracted feature coefficients and displayed the top 10 influential job titles.
- Explanation:
  - Feature selection ensures only relevant variables are included in the prediction model. Linear Regression establishes relationships between variables and predicts salaries based on coefficients.
### Task 3: Additional Regression Models
- Implementation:
  - Trained Ridge Regression (`Ridge`) with L2 regularization to penalize large coefficients and reduce overfitting.
  - Trained Lasso Regression (`Lasso`) with L1 regularization to shrink insignificant coefficients to zero.
- Explanation:
- Regularization improves the model's robustness by addressing multicollinearity and reducing overfitting.
### Task 4: Model Performance Evaluation
- Implementation:
  - Evaluated models using:
    - `MAE` (Mean Absolute Error): Measures average prediction errors.
    - `MSE` (Mean Squared Error): Penalizes larger errors more.
    - `RMSE` (Root Mean Squared Error): Similar to MSE but in the same units as the target.
    - `R²` (Coefficient of Determination): Measures how well the model explains the variance in the data.
    - Compared the metrics for all three models and identified Ridge Regression as the best performer.
  - Explanation:
    - Metrics evaluate the accuracy and reliability of the predictions. Ridge Regression outperformed other models due to its balance of accuracy and regularization. 
### Task 5: Clustering
- Implementation:
  - Selected BasePay and the first 5 encoded job titles to avoid high dimensionality.
  - Standardized features using StandardScaler to ensure clustering isn't biased by scale.
  - Performed `K-Means` clustering with 3 clusters using KMeans.
  - Visualized clusters in 2D using PCA (Principal Component Analysis) and a scatter plot.
- Explanation:
  - Clustering groups employees into similar categories based on salary patterns, revealing systemic biases or trends in pay distribution.
### Task 6: Cluster Analysis
- Implementation:
  - Computed average BasePay, TotalPayBenefits, and predicted pay for each cluster.
  - Highlighted differences across clusters, identifying high, moderate, and low-paying groups.
  - Compared predicted values from the Ridge Regression model across clusters.
- Explanation:
  - Analyzing clusters helps understand pay distribution and fairness, revealing gaps that may need policy adjustments.
  - Simplified Code Walkthrough
- Data Analysis:
  - Visualizations: Histograms, boxplots, and a correlation heatmap show salary distributions and relationships.
- Feature Selection:
  - Selected BasePay and JobTitle for predictions based on their strong correlations with TotalPayBenefits.
- Linear Models:
  - Ridge Regression was chosen as the best model based on evaluation metrics (highest R²).
- Clustering:
  - K-Means identified groups (e.g., high, moderate, low earners), visualized with PCA.
- Example Report Insight
  - Cluster 0 (High-Paying Jobs):
    - Average BasePay: $107,883.
    - Includes roles like Chiefs and Directors.
  - Cluster 1 (Moderate-Paying Jobs):
    - Average BasePay: $42,372.
  - Cluster 2 (Low-Paying Jobs):
    - Average BasePay: $37,627.
  - Policy Recommendations:
- Adjust pay for low earners to improve fairness.
  - Regularize coefficients to ensure equitable salary computations.











