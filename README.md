# 🌱 Soil Classification Challenges - Image-Based ML

This repository contains solutions for two image-based machine learning challenges focused on soil classification. Both challenges involved analyzing soil images and applying deep learning techniques to achieve the desired classification outcomes.

---

## 📦 Challenge 1: Soil Type Classification

### 🧠 Objective

Classify each soil image into one of the **four soil types**:

* 🌾 Alluvial soil
* 🌑 Black soil
* 🧱 Clay soil
* 🔴 Red soil

### 📁 Dataset Structure

#### Training Set

* A directory `train/` containing labeled soil images.
* Labels provided in a CSV file with:

  * `image_id`: Unique image identifier
  * `soil_type`: Corresponding soil category

#### Test Set

* A directory `test/` containing unlabeled images.
* A CSV file lists `image_id` for which predictions are required.

#### Image Details

* Varying resolutions
* Preprocessing involved resizing to **224×224** to ensure model compatibility.

### 🧪 Approach

* Image preprocessing and normalization
* CNN-based model development (e.g., ResNet, EfficientNet)
* Cross-validation to improve robustness
* Final predictions submitted in the required CSV format.

---

## 🌍 Challenge 2: Soil or Not Classification

### 🧠 Objective

Classify images as either **"Soil"** or **"Not Soil"**.

### 📁 Dataset Structure

* Binary classification problem with labeled images.
* Images may contain visual noise or non-soil elements requiring strong feature discrimination.

### 🧪 Approach

* Custom data augmentation to improve generalization
* CNN-based binary classifier
* Threshold tuning to maximize F1 score and minimize false positives/negatives.

---

## ✅ Status

Both challenges have been **successfully completed**, with models trained, evaluated, and predictions submitted.

---

## 🚀 Technologies Used

* Python
* TensorFlow / PyTorch
* OpenCV, NumPy, Pandas
* Matplotlib / Seaborn (for visualization)
* Scikit-learn (for metrics and evaluation)

---

## Author - Ayush Gupta
