# Supervised Machine Learning with Python: Linear Regression #

_Regression_ is a supervised machine learning technique which is used to predict continuous values (as opposed to _classification_). The ultimate goal of the regression algorithm is to plot a best-fit line or a curve between the data. The three main metrics that are used for evaluating the trained regression model are variance, bias and error.

Linear regression fits a linear model with coefficients $w = (w_1, \dots, w_p)$  to minimize the residual sum of squares between the observed targets in the dataset, and the targets predicted by the linear approximation. Mathematically it solves a problem of the form:

$$
 \min_{w} || Xw - y||_2^2
$$

In this lesson we will predict world happiness ranking from (perception of) corruption. Data are derived from the [World Happiness Report](https://worldhappiness.report/)

Start by importing your depedencies

```py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
```

and reading the data

```py
print(f'[INFO] Preparing data...')
df = pd.read_csv(dpath)
X = df.loc[:,['Ladder score', 'Perceptions of corruption']].values
print(f'[INFO] Training regression model')
```

before training the model, we standardize the variables in order to make the regression coefficient identical to Pearson's correlation coefficient $\rho$. The standard score of a sample $x$ is calculated as:

$$
z = \frac{(x - u)}{s}
$$

where $u$ is the mean of the training samples and $s$ is the standard deviation of the training samples.


```py
scaler = StandardScaler()
scaler.fit(X)
X_sd = scaler.transform(X)
x = X_sd[:,1].reshape(-1, 1)
y = X_sd[:,0].reshape(-1, 1)
```

We split in training and test data

```py
X_train, X_test, y_train, y_test = train_test_split(
        x, y, 
        test_size=0.25, 
        random_state=23
        )   
```

we are now ready to train the regression model

```py
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
```

and finally test the model

```py
y_pred = reg.predict(X_test)
print(f'Coefficients: \n {reg.coef_}')
print(f'Mean squared error: {mean_squared_error(y_test, y_pred)}')
print(f'Coefficient of determination: {r2_score(y_test, y_pred)}')
```

# Supervised Machine Learning with Python: Multinomial Logistic Regression #

Logistic regression, despite its name, is a linear model for _classification_ rather than _regression_. Logistic regression is also known logit regression, maximum-entropy classification (MaxEnt) or the log-linear classifier. In this model, the probabilities describing the possible outcomes of a single trial are modeled using a logistic function.

In the binary case the logistic regression predicts the probability of the positive class $P(y_i = 1|X_i)$ (assumzing $y$ takes values in the set $\{0, 1\}$) as

$$
\hat{p}(X_i) = \text{expit}(X_iw + w_0) = \frac{1}{1 + \text{exp}(-X_i w - w_0)}
$$

As an optimization problem, binary class logistic regression with regularization term $r(w)$ minimizes the following cost function:

$$
min_{w} C \sum_{i=1}^{n} (-y_i \log(\hat{p}(X_i)) - (1-y_i)\log (1 - \hat{p} (X_i))) + r(w)
$$

`scikit-learn` provides regularization with l1, l2, and ElasticNet

The binary case extends to $K$ classes leading to multinomial regression 










