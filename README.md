# Otto product classification
This is done as a part of Graduate Course Project, for Introduction to Machine Learning EL-GY 9123.

**Problem statement:**

Otto Group is one of the world’s biggest e-commerce companies. Their data was generously made available by Otto Group and Kaggle. It has 200,000 different products 93 independent features. The objective is to build a predictive model which is able to classify the product into one of the 10 different categories.


---------------------------
## Initial Analysis of the data

The data is observed to check if all the features  are relevant for prediction. It turns out all the features are important. Also, data was normalized to bring them at the same scale.

---------------------------
## Try to use different Machine Learning Models with different parameters for each repective model
Algorithms considered for predictive modeling were SVM, Neural Networks, XgBoost (gradient boosting) and Random Forests.
A table showing minimum Logloss is obtained after trying different algorithms. 

| Model          | Log Loss       | Accuracy
| :---           |     :---:      |   ---:
| SVM            | 0.542290       | 0.76
| Nueral Network | 0.523256       | 0.79
| XG boost       | 0.531245       | 0.78
| Random forest  | 0.501333       | 0.83

It can be observed from the table that random forests produce better results than any other model. But we still wanted to increase the accuracy and reduce the logloss. For that, Ensemble Learning approach was used.

---------------------------
## Ensemble Learning approach to try and combine the models
Model ensembling is a very powerful technique used nowadays very frequently to improve the results. It can be used in both classification and regression. Learning by means of ensembling different machine learning algorithms is called ensemble learning. In simple terms, it is learning by committee or crowd. You train a large number of models and then combine the predictions to come to a conclusion. <br>
The method of combining the predictions depends on the choice of models used for training. If the models are homogeneous, that is all the trained models are using the same algorithm with different parameters of course, for example Decision Tree, then boosting can be used. These are the most widely used techniques. If the trainers are heterogeneous, that is a combination of algorithms is used for training, example DT, SVM, Neural Network, etc, then something called bagging can be used. In bagging (stands for Bootstrap Aggregating), on top of all the predictions obtained after training the model on individual models, another model is trained which ultimately decides the final prediction.
Here's is an excellent link to understanding more about ensemble learning and why it works:
https://mlwave.com/kaggle-ensembling-guide/ 

What we are using here is bagging where weighted average of SVM, Random Forest, xgboost and Nueral Network predictions was used to make final stage predictions. The model with highest individual accuracy will get more weightage than the other models. There is no limit on the number of models to be used in first stage. 
With the four models we used, and then using Bagging, our results ere improved. The new LogLoss was 0.438509 with the new accuracy was 0.88. 
The results can be further improved by using more models in the first stage to capture more details in the data. The highest Logloss obtained in this problem according to Kaggle is 0.38.

| Model          | Log Loss       | 
| :---           |     :---:      |
| Ensemble model | 0.438593       |

---------------------------

Please go through the wiki for detailed instructions of the project. 
