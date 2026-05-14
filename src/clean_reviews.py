from pyspark.sql.functions import (
    lower,
    regexp_replace,
    trim,
    col,
    when,
    size,
    split,
    concat_ws
)

from pyspark.ml.feature import Tokenizer, StopWordsRemover


def clean_reviews(reviews):

    # Select needed columns
    reviews_clean = reviews.select(
        "review_id",
        "user_id",
        "business_id",
        "stars",
        "date",
        "text",
        "useful",
        "funny",
        "cool"
    )

    # Handle nulls
    reviews_clean = reviews_clean.fillna({
        "stars": 0,
        "text": "",
        "useful": 0,
        "funny": 0,
        "cool": 0
    })

    # Lowercase
    reviews_clean = reviews_clean.withColumn(
        "clean_text",
        lower(col("text"))
    )

    # Remove URLs
    reviews_clean = reviews_clean.withColumn(
        "clean_text",
        regexp_replace(col("clean_text"), r"http\\S+|www\\S+", "")
    )

    # Remove punctuation/special chars
    reviews_clean = reviews_clean.withColumn(
        "clean_text",
        regexp_replace(col("clean_text"), r"[^a-zA-Z\\s]", " ")
    )

    # Remove extra spaces
    reviews_clean = reviews_clean.withColumn(
        "clean_text",
        regexp_replace(col("clean_text"), r"\\s+", " ")
    )

    reviews_clean = reviews_clean.withColumn(
        "clean_text",
        trim(col("clean_text"))
    )

    # Tokenization
    tokenizer = Tokenizer(
        inputCol="clean_text",
        outputCol="words"
    )

    reviews_clean = tokenizer.transform(reviews_clean)

    # Stopword removal
    remover = StopWordsRemover(
        inputCol="words",
        outputCol="filtered_words"
    )

    reviews_clean = remover.transform(reviews_clean)

    # Rebuild cleaned sentence
    reviews_clean = reviews_clean.withColumn(
        "clean_text_no_stopwords",
        concat_ws(" ", "filtered_words")
    )

    # Sentiment labels
    reviews_clean = reviews_clean.withColumn(
        "sentiment",
        when(col("stars") >= 4, "positive")
        .when(col("stars") == 3, "neutral")
        .otherwise("negative")
    )

    # Word count
    reviews_clean = reviews_clean.withColumn(
        "word_count",
        size(split(col("clean_text_no_stopwords"), " "))
    )

    # Remove very short reviews
    reviews_clean = reviews_clean.filter(
        col("word_count") >= 3
    )

    return reviews_clean