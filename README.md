# Otto product classification
Graduate course project, Introduction to Machine Learning, NYU Tandon.

**Problem statement:**

A dataset with 93 features for more than 200,000 products. The objective is to build a predictive model which is able to distinguish between the main 10 product categories .

---------------------------
## Initial Analysis of the data

The data is observed to check if all the features  are relevant for prediction. It turns out all the features are important. Tried to add variation of the original features like Sin and log on relevant features. 

---------------------------
## Try to use different Machine Learning Models with different parameters for each repective model

A table showing minimum Logloss is obtained after trying different parameters.

| Model          | Log Loss       | 
| :---           |     :---:      |
| SVM            | 0.542290       |
| Nueral Network | 0.523256       |
| XG boost       | 0.531245       |
| Random forest  | 0.531333       |

---------------------------
## Ensemble approach to try and combine the models



---------------------------
