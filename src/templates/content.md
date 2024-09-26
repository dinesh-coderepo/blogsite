---
title: Title of the blog which shown in the home screen
subheading: Subheading of the blog which shown in the home screen
date: 2024-08-07
---

# App name which will be shown in the actial blog


### Data Flow Graph

To better visualize the flow of a graph, example template:

```mermaid
graph LR
    A[External Source] -->|Fetch Data| B[Local Processing]
    B -->|Upload| C[Blob Storage]
    C -->|Train| D[ML Model]
    D -->|Save| E[Trained Model Storage]
    C -->|Inference| F[Prediction Service]
    E -->|Load| F
```