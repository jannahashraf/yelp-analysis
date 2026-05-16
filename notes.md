## Train the Model
``spark-submit --master local[4] src/sentiment_train.py --input /user/yelp/cleaned/ --model-output models/sentiment_model``

## Predict a Single Review
``spark-submit src/predict_sentiment.py --model models/sentiment_model --review "The food was amazing!"``


## Run in Jupyter
``jupyter notebook notebooks/sentiment_training.ipynb``

## Run as Python script
``jupyter nbconvert --to script notebooks/sentiment_training.ipynb``

``spark-submit notebooks/sentiment_training.py``


## any changes occurs
``git status``
``git pull``
``git add ./notebooks/name of the file``
``git commit -m "msg"``
``git push``