# Iris Flower Classification

A simple yet complete machine learning project that demonstrates basic classification techniques using the famous **Iris dataset**.

This project compares several classic machine learning algorithms to classify iris flowers into three species based on sepal and petal measurements.

## Dataset

- **Source**: UCI Machine Learning Repository (via [jbrownlee/Datasets](https://github.com/jbrownlee/Datasets))
- **Features**: 4 numeric features  
  - sepal length (cm)  
  - sepal width (cm)  
  - petal length (cm)  
  - petal width (cm)
- **Target**: 3 classes  
  - Iris Setosa  
  - Iris Versicolour  
  - Iris Virginica
- **Samples**: 150 instances (50 per class)

## Algorithms Compared

| Abbreviation | Algorithm                        | Notes                        |
|--------------|----------------------------------|------------------------------|
| LDA          | Linear Discriminant Analysis     |                              |
| KNN          | k-Nearest Neighbors              | Default parameters           |
| CART         | Decision Tree (CART)             | Default parameters           |
| NB           | Gaussian Naive Bayes             |                              |
| SVM          | Support Vector Machine           | gamma='auto'                 |

## Results (example output - your actual numbers may vary slightly)

LDA: 0.975000 (0.038730)
KNN: 0.958333 (0.040825)
CART: 0.941667 (0.053359)
NB: 0.950000 (0.055277)
SVM: 0.983333 (0.033333)


**Best model (validation set): SVM**  
Accuracy: 0.9666666666666667
Confusion Matrix:
[[11  0  0]
[ 0 12  1]
[ 0  0  6]]
Classification Report:
precision    recall  f1-score   support
Iris-setosa       1.00      1.00      1.00        11
Iris-versicolor   1.00      0.92      0.96        13
Iris-virginica    0.86      1.00      0.92         6
accuracy                               0.97        30
macro avg         0.95      0.97      0.96        30
weighted avg      0.97      0.97      0.97        30


## Project Structure
iris-classification/
├── iris.csv                  # (optional - if you want to keep local copy)
├── iris_classification.py    # Main script (the code you provided)
└── README.md


## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR-USERNAME/iris-classification.git
cd iris-classification

# 2. Install requirements (if you don't have them already)
pip install pandas matplotlib scikit-learn

# 3. Run the script
python iris_classification.py

Requirements

Python 3.6+
pandas
matplotlib
scikit-learn

License
MIT License
Feel free to use this code as a learning resource or starting point for your own machine learning projects!
Happy classifying! 🌸
