---
title: RAG architecture basics and workings
subheading: Using RAGS to retrieve information from documents and provide answers using foundational LLMs
date: 2024-11-21
---

# Going deeper into RAG: Vector Databases, Embeddings, and their workings

## More details on the learning resources publishing on notion link: [Notion](https://blushing-drink-f49.notion.site/RAG-Basics-106f681975c780aa81a2ddb8728ddf96?pvs=4)


RAG, which stands for Retrieval-Augmented Generation, is an advanced technique in natural language processing that combines information retrieval with text generation. This approach enhances the capabilities of large language models by allowing them to access and utilize external knowledge sources.

## Key Components of RAG:

1. **Vector Databases**: These are specialized databases designed to store and efficiently query high-dimensional vectors, which represent semantic information about text.

2. **Embeddings**: These are dense vector representations of text that capture semantic meaning, allowing for efficient similarity comparisons.

3. **Retrieval Mechanism**: This component searches the vector database to find relevant information based on the input query.

4. **Language Model**: A large language model that generates responses based on the retrieved information and the original query.

## How RAG Works:

1. The input query is converted into an embedding.
2. Similar embeddings are retrieved from the vector database.
3. The retrieved information is combined with the original query.
4. The language model generates a response based on this combined input.

This blog will explore each of these components in depth, discussing their implementations, challenges, and best practices.




### Stay tuned for the full article!