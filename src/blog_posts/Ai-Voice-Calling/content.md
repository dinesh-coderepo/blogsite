---
title: AI Voice chatting to help with Customer support use-cases
subheading: Using current speech augmented LLMs (SpeechLLMs) with realtime voice modality to understand user issues and to provide support and solutions.
date: 2024-11-12
---

# Using Realtime speech LLMs to assist with service requests 
## Provide solutions and raise service tickets.

## Initial Architecture - Version V1

Link to the architecture diagram : [User draw.io to render](https://github.com/dinesh-coderepo/all-spec-draws/blob/main/AI-Voice-Support.drawio)

![alt text](AI-Voice-Support.drawio.png)


- Using webapp get the audio input from user with record button from UI
- Pass to a audio to text conversion tool (google or other services)
- Use LLM model - Open AI/Gemini to get the response back for the converted text
- Use text to speech to convert back the text generated from the Large language model
- Return the audio file to webapp

High level initial implementation for version 1 , later we will introduce chat like functionality, having context to the model on the topic, raising service tickets.(in future blogs)

### Building - Next steps coming soon




