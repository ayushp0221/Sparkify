# Sparkify Data Pipeline and Analysis

## Project Overview
Sparkify, a music streaming startup, collects user activity and song metadata in JSON format. This project builds a data pipeline to store, process, and analyze this data using MongoDB, AWS (S3, EC2, EMR), Hadoop, and Apache Spark.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Project Tasks](#project-tasks)
- [Results](#results)
- [Contributors](#contributors)

## Technologies Used
- **Python** (Flask, PyMongo, Boto3, PySpark)
- **AWS** (S3, EC2, EMR, Hadoop, Zeppelin)
- **MongoDB** (for NoSQL data storage)
- **Hadoop & Spark** (for big data processing)
- **Jupyter & Zeppelin Notebooks** (for interactive analytics)

## Project Structure
```
├── dataset/                   # Sample JSON log files
├── scripts/                   # Python scripts for data processing
│   ├── ingest_mongodb.py      # Loads data into MongoDB
│   ├── s3_upload.py           # Uploads data to S3
│   ├── hadoop_mapper.py       # Mapper script for Hadoop
│   ├── hadoop_reducer.py      # Reducer script for Hadoop
│   ├── spark_analysis.py      # PySpark job for analysis
│   ├── flask_app.py           # Flask app for web visualization        
├── notebooks/                 # Jupyter and Zeppelin notebooks
├── README.md                  # Project documentation
```

## Setup Instructions
### 1. Install MongoDB (on AWS EC2)
```sh
sudo yum install -y mongodb
sudo systemctl start mongod
```
### 2. Upload Log Data to S3
```sh
python scripts/s3_upload.py
```
### 3. Process Data with Hadoop
```sh
cat data/sample_log.json | python scripts/hadoop_mapper.py | sort | python scripts/hadoop_reducer.py
```
### 4. Run Flask Web App
```sh
python scripts/flask_app.py
```

## Project Tasks
### 1. MongoDB Integration
- Store JSON log data in MongoDB.
- Develop a Flask web app to display top songs and artists.

### 2. AWS S3 Storage
- Upload Sparkify logs to S3 using Boto3.

### 3. Parallel Processing with Python
- Use `ipyparallel` for distributed processing.

### 4. Hadoop Batch Processing
- Implement Mapper and Reducer scripts for Hadoop.
- Run MapReduce jobs on AWS EMR.

### 5. Spark Processing
- Analyze data using PySpark in Zeppelin notebooks.

### 6. Spark Batch Processing
- Submit Spark jobs using `spark-submit`.
- Save results in S3.

## Results
- A fully functional data pipeline from ingestion to analysis.
- Processed user activity logs for top song and artist insights.
- Scaled analysis using Hadoop and Spark on AWS.

## Contributors
- **Ayush Prajapati** - Data Engineer & Developer
