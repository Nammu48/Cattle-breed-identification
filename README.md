# Cattle Breed Identification Using Deep Learning

## 📌 Project Overview

Cattle Breed Identification is a deep learning-based application that identifies the breed of cattle from an uploaded image.

The system is trained on images of **41 different cattle breeds**. It uses transfer learning with pre-trained deep learning models and provides the predicted breed along with confidence and breed-related information.

## 🎯 Objectives

- Identify cattle breeds automatically from images.
- Reduce manual effort in breed identification.
- Compare different deep learning architectures.
- Provide useful information about the predicted breed.
- Develop a simple graphical user interface for users.

## 🐄 Dataset

The dataset contains images belonging to **41 cattle breeds**.

The dataset was divided into:
- Training set – 80%
- Testing set – 20%
- Training data was further divided into training and validation sets.

### Cattle Breeds

Alambadi, Amritmahal, Ayrshire, Banni, Bargur, Bhadawari, Brown Swiss, Dangi, Deoni, Gir, Guernsey, Hallikar, Hariana, Holstein Friesian, Jaffrabadi, Jersey, Kangayam, Kankrej, Kasargod, Kenkatha, Kherigarh, Khillari, Krishna Valley, Malnad Gidda, Mehsana, Murrah, Nagori, Nagpuri, Nili Ravi, Nimari, Ongole, Pulikulam, Rathi, Red Dane, Red Sindhi, Sahiwal, Surti, Tharparkar, Toda, Umblachery, Vechur.

## ⚙️ Data Preprocessing

The images were preprocessed before training.

The preprocessing steps include:

1. Image resizing to 224 × 224 pixels.
2. Image format conversion.
3. Image renaming according to breed labels.
4. Removal of unsuitable images.
5. Dataset splitting into training, validation and testing sets.
6. Data augmentation to improve model generalization.

## 🧠 Deep Learning Models

Three pre-trained models were trained and compared:

- ResNet50
- EfficientNet-B0
- Vision Transformer (ViT)

Transfer learning was used by loading models with pre-trained ImageNet weights and replacing the final classification layer with a layer containing **41 output classes**.

## 📊 Model Comparison

| Model | Test Accuracy |
|---|---:|
| ResNet50 | 50.38% |
| EfficientNet-B0 | 51.13% |
| Vision Transformer (ViT) | 59.93% |

Among the tested models, **Vision Transformer achieved the highest test accuracy of 59.93%**.

## 🏆 Best Model

The Vision Transformer model was selected as the best-performing model among the three tested architectures.

The trained model checkpoint was saved as:

`vit_best.pth`

## 🖥️ Graphical User Interface

A Gradio-based GUI was developed for the application.

The user can:

1. Upload a cattle image.
2. Click the **Predict Breed** button.
3. View the predicted cattle breed.
4. View the prediction confidence.
5. View the Top-3 predicted breeds.
6. View breed-related information.

## 🔄 System Workflow

```text
Cattle Image Dataset
        ↓
Data Preprocessing
        ↓
Train/Test Split
        ↓
Data Augmentation
        ↓
Training & Validation
        ↓
Deep Learning Models
        ↓
Model Comparison
        ↓
Best Model Selection
        ↓
Upload Cattle Image
        ↓
Breed Prediction
        ↓
Breed Information
