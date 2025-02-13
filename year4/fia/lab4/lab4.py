import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Print scikit-learn version
print(f"Scikit-learn version: {sklearn.__version__}")

# Step 1: Import the data
df = pd.read_csv('luna_city_salaries.csv', low_memory=False)

# Display first two and last two rows
print("\nFirst two rows of the dataset:")
print(df.head(2))
print("\nLast two rows of the dataset:")
print(df.tail(2))
print("\nThese are the first and last two rows of the dataset, giving us an initial look at the data structure.")

# Step 2: Data Preprocessing
# Convert numeric columns to appropriate data types
numeric_cols = ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay', 'TotalPayBenefits']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Handle missing values
df = df.dropna(subset=numeric_cols + ['JobTitle'])
print("\nData preprocessing completed. Numeric columns converted and missing values handled.")

# Step 3: Data Analysis and Visualization
# Basic statistics
print("\nBasic Statistics:")
print(df[numeric_cols].describe())
print("\nThe basic statistics provide insights into the distribution and range of the numeric variables.")

# Distribution plots
print("\nGenerating distribution plots for numeric variables...")
for col in numeric_cols:
    plt.figure()
    sns.histplot(df[col], bins=30, kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()
    print(f"Displayed distribution plot for {col}.")

# Boxplots to detect outliers
print("\nGenerating boxplots to detect outliers...")
for col in numeric_cols:
    plt.figure()
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.xlabel(col)
    plt.show()
    print(f"Displayed boxplot for {col}.")

# Correlation matrix
print("\nCorrelation Matrix:")
corr = df[numeric_cols].corr()
print(corr)
print("\nThe correlation matrix shows the relationships between numeric variables.")

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
print("Displayed heatmap of the correlation matrix.")

# Step 4: Feature Selection
print("\nFeature Selection:")
print("We'll use 'JobTitle' and 'BasePay' as features to predict 'TotalPayBenefits'.")
print("This decision is based on the strong correlation between 'BasePay' and 'TotalPayBenefits' observed in the correlation matrix.")

# Encode 'JobTitle' using One-Hot Encoding
print("\nEncoding 'JobTitle' using One-Hot Encoding...")
ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
job_title_encoded = ohe.fit_transform(df[['JobTitle']])

# Create DataFrame from encoded job titles
job_title_df = pd.DataFrame(job_title_encoded, columns=ohe.get_feature_names_out(['JobTitle']))

# Prepare features and target variable
X = pd.concat([df[['BasePay']].reset_index(drop=True), job_title_df], axis=1)
y = df['TotalPayBenefits'].reset_index(drop=True)

print("\nFeatures after encoding:")
print(X.head())
print("\nThe features now include 'BasePay' and one-hot encoded 'JobTitle' columns.")

# Step 5: Split data into training and testing sets
print("\nSplitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape}")
print(f"Testing set size: {X_test.shape}")
print("Data split completed. 80% for training and 20% for testing.")

# Step 6: Train Linear Regression Model
print("\nTraining Linear Regression model...")
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

# Display model coefficients
print("\nLinear Regression Coefficients:")
coefficients = pd.Series(lr.coef_, index=X.columns)
print(coefficients.sort_values(ascending=False).head(10))
print("\nThese coefficients indicate the impact of each feature on the prediction.")

# Step 7: Train Ridge and Lasso Regression Models
print("\nTraining Ridge Regression model...")
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)

print("\nTraining Lasso Regression model...")
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
y_pred_lasso = lasso.predict(X_test)

# Step 8: Evaluate Models
def print_metrics(y_true, y_pred, model_name):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    print(f'\n{model_name} Performance:')
    print(f'MAE: {mae:.2f}')    # Mean Absolute Error
    print(f'MSE: {mse:.2f}')    # Mean Squared Error
    print(f'RMSE: {rmse:.2f}')  # Root Mean Squared Error
    print(f'R^2 Score: {r2:.4f}')  # R-squared Score

print_metrics(y_test, y_pred_lr, 'Linear Regression')
print_metrics(y_test, y_pred_ridge, 'Ridge Regression')
print_metrics(y_test, y_pred_lasso, 'Lasso Regression')
print("\nModel evaluation completed. Metrics help in comparing model performances.")

# Step 9: Clustering
print("\nPerforming KMeans Clustering...")
# For clustering, we'll use 'BasePay' and the first few job title features to avoid high dimensionality
clustering_features = pd.concat([df[['BasePay']].reset_index(drop=True), job_title_df.iloc[:, :5]], axis=1)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(clustering_features)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
df['Cluster'] = clusters

# Display cluster centers
print("\nCluster Centers:")
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=clustering_features.columns)
print(cluster_centers_df)
print("\nCluster centers represent the average feature values for each cluster.")

# Visual representation using PCA
print("\nVisualizing clusters using PCA...")
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)
df['PC1'] = principal_components[:, 0]
df['PC2'] = principal_components[:, 1]

plt.figure(figsize=(10, 6))
sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=df, palette='viridis')
plt.title('Clusters of Employees')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
print("Displayed PCA scatter plot to visualize clusters.")

# Step 10: Analyze Clusters
print("\nCluster Analysis:")
df['PredictedPay'] = lr.predict(X)

numeric_cols_for_groupby = ['BasePay', 'TotalPayBenefits', 'PredictedPay']
cluster_groups = df.groupby('Cluster')[numeric_cols_for_groupby].mean()
print(cluster_groups)
print("\nThe cluster analysis shows the average 'BasePay', 'TotalPayBenefits', and 'PredictedPay' for each cluster.")

# Analyze predicted values by the best model
models = {
    'Linear Regression': r2_score(y_test, y_pred_lr),
    'Ridge Regression': r2_score(y_test, y_pred_ridge),
    'Lasso Regression': r2_score(y_test, y_pred_lasso)
}
best_model_name = max(models, key=models.get)
best_model_r2 = models[best_model_name]
print(f"\nBest Model: {best_model_name} with R^2 Score: {best_model_r2:.4f}")
print("The best model is chosen based on the highest R^2 Score.")

# Compare predicted pay across clusters
print("\nAverage Predicted Pay per Cluster:")
cluster_predictions = df.groupby('Cluster')['PredictedPay'].mean()
print(cluster_predictions)
print("\nThis shows how the predicted pay varies across different clusters.")

# Display sample predictions
print("\nSample Predictions:")
sample_predictions = df[['JobTitle', 'BasePay', 'TotalPayBenefits', 'PredictedPay', 'Cluster']].head(10)
print(sample_predictions)
print("\nThese are sample predictions showing actual and predicted 'TotalPayBenefits' along with the cluster assignment.")
