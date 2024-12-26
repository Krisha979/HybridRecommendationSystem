# Hybrid Recommendation System

This project implements a **Hybrid Recommendation System** that combines collaborative filtering, genre-based similarity, and tag-based similarity to provide personalized and diverse movie recommendations.

## **Features**
- **Collaborative Filtering**: Utilizes both user-based and item-based approaches.
- **Content-Based Filtering**: Incorporates genre information for relevance.
- **Tag-Based Similarity**: Leverages community-driven tags for granular recommendations.
- **Hybrid Approach**: Combines multiple methods to balance personalization and diversity.

## **Project Workflow**
1. **Exploratory Data Analysis (EDA)**: Extracted insights from the dataset.
2. **Data Preprocessing**: Prepared the data for modeling.
3. **Model Implementation**:
    - Collaborative Filtering
    - Content-Based Filtering (Genre Similarity)
    - Tag-Based Similarity
    - Hybrid Recommendation System
4. **Evaluation**: Assessed performance using RMSE, precision, and recall.
5. **Insights and Implications**: Highlighted findings with business impact.

## **Results**
- Lowest RMSE achieved: **0.9123** (Item-based collaborative filtering).
- Hybrid model precision: **0.7** (Top 10 recommendations).
- Challenges: Improving recall and addressing sparsity.

## **Requirements**
Install the required libraries using:
```bash
pip install scikit-surprise
