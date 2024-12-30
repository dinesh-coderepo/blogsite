---
title: Taking the 3 Azure Ignite Edition Challenges to Complete
subheading: Microsoft Learn Challenge conducting a challenge to get good in few of the challenges which are super useful to complete to gain knowledge on Microsoft Fabric , Data Security , Building AI apps with Microsoft Azure services
date: 2024-12-23
---

# Documenting 3 Microsoft Learning challenges

### [Ignite Edition Challenge: Prepare for the next generation of data analytics with Microsoft Fabric](https://learn.microsoft.com/en-us/collections/8wy3ioj77zzgyd?sharingId=6A9F03F25E12DA9E&ref=collection&listId=d1z7cn7do0xpxr&wt.mc_id=ignitechallenge25_landingpage_wwl)
### [Microsoft Learn Challenge | Ignite Edition: Secure your data in the age of AI](https://learn.microsoft.com/en-us/collections/8wy3ioj73j1wyr?sharingId=6A9F03F25E12DA9E&ref=collection&listId=d1z7cn7drdg02o&wt.mc_id=ignitechallenge25_landingpage_wwl)
### [Microsoft Learn Challenge | Ignite Edition: Build AI apps with Microsoft Azure services](https://learn.microsoft.com/en-us/collections/j25rcze78q2ry5?sharingId=6A9F03F25E12DA9E&ref=collection&listId=63kgh6d1mp124g&wt.mc_id=ignitechallenge25_landingpage_wwl)

## Microsoft Fabric - Unified data analytics platform

#### Introduction to end-to-end analytics using Microsoft Fabric : [Link](https://learn.microsoft.com/en-us/collections/8wy3ioj77zzgyd?sharingId=6A9F03F25E12DA9E&ref=collection&listId=d1z7cn7do0xpxr&wt.mc_id=ignitechallenge25_landingpage_wwl)

Note : while I follow this challenge I will also create the resources in Azure and attach screenshots for better documentation.

- Getting started with the intro module, fabric is a analytics platform with all the required services for data integrated to one service. It has services integrated to ingest, store, transform and analyze data all in one place. 
- Exciting for any member in data field having all in one place and managing it will be simpler than managing 4-5 different services in different places and permissions across services.
- Fabric has integrated data lake called onelake, OneCopy methodology seems to be key and looks like this paradigm will eliminate a separate copy(Costly Query Clusters) just for Product Managers to query data. [link](https://learn.microsoft.com/en-us/training/modules/introduction-end-analytics-use-microsoft-fabric/2-explore-analytics-fabric)
- One Lake is built on top of ADLS Azure. Data can be stored in all open formats like delta, parquet, csv, JSON. Meaning all services stores data in OneLake 
- In Onelake we can create shortcuts and point the data assets to other services , source data will always be in sync with other links.
- Workspaces - we can control resources and access controls on the workspaces and differentiate DEV UAT PROD env. 
- Workspace resources can be integrated to GIT and deploy, we can configure compute resources and other config details directly from ADO.
- Fabric brings together data ingestion and storage with OneLake, and for transformation we can use ADF and connect data ingested using DirectLake, easy integration to Power BI and much more.
-  we need an organizational email to create a trail account , process : [link](https://go.microsoft.com/fwlink/?linkid=2227864) , free trial restrictions and capabilities : [link](https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial)

![signed_up_fabric](signed_up_fabric.png)
![activate_freetrial](activate_freetrial.png)
![new_workspace](new_workspace.png)

- Login to Azure fabric : [https://app.fabric.microsoft.com/home](https://app.fabric.microsoft.com/home) , you can provide access to other users even in trail account.
- By default onelake creates files in delta file format. Intro to fabric is module is now complete, on to the next module in this challenge. 

![intro_to_fabric](intro_to_fabric.png)


### Get started with lakehouses in Microsoft Fabric Module : [link](https://learn.microsoft.com/en-us/training/modules/get-started-lakehouses/)

- Foundation of Fabric is lakehouse built on top of onelake storage layer, good integration to compute engines for processing.
- lakehouse data is organized as schema on read, stores data by default as delta table format but supports all file formats. 
- Ingest data to lakehouse from many different sources and also there is a concept of shortcuts where we can link data from ADLS gen2 or some external sources directly.
- Access to lakehouse can be managed at workspace level or item-level sharing, item-level access is useful for granting read-only access for reporting or analytical needs.
- Lakehouse supports data governance features , sensitivity labels (microsoft purview). Transformation on ingested data can be done using spark or dataflows gen 2.
- For a new data lake house we create it creates three data items : lakehouse(which contains shortcuts,folders,files,tables) , Semantic model , SQL analytics endpoint (to allow read-only access to query data)
- To ingest data to lakehouse we have three options, upload data(local data) , Dataflow Gen2 (import and transform using power query) , Notebooks (will have access to pools) ,  Data Factory copy activity. We will have two options load to place files directly or load to tables.
- we can use custom JARS to create frameworks in spark and provide for custom implementations. - more info in the link : [spark-config](https://learn.microsoft.com/en-us/fabric/data-engineering/create-spark-job-definition)
- Fabric can access to shortcuts (data) directly from source systems( integrate data into your lakehouse while keeping it stored in external storage ) . While accessing the source data from fabric it uses the user credential to source systems for example we are accessing a storage to query(sql query end point), the user need to have read permissions in source system inorder to be able to read the data using the tool.  - more info on creating short cuts in lakehouse : [shortcuts](https://learn.microsoft.com/en-us/fabric/onelake/onelake-shortcuts)
- There are three mechanisms to ingest or transform data - notebooks (pyspark,scala, SQl), dataflow gen2( power query interface) , Pipelines to do Ingesting, transforming and loading. 
- The final enriched data can be accessed from notebooks (for ML development or analytical), using semantic model users can build power BI reports, also analysts can use SQL endpoint to query data.
- Doing the exercise on creating lakehouse in my trail account - [link](https://learn.microsoft.com/en-us/training/modules/get-started-lakehouses/5-exercise-lakehouse)
- Using visual tools for transformation and querying using sql pool, below attached few dashboard pics created on ingested sales data.

![lake_house](lake_house.png)

![exercise](exercise_1_1.png)

![exercise_2](exercise_1_2.png)

![alt text](exercise_1_3.png)

- Final view of lakehouse in the workspace for the exercise.

![exercise_1_4](exercise_1_4.png)

- Completed this module , on to the next module ... 

![completed_2](completed_module_2.png)

### Use Apache Spark in Microsoft Fabric : [Link](https://learn.microsoft.com/en-us/training/modules/use-apache-spark-work-files-lakehouse/)

- 

### continue...