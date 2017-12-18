# Otto product classification
Graduate course project, Introduction to Machine Learning, NYU Tandon.

**Problem statement:**

Dataset from Otto Group (one of the world’s biggest e-commerce companies) with 93 features for more than 200,000 products. The objective is to build a predictive model which is able to distinguish between its  the main 10 product categories .

---------------------------
## Initial Analysis of the data

The data is observed to check if all the features  are relevant for prediction. It turns out all the features are important. Tried to add variation of the original features like Sin and log on relevant features. 

---------------------------
## Try to use different Machine Learning Models with different parameters for each repective model

A table showing minimum Logloss is obtained after trying different parameters. For simplicity,  models were taken from other open source projects to reduce the time in building the models.

| Model          | Log Loss       | 
| :---           |     :---:      |
| SVM            | 0.542290       |
| Nueral Network | 0.523256       |
| XG boost       | 0.531245       |
| Random forest  | 0.531333       |

---------------------------
## Ensemble approach to try and combine the models

Weighted average of SVM, Random forest, xgboost and nueral network was used to make prediction and the following results was obtained. The models selected here are arbitrary, for some cases the loss did not improve.

| Model          | Log Loss       | 
| :---           |     :---:      |
| Ensemble model | 0.438593       |

---------------------------
The ensemble approach can be improved by trying diffrent models and parameters. A comprehensive study has to be done to determine how they are affecting the loss.

Go through the wiki for detailed instructions of the project. 
