#!/usr/bin/env python3
"""
Standalone prediction script - Just input a review, get probability!
Usage: python src/predict_sentiment.py --model models/sentiment_model --review "Great food!"
"""

import argparse
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel


def predict_single_review(model_path, review_text):
    """Predict sentiment probability for a single review"""
    
    spark = SparkSession.builder.appName("PredictSentiment").getOrCreate()
    
    # Load model
    model = PipelineModel.load(model_path)
    
    # Create DataFrame
    df = spark.createDataFrame([(review_text,)], ["text_clean"])
    
    # Predict
    prediction = model.transform(df)
    
    # Get probability (positive class)
    prob_positive = prediction.select("probability").collect()[0][0][1] * 100
    prob_negative = 100 - prob_positive
    
    # Get label
    if prob_positive >= 90:
        label = "EXCELLENT"
    elif prob_positive >= 75:
        label = "GOOD"
    elif prob_positive >= 50:
        label = "NOT BAD"
    elif prob_positive >= 25:
        label = "BAD"
    else:
        label = "TERRIBLE"
    
    spark.stop()
    
    # Print result
    print("\n" + "="*50)
    print(f"📝 Review: {review_text}")
    print("="*50)
    print(f"📊 {prob_positive:.1f}% positive, {prob_negative:.1f}% negative")
    print(f"⭐ Rating: {label}")
    print("="*50)
    
    return {
        "review": review_text,
        "positive_percent": round(prob_positive, 1),
        "negative_percent": round(prob_negative, 1),
        "rating": label
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="Path to trained model")
    parser.add_argument("--review", required=True, help="Review text to analyze")
    args = parser.parse_args()
    
    predict_single_review(args.model, args.review)