# Day 106 - Model Evaluation & Error Analysis

Today I evaluated my SMS Spam Detection model using **TF-IDF and Multinomial Naive Bayes**.

The goal was to understand how well the model identifies spam and legitimate messages, inspect its mistakes, and study the spam probabilities of messages it failed to detect.

## Dataset Split

The SMS Spam Collection dataset contains **5,572 messages**.

| Dataset | Messages |
|---|---:|
| Training | 3,342 |
| Validation | 1,115 |
| Testing | 1,115 |
| **Total** | **5,572** |

**Vocabulary size:** 6,583 features

## Model Performance

<badge color="success">95.16% accuracy</badge>

The reported evaluation results were:

| Metric | Ham | Spam |
|---|---:|---:|
| Precision | 0.95 | 1.00 |
| Recall | 1.00 | 0.64 |
| F1-score | 0.97 | 0.78 |
| Support | 965 | 150 |

**Overall accuracy:** 95.16%

### Understanding the Results

- The model correctly identified all 965 legitimate messages in the evaluation set.
- It correctly detected 96 out of 150 spam messages.
- It missed 54 spam messages.
- No legitimate messages were incorrectly classified as spam.

The spam precision of 1.00 means that all messages predicted as spam in this evaluation set were actually spam. However, spam recall was 0.64, meaning the model detected 64% of the actual spam messages.

## Confusion Matrix

```text
[[965   0]
 [ 54  96]]
```

| Actual / Predicted | Ham | Spam |
|---|---:|---:|
| Ham | 965 | 0 |
| Spam | 54 | 96 |

- **True Negatives:** 965
- **False Positives:** 0
- **False Negatives:** 54
- **True Positives:** 96

## Misclassification Analysis

The model made **54 misclassifications**, all of which were missed spam messages.

Some examples included:

- Valentine's Day promotional offers
- Online auction notifications
- Dating service invitations
- Mobile content and game promotions
- Reward and prize messages
- Promotional messages containing phone numbers and subscription details

### Important Observation

The model detected many obvious spam messages but missed some promotional messages with less obvious wording.

This suggests that the model may need further improvement in recognizing different types of spam messages.

## Spam Probability Analysis

I also examined the spam probabilities assigned to the 54 missed spam messages.

| Statistic | Spam Probability |
|---|---:|
| Count | 54 |
| Mean | 0.234170 |
| Standard Deviation | 0.157195 |
| Minimum | 0.003841 |
| 25th Percentile | 0.096098 |
| Median | 0.237673 |
| 75th Percentile | 0.367829 |
| Maximum | 0.492363 |

### Highest Spam Probability Among Missed Messages

The highest spam probability was approximately **0.4924**, belonging to a promotional reward message.

Even the highest-probability missed spam message remained below the default 0.5 classification threshold.

This indicates that the default threshold may be worth investigating.

## Key Learnings

- Learned how to evaluate a classification model.
- Understood precision, recall, F1-score and support.
- Interpreted a confusion matrix.
- Identified false negatives and false positives.
- Analyzed messages that the model classified incorrectly.
- Explored spam probability values using `predict_proba()`.
- Understood that high accuracy alone does not tell the whole story.

## Next Steps

- Experiment with different classification thresholds.
- Compare precision, recall, F1-score and false positives at different thresholds.
- Select a threshold using validation results.
- Retrain the final model using the training and validation data.
- Evaluate the finalized model on the untouched test set.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Multinomial Naive Bayes
- Model Evaluation Metrics