---
title: Automating audio generation
subheading: From text , generate audio files and publishing them to webapp
date: 2026-02-22
---

# Using Text-to-Audio Conversion Service to Publish Audio Content to a Web App

In this post, we'll walk through an approach to convert text into audio using **Azure AI Speech Service** and serve the generated audio files from a web application.

---

## Method Provided by LLM

> The following approach was generated with the assistance of an LLM (GitHub Copilot). The code implementation is left to the reader.

### Architecture

```
Text Input → Azure AI Speech Service → .wav/.mp3 file → Azure Blob Storage → Web App
```

### Approach — Step by Step

#### 1. Provision an Azure AI Speech Resource

- Go to the **Azure Portal** → **Create a resource** → search **Speech** → select **Speech** by Microsoft
- Choose a **Resource group** (or create one, e.g. `rg-audio-gen`)
- Pick a **Region** close to you (e.g. `East US`)
- Select **Pricing tier**: Free F0 for testing, or Standard S0 for production
- After deployment, navigate to the resource and note down the **Key** and **Region** from the **Keys and Endpoint** blade
- Alternatively, use the Azure CLI: `az cognitiveservices account create` with `--kind SpeechServices`

#### 2. Set Up Your Python Environment

- Install the **Azure Speech SDK** package: `azure-cognitiveservices-speech`
- Store your Speech key and region as environment variables (`AZURE_SPEECH_KEY`, `AZURE_SPEECH_REGION`) — never hard-code secrets

#### 3. Write the Text-to-Audio Conversion Logic

- Create a `SpeechConfig` object using your key and region
- Set the voice using `speech_synthesis_voice_name` — Azure supports **400+ neural voices** across **140+ languages** (see [voice gallery](https://speech.microsoft.com/portal/voicegallery))
- Create an `AudioOutputConfig` pointing to a local `.wav` file
- Instantiate a `SpeechSynthesizer` and call `speak_text_async()` with your input text
- Handle both the **success** case (`SynthesizingAudioCompleted`) and the **cancellation/error** case
- The SDK writes the audio directly to the specified output file

#### 4. Provision Azure Blob Storage

- Create a **Storage Account** in the same resource group (e.g. via `az storage account create`)
- Create a **Blob Container** (e.g. `audio-files`) with public blob-level read access so audio URLs are directly accessible
- Install the `azure-storage-blob` Python package
- Store the storage connection string as an environment variable (`AZURE_STORAGE_CONNECTION_STRING`)

#### 5. Upload the Generated Audio File

- Use `BlobServiceClient.from_connection_string()` to connect
- Get a `BlobClient` for your container and target blob name
- Open the local `.wav` file in binary mode and call `upload_blob()` with `overwrite=True`
- The blob client exposes a `.url` property — this is the public URL of your audio file
- Optionally delete the local file after upload to save disk space

#### 6. Serve the Audio in Your Web App

- The uploaded blob will have a public URL like: `https://<account>.blob.core.windows.net/audio-files/output.wav`
- Embed it in HTML using the `<audio controls>` element with a `<source>` tag
- In Flask (this blog's stack), you can create a route that renders the audio player with the blob URL passed as a template variable

#### 7. End-to-End Flow

Combine everything into a single function that:
1. Takes text input as a parameter
2. Synthesizes it to a local `.wav` file via Azure Speech
3. Uploads the file to Blob Storage
4. Cleans up the local file
5. Returns the public URL

### Key Azure Services Used

| Service | Purpose |
|---|---|
| **Azure AI Speech** | Converts text to natural-sounding audio using neural voices |
| **Azure Blob Storage** | Hosts the generated audio files with public URL access |

### Cost Estimate

| Service | Free Tier | Pay-as-you-go |
|---|---|---|
| Azure AI Speech | 500K chars/month (F0) | ~$1 per 1M chars (S0) |
| Azure Blob Storage | 5 GB free for 12 months | ~$0.02/GB/month |

### Important Notes

- **Security**: Use environment variables for all keys and connection strings. Consider Azure Key Vault for production.
- **Voice selection**: Experiment with different `speech_synthesis_voice_name` values. Multi-lingual voices (e.g. `en-US-JennyMultilingualNeural`) can handle mixed-language text.
- **Output format**: The SDK defaults to WAV. For smaller files, configure MP3 output via `speech_config.set_speech_synthesis_output_format()`.
- **SSML**: For finer control over pronunciation, pauses, pitch, and speed, use SSML markup instead of plain text with `speak_ssml_async()`.
- **Batch processing**: For large volumes of text, consider splitting into chunks and processing in parallel.

### Cleanup

Delete the resource group when done to avoid charges:

```bash
az group delete --name rg-audio-gen --yes --no-wait
```

### References

- [Azure AI Speech documentation](https://learn.microsoft.com/azure/ai-services/speech-service/)
- [Speech SDK for Python](https://learn.microsoft.com/azure/ai-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python)
- [Voice gallery](https://speech.microsoft.com/portal/voicegallery)
- [Azure Blob Storage quickstart](https://learn.microsoft.com/azure/storage/blobs/storage-quickstart-blobs-python)

--

## Implementation

