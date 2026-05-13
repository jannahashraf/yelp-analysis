# CSCI461 Big Data Project: Yelp Reviews Sentiment Analysis & Business Ranking

## 📌 Project Overview

| **Field** | **Details** |
|-----------|-------------|
| **Course** | CSCI461: Introduction to Big Data (Spring 2026) |
| **Project Title** | Yelp Reviews Sentiment Analysis and Business Ranking with Fake Review Detection |

---

## 📖 Phase #1: Project Idea, Objective, and Dataset

### Project Idea

In the digital age, businesses struggle to manually analyze thousands of online reviews to understand customer sentiment and detect fraudulent feedback. Fake reviews distort business reputations and mislead consumers. This project addresses both challenges by building a **scalable big data pipeline** that:

1. **Automatically classifies review sentiment** (positive/negative) using Spark MLlib
2. **Detects fake/spam reviews** using behavioral and textual features
3. **Generates spam-filtered business rankings** to reflect genuine customer satisfaction

The project processes the **Yelp Open Dataset** (4GB–9GB of semi-structured JSON), demonstrating distributed data processing with **Apache Hadoop (HDFS)** and **Apache Spark** on a local cluster or Docker containers.

### Objective (SMART)

| **Criterion** | **Target** |
|---------------|-------------|
| **Specific** | Build a sentiment classifier and spam detector for Yelp reviews |
| **Measurable** | Achieve ≥85% sentiment accuracy and ≥80% spam detection precision |
| **Achievable** | Using Spark MLlib on a 4-node local cluster or Docker setup |
| **Relevant** | Real-world application for businesses and consumers |
| **Time-bound** | Complete within 6 days following project milestones |

**Success Metrics:**
- Sentiment classification accuracy: **≥85%**
- Spam detection precision: **≥80%**
- Business ranking generation: **Top 100 businesses by city**
- Pipeline runtime: **≤45 minutes on 4GB dataset**

### Dataset

| **Property** | **Details** |
|--------------|-------------|
| **Source** | [Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/) (official) / [Kaggle Mirror](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset) |
| **Size** | 4GB (official) – 9GB (Kaggle) |
| **Format** | Semi-structured JSON (newline-delimited) |
| **Contents** | ~8 million reviews, ~160k businesses, ~1.5M users |
| **Challenges** | Missing values, nested JSON, text preprocessing, spam outliers |
| **Legal** | Allowed for academic/research use; no PII |

---

## 👥 Team Roles and Responsibilities

> **⚠️ IMPORTANT: All 5 members write code and contribute to algorithms.**
> 
> While each member has a **primary focus area**, every team member is expected to:
> - Write production-quality Python/Spark code for their components
> - Debug and test their assigned modules
> - Participate in code reviews via GitHub Pull Requests
> - Contribute to algorithm design decisions during team meetings
> - Help solve technical challenges across the entire pipeline
> - Document their code with clear comments and docstrings
> 
> The division below shows **primary ownership** of specific deliverables, but **collaborative coding** is expected throughout the project. All members will have their code merged into the `develop` branch via pull requests.

---

### Member 1 – Data Engineering & Pipeline Setup

| **Primary Focus** | **Technical Deliverables (Owner)** |
|-------------------|-----------------------------------|
| **Idea & Data Hunting** | |
| | - Write project concept and problem statement |
| | - Download Yelp dataset and verify data integrity |
| | - Set up local Hadoop HDFS environment |
| | - Load raw JSON files into HDFS |
| | - Create GitHub repository with branch structure |
| | - Document dataset characteristics and legal compliance |

| **Code & Algorithms to Write** | **Files/Modules Responsible For** |
|--------------------------------|----------------------------------|
| | - HDFS data loading scripts |
| | - Data exploration and profiling notebook |
| | - JSON schema definition for Spark reads |
| | - Data validation and integrity tests |
| | - Partitioning strategy for raw data |

---

### Member 2 – Architecture & Project Planning

| **Primary Focus** | **Technical Deliverables (Owner)** |
|-------------------|-----------------------------------|
| **Planning & Setup** | |
| | - Create Gantt chart and project timeline |
| | - Draw system architecture diagram |
| | - Write risk assessment and mitigation strategies |
| | - Set up Docker-based Spark cluster |
| | - Configure Spark session with optimal parameters |
| | - Define project milestones and deliverables |

| **Code & Algorithms to Write** | **Files/Modules Responsible For** |
|--------------------------------|----------------------------------|
| | - Docker Compose configuration for cluster |
| | - Spark session manager and configuration files |
| | - End-to-end pipeline orchestration script |
| | - Cluster connection and health check tests |
| | - Broadcast variable utilities for stopwords |

---

### Member 3 – Data Preprocessing & Security

| **Primary Focus** | **Technical Deliverables (Owner)** |
|-------------------|-----------------------------------|
| **Data Prep & Cleaning** | |
| | - Read JSON from HDFS using Spark DataFrames |
| | - Handle missing values (imputation or removal) |
| | - Remove outliers (extreme ratings, new users) |
| | - Tokenize review text and remove punctuation |
| | - Remove stopwords using NLTK/Spark |
| | - Add derived features (review length, word count) |
| | - Save cleaned data as Parquet with compression |
| | - Implement basic data security measures |
| | - Document all preprocessing steps |

| **Code & Algorithms to Write** | **Files/Modules Responsible For** |
|--------------------------------|----------------------------------|
| | - Main data cleaning pipeline script |
| | - Preprocessing utilities (tokenization, stopwords) |
| | - Feature engineering functions |
| | - Outlier detection and removal logic |
| | - Data quality validation tests |
| | - Missing value imputation strategies |

---

### Member 4 – Algorithms & Model Implementation

| **Primary Focus** | **Technical Deliverables (Owner)** |
|-------------------|-----------------------------------|
| **Algorithms & Coding** | |
| | - Implement sentiment analysis using Logistic Regression with TF-IDF |
| | - Perform hyperparameter tuning via grid search |
| | - Implement spam detection using Random Forest |
| | - Engineer spam features (extreme ratings, duplicates, short length, frequency) |
| | - Implement business ranking with weighted scoring formula |
| | - Save trained models to disk for reuse |
| | - Optimize performance (caching, broadcasting, partitioning) |
| | - Write clean, reusable, documented production code |

| **Code & Algorithms to Write** | **Files/Modules Responsible For** |
|--------------------------------|----------------------------------|
| | - Sentiment analysis training pipeline |
| | - Spam detection model with Random Forest |
| | - Business ranking and scoring logic |
| | - Cross-validation and hyperparameter tuning |
| | - Model persistence and loading utilities |
| | - Unit tests for model functions |

---

### Member 5 – Results, Visualization & Documentation

| **Primary Focus** | **Technical Deliverables (Owner)** |
|-------------------|-----------------------------------|
| **Results & Sharing** | |
| | - Run final pipeline on full dataset |
| | - Calculate accuracy, precision, recall, F1-score |
| | - Generate confusion matrix for sentiment classifier |
| | - Create bar chart of top 10 businesses |
| | - Generate word clouds for positive vs negative reviews |
| | - Create heatmap of spam review patterns |
| | - Write final README with results interpretation |
| | - Prepare presentation slides and final report |

| **Code & Algorithms to Write** | **Files/Modules Responsible For** |
|--------------------------------|----------------------------------|
| | - Metrics calculation and evaluation script |
| | - Visualization module (all charts and plots) |
| | - Final business ranking table generation |
| | - Results export to CSV and JSON formats |
| | - Performance benchmarking utilities |
| | - Final report and presentation slides |

---

## 📅 Phase #2: Project Planning, Design, and Timeline

### Gantt Chart

| **Phase** | **Task** | **Owner** | **Day 1** | **Day 2** | **Day 3** | **Day 4** | **Day 5** | **Day 6** |
|-----------|----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| **Phase 1** | Project Idea & Dataset | Member 1 | ████████ | | | | | |
| | Planning & Architecture | Member 2 | ████████ | | | | | |
| **Phase 2** | Data Cleaning & Prep | Member 3 | | ████████ | ████████ | | | |
| | Algorithms & Models | Member 4 | | | ████████ | ████████ | | |
| **Phase 3** | Results & Visualization | Member 5 | | | | | ████████ | ████████ |
| | Final Paper & README | All | | | | | | ████████ |

### Resource Allocation (Local Machine / Docker)

| **Resource** | **Specification** |
|--------------|-------------------|
| **Hardware** | Any laptop/desktop with 8GB+ RAM, 20GB free disk |
| **Software** | Docker Desktop, or local Hadoop (3.3+) + Spark (3.4+) |
| **Cluster Mode** | Docker Compose with 1 master + 3 worker nodes (simulated) |
| **Storage** | HDFS in Docker volumes or local filesystem |

### Risk Assessment

| **Risk** | **Probability** | **Impact** | **Mitigation Strategy** |
|----------|----------------|------------|-------------------------|
| Dataset too large for local machine | Medium | High | Use 20% sample for development; full run overnight |
| Spark out-of-memory errors | Medium | Medium | Tune partitioning; enable disk spill |
| Merge conflicts on GitHub | High | Medium | Daily `git pull`; small PRs; regular communication |
| Model accuracy below target | Medium | Medium | Iterative tuning; try alternative algorithms |
| Docker not working on some devices | Low | Medium | Provide local Hadoop installation alternative |
| Member unavailable due to illness | Low | High | Code reviews ensure knowledge sharing |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     LOCAL DEVELOPMENT MACHINE                    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                 DOCKER / LOCAL CLUSTER                       │ │
│  │                                                              │ │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │ │
│  │  │  HDFS    │  │  Spark   │  │  Spark   │  │  Spark   │    │ │
│  │  │ (NameNode│  │ (Master) │  │ (Worker1)│  │ (Worker2)│    │ │
│  │  │ +Data)  │  │          │  │          │  │          │    │ │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘    │ │
│  │       │             │             │             │           │ │
│  │       └─────────────┴─────────────┴─────────────┘           │ │
│  │                        │                                     │ │
│  │                        ▼                                     │ │
│  │  ┌──────────────────────────────────────────────────────┐   │ │
│  │  │              Processing Pipeline                      │   │ │
│  │  │  Raw JSON → Cleaning → Sentiment Model → Ranking     │   │ │
│  │  │                    ↓                                  │   │ │
│  │  │              Spam Detection → Filtered Results        │   │ │
│  │  └──────────────────────────────────────────────────────┘   │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                              │                                    │
│                              ▼                                    │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                    GITHUB REPOSITORY                         │ │
│  │  - All code (src/)              - Results (CSV, plots)      │ │
│  │  - Documentation (README)       - Pull Requests & Reviews   │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Technology Justification

| **Technology** | **Why Used** | **Big Data Alignment** |
|----------------|--------------|------------------------|
| **HDFS** | Distributed storage for large JSON files | Core Hadoop component – required by rubric |
| **Apache Spark** | In-memory processing for iterative ML | Faster than MapReduce for ML algorithms |
| **Spark MLlib** | Built-in NLP and classification algorithms | Scales to large datasets natively |
| **Parquet** | Columnar storage for cleaned data | Efficient compression and query performance |
| **GitHub** | Version control and collaboration | Pull requests enforce code review |
| **Docker** | Reproducible cluster environment | Same setup across all team devices |

---

## 📊 Phase #3: Data Preprocessing & Methodology

### Data Preprocessing Steps (Led by Member 3)

| **Step** | **Method** | **Tool** |
|----------|------------|----------|
| Missing values | Drop rows with null review text | Spark DataFrame API |
| Outliers | Remove users with <5 reviews | GroupBy + filter |
| Text cleaning | Lowercase, remove punctuation, remove HTML | Spark UDF / Regex |
| Tokenization | Split on whitespace | Spark Tokenizer |
| Stopword removal | NLTK stopword list | Spark StopWordsRemover |
| Feature engineering | Review length, word count, sentiment intensity | Spark withColumn |
| Output format | Parquet with Snappy compression | DataFrame writer |

### Methodology (Led by Member 4)

#### Sentiment Analysis Pipeline

| **Component** | **Algorithm/Tool** | **Purpose** |
|---------------|-------------------|--------------|
| Text Vectorization | TF-IDF (10,000 features) | Convert text to numerical features |
| Classification | Logistic Regression | Binary sentiment (positive/negative) |
| Hyperparameter Tuning | Grid Search with 5-fold CV | Optimize regParam, elasticNetParam |
| Evaluation | Accuracy, Precision, Recall, F1-Score | Measure model performance |

#### Spam Detection Features

| **Feature** | **Description** | **Weight in Decision** |
|-------------|----------------|------------------------|
| Extreme rating | Review has 1-star or 5-star only | High |
| Short review | Text length less than 50 characters | Medium |
| Duplicate text | Same text appears in multiple reviews | High |
| High frequency | User posted >5 reviews per day | Medium |

| **Component** | **Algorithm/Tool** | **Purpose** |
|---------------|-------------------|--------------|
| Feature Assembly | VectorAssembler | Combine features into single vector |
| Classification | Random Forest (50 trees) | Detect spam reviews |
| Labeling | Rule-based (≥2 suspicious features) | Generate training labels |

#### Business Ranking Formula

| **Component** | **Weight** | **Description** |
|---------------|------------|-----------------|
| Sentiment Score | 60% | Average sentiment prediction from model |
| Normalized Rating | 30% | Average star rating (converted to 0-1 scale) |
| Volume Score | 10% | Review count normalized (capped at 100+ reviews) |

**Final Score = (Sentiment × 0.6) + (Rating/5 × 0.3) + (Volume × 0.1)**

---

## 🌍 Contribution to Community

| **Contribution Type** | **Details** |
|-----------------------|-------------|
| **Open-source code** | All code available on GitHub under MIT license |
| **Reproducible pipeline** | Docker Compose setup for anyone to replicate |
| **Educational value** | Demonstrates complete big data workflow for students |
| **Real-world impact** | Helps small businesses filter fake reviews |
| **Documentation** | Comprehensive README with setup and execution instructions |

### Ethical Considerations

| **Consideration** | **Mitigation** |
|-------------------|----------------|
| Data privacy | Dataset contains no PII (anonymized by Yelp) |
| Model bias | Document limitations; balanced training data |
| False positives in spam detection | Ranking includes confidence scores |
| Reproducibility | Full code and environment provided |

---

## 📁 Repository Structure

```
yelp-big-data/
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md      # PR template for code reviews
│   └── workflows/
│       └── test_on_push.yml          # GitHub Actions CI (Member 2)
├── config/
│   ├── spark_config.yaml             # Spark tuning (Member 2)
│   └── hyperparameters.json          # Best model params (Member 4)
├── src/
│   ├── __init__.py
│   ├── data_schema.py                # JSON schema (Member 1)
│   ├── spark_session_manager.py      # Spark session (Member 2)
│   ├── clean_yelp.py                 # Cleaning pipeline (Member 3)
│   ├── preprocessing_utils.py        # Tokenization (Member 3)
│   ├── feature_engineering.py        # Derived features (Member 3)
│   ├── sentiment_train.py            # Sentiment model (Member 4)
│   ├── spam_detector.py              # Spam detection (Member 4)
│   ├── rank_businesses.py            # Ranking logic (Member 4)
│   ├── evaluate.py                   # Metrics (Member 5)
│   └── visualize.py                  # Charts & plots (Member 5)
├── scripts/
│   ├── load_data_to_hdfs.sh          # HDFS upload (Member 1)
│   ├── run_pipeline.py               # Orchestration (Member 2)
│   └── docker-compose.yml            # Cluster setup (Member 2)
├── tests/
│   ├── test_cleaner.py               # Cleaning tests (Member 3)
│   ├── test_models.py                # Model tests (Member 4)
│   └── __init__.py
├── notebooks/
│   ├── m1_exploration.ipynb          # Data exploration (Member 1)
│   ├── m3_cleaning_debug.ipynb       # Debugging (Member 3)
│   └── m5_visualization.ipynb        # Final plots (Member 5)
├── results/
│   ├── metrics/
│   │   └── final_metrics.json        # Accuracy scores (Member 5)
│   ├── plots/
│   │   ├── confusion_matrix.png      # Member 5
│   │   ├── top_businesses.png        # Member 5
│   │   ├── wordcloud_positive.png    # Member 5
│   │   └── spam_heatmap.png          # Member 5
│   └── rankings/
│       └── top_100_businesses.csv    # Member 5
├── docs/
│   ├── dataset_info.md               # Member 1
│   ├── architecture.mmd              # Member 2
│   ├── risk_assessment.md            # Member 2
│   ├── data_quality_report.html      # Member 3
│   └── final_report.md               # Member 5
├── .gitignore
├── .env.example
├── requirements.txt
├── setup.py
└── README.md                         # This file (All members)
```

---

## 🔗 GitHub Workflow for Team Collaboration

| **Step** | **Action** | **Responsible** |
|----------|------------|-----------------|
| 1 | Create feature branch from `develop` | Each member |
| 2 | Write code and commit changes | Each member |
| 3 | Push branch to GitHub | Each member |
| 4 | Open Pull Request to `develop` | Each member |
| 5 | Request code review from another member | Each member |
| 6 | Address review comments | Each member |
| 7 | Merge PR after approval | Each member |
| 8 | Daily `git pull develop` to stay synced | Each member |

### Branch Structure

```
main (production-ready code)
  └── develop (integration branch)
       ├── feature/member1-data-hunting
       ├── feature/member2-planning
       ├── feature/member3-cleaning
       ├── feature/member4-algorithms
       └── feature/member5-results
```

---

## ✅ Expected Results Summary

| **Output** | **Description** | **Primary Owner** |
|------------|-----------------|-------------------|
| Raw data in HDFS | Yelp JSON files loaded to distributed storage | Member 1 |
| Docker cluster | Reproducible Spark/Hadoop environment | Member 2 |
| Cleaned Parquet files | Preprocessed reviews ready for modeling | Member 3 |
| Sentiment model | Trained Logistic Regression classifier | Member 4 |
| Spam detector | Trained Random Forest classifier | Member 4 |
| Business rankings | Top 100 businesses with scores | Member 4 |
| Metrics & plots | Accuracy, charts, word clouds | Member 5 |
| Final documentation | Complete README and report | All members |

---

## 📚 Rubric Alignment Summary

| **Rubric Section** | **Primary Owner** | **All Members Code?** | **Location in Repo** |
|--------------------|-------------------|----------------------|----------------------|
| Project Idea & Objective | Member 1 | Yes (reviewed by all) | README → Phase #1 |
| Dataset | Member 1 | Yes (validation code) | `docs/dataset_info.md` |
| Project Planning (Gantt, risks) | Member 2 | Yes (feedback) | README → Phase #2 |
| Design (Architecture) | Member 2 | Yes (diagram review) | README → Architecture |
| Data Lifecycle | Member 3 | Yes (cleaning code) | `src/clean_yelp.py` |
| Data Preprocessing | Member 3 | Yes (helper functions) | `src/preprocessing_utils.py` |
| Methodology (Algorithms) | Member 4 | Yes (model code) | `src/sentiment_train.py`, `src/spam_detector.py` |
| Results & Visualizations | Member 5 | Yes (plotting code) | `results/plots/`, `src/visualize.py` |
| Contribution to Community | All | Yes (documentation) | README → Contribution |

---

## ✅ Final Deliverables Checklist

| **Deliverable** | **Owner** | **Status** |
|-----------------|-----------|------------|
| GitHub repository with all code | All | ⬜ |
| Complete README (this document) | All | ⬜ |
| Raw data loaded to HDFS | Member 1 | ⬜ |
| Docker cluster configuration | Member 2 | ⬜ |
| Data cleaning pipeline | Member 3 | ⬜ |
| Sentiment model training code | Member 4 | ⬜ |
| Spam detection model code | Member 4 | ⬜ |
| Business ranking logic | Member 4 | ⬜ |
| Evaluation metrics and accuracy scores | Member 5 | ⬜ |
| Visualizations (charts, word clouds) | Member 5 | ⬜ |
| Final business rankings (CSV) | Member 5 | ⬜ |
| Final project paper (IEEE format) | All | ⬜ |
| Presentation slides | All | ⬜ |

---

**Repository:** https://github.com/YOUR_ORG/yelp-big-data  
**Last Updated:** Spring 2026  
**License:** MIT

---

*For questions, open a GitHub Issue and tag the responsible member. All members participate in coding, debugging, and code reviews.*