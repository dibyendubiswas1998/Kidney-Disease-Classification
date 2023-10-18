# Kidney Disease Classification:


## Problem Statement:
Develop an intelligent Kidney Disease Classification system using deep learning techniques to accurately diagnose kidney images as either normal or showing signs of a tumor. The system should analyze medical images of kidneys and provide a reliable classification to assist healthcare professionals in making informed decisions about patient diagnosis and treatment.


## Solution:
The seamless integration of the Kidney Disease Classification system through a robust CI/CD pipeline using GitHub Actions marks a significant milestone in healthcare technology. This automated deployment ensures that the latest advancements in kidney abnormality identification are promptly and efficiently delivered to healthcare professionals. By enabling swift iterations, seamless deployment, and continuous improvements, this automated workflow elevates the precision of kidney disease diagnosis.
<br><br>
With this CI/CD pipeline, healthcare professionals are empowered with a reliable and continually updated tool, enhancing their ability to identify kidney abnormalities with speed and accuracy. Through early diagnosis and timely intervention facilitated by this application, patient outcomes are substantially improved. This not only positively impacts individual lives but also contributes to the overall efficiency of kidney disease diagnosis and treatment, shaping a future where healthcare technology plays a pivotal role in enhancing patient care. [User APP](34.204.101.91:8080)


## Project Workflow:
**1. Data Ingestion:**
* **Description:** Load the dataset from the AWS S3 bucket.

* **Task:**
    * Connect to the AWS S3 bucket.
    * Retrieve the dataset files.
    * Ingest the data into the project environment.
<br><br>

**2. Prepare Base Model:**
* **Description:** Create the base model using VGG16 architecture with the Keras library.

* **Task:**
    * Import the VGG16 architecture from Keras.
    * Customize the model for the specific classification task.
    * Set up the base model's layers and configurations.
<br><br>

**3. Model Training:**
* **Description:** Train the model using the prepared base model and save the updated model.

* **Task:**
    * Prepare the dataset for training.
    * Train the model using the base model as a feature extractor.
    * Save the trained model for future use.
<br><br>

**4. Model Evaluation:**
* **Description:** Evaluate the trained model's performance using test data.

* **Task:**
    * Prepare the test dataset.
    * Evaluate the model's accuracy, precision, recall, F1-score metrics.
    * Generate evaluation reports and visualizations.
    * Store the results.
    * Intregates the **mlflow** for visualize the metrics for comparison.
<br><br>

**5. Create User App:**
* **Description:** Develop a user-friendly application for predicting new image data.

* **Task:**
    * Design an intuitive user interface for uploading images.
    * ntegrate the trained model into the application.
    * Implement the prediction mechanism.
    * Display the prediction results along with confidence scores.
    * [User APP](34.204.101.91:8080)



## Tech Stack:
* **Front-End:**
    * Html5
    * CSS3
    * JavaScript

* **Back-End:**
    * Python (tensorflow, keras, boto3, numpy, pandas, flask,etc.)

* **Deployment:**
    * AWS

* **Containerization:**
    * Docker

* **CI-CD Tool:**
    * GitHub Actions



<br><br><br>

-------------------------------- Thank You