---
title: Orchestrating ML Pipelines with Azure Data Factory
subheading: Leveraging Azure Data Factory for Scalable and Efficient Machine Learning Workflows
date: 2024-08-22
---

# Using ADF pipelines for orchestrating ML training & inference

## Introduction

In this blog post, we'll explore how to use Azure Data Factory (ADF) for orchestrating machine learning pipelines. We'll walk through the process of setting up a project and connecting it to Azure Data Factory.

## Project Setup

### Creating a GitHub Repository

To begin, we'll create a new repository on GitHub to store our project files.

![GitHub Repository Creation](git-repo.png)

### Setting Up Azure Resources

Next, we'll create a new resource group in Azure specifically for this project.

**Resource Group Name:** adf-ml-project

![Azure Resource Group](resource-group.png)

## Integrating with Azure Data Factory

### Connecting GitHub to ADF

To leverage version control and collaborative features, we'll connect our GitHub repository to Azure Data Factory.

1. In the Azure Data Factory interface, navigate to the "Author & Monitor" section.
2. Click on "Set up code repository" to begin the integration process.

![GitHub Integration in ADF](github-integration.png)

### Authorizing ADF Access

During the setup, you'll be prompted to authorize Azure Data Factory to access your GitHub account. This step is crucial for enabling seamless integration between ADF and your code repository.

![Authorization Request](authorization.png)

### Configuring Repository Settings

After authorization, configure the repository settings as follows:

![GitHub Configuration](git-hub-config.png)

### Key points to note:
    - Select your repository from the dropdown.
    - Choose the branch you want to use for development.
    - ADF will automatically create a "publish" branch for ARM templates.
    - Set the root folder to "src" to ensure all code resources are properly converted to JSON and stored in the correct location.


I will be using the MNIST dataset for this ML model : https://www.kaggle.com/code/prashant111/mnist-deep-neural-network-with-keras
In this version we will build everything from UI of ADF itself , but we will document all steps one by one.


### Creating a blob storage in the resource group which we will use for storing data and storing trained model

![Storage account creation](storage-create.png)

Using LRS type redundancy as Locally Redundant Storage is good for our usecase but for production systems it is better to have RA-GRS type redundancy as this is a GEO-redundant storage and copies 3 times locally and 3 times in the other region.


![Containers and Folders](containers-folders.png)

Created a container **adftrain** and folders for storing training data, inference data and trained model.


### Adding access to the storage account via linked service

Add the Managed Identity of the ADF workspace and provide **Contributor access** to the storage account as below.

![access-storage](access-storage.png)

Once added then add this account to the linked service in the ADF workspace. Validate with the Test Connection at the bottom to check if the connection is successful.

![adf_linked_service](adf_linked_service.png)


### Key points to note:
    - With the above steps we created a ADF workspace, Storage account and Linked Service to access storage account from ADF service.
    - Going forward we can keep publishing ARM template for any changes so that the repo : [https://github.com/dinesh-coderepo/adf-ml-project](https://github.com/dinesh-coderepo/adf-ml-project) , `branch : adf_publish` is updated with the latest changes.
    - Publishing to adf_publish involves some checks from ADF and then the ARM template is published.
    - Incase of any issues we can revert to the previous commit in the repo.
    - Ideally in production we should not publish the code changes directly to the repo without testing in the dev environment.
    - We can have a CI/CD pipeline to monitor any changes to adf_publish branch and it detects any changes it will deploy these to target environment such as staging and production
    - The deployment uses the ARM template to create update or delete resources in target ADF environment.
    - We will cover this entire setup in an another blog post.




### Uploading data to blob storage

As part of next steps first we will get the mnist data from keras datasets and then upload it to blob storage. We are trying to mimic a real time scenario where we first get the data from some external source and then upload it to blob storage, in this case we are are getting the data from keras.datasets module then uploading it to blob storage.

```python
# I am first dumping these images into blob storage
from keras.datasets import mnist



# Remaining steps are coming soon...
```
### Remaining steps are coming soon...