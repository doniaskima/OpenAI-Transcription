# OpenAI Whisper Transcription and Summary Tool

## Overview

This project is an AI-powered transcription and summarization tool built using **Streamlit** for the front end and **OpenAI Whisper** for audio transcription. The application allows users to upload or record audio files, which are then transcribed into text, summarized, and analyzed for sentiment. It also integrates various AI tools and APIs to provide fact-checking, math operations, and research capabilities from multiple sources such as Wikipedia, DuckDuckGo, YouTube, and PubMed.

## Features

1. **Audio Upload and Recording**:

   - Users can either upload audio files or directly record audio through the interface.
   - Supported audio formats: mp3, mp4, mpeg, mpga, m4a, wav, webm.

2. **OpenAI Whisper for Transcription**:

   - Audio is transcribed using OpenAI Whisper, with automatic corrections for grammar and spelling.

3. **AI-Powered Summary**:

   - Transcriptions are automatically summarized using the OpenAI GPT-4 model with a map-reduce summarization method.

4. **Sentiment Analysis**:

   - The transcription is analyzed to determine the sentiment, generating a report based on the content of the audio.

5. **Fact Checking**:

   - Integrated tools allow fact-checking of the transcription using various research databases such as Wikipedia, DuckDuckGo, and PubMed.

6. **Text Statistics**:

   - Displays word count, character count, and word frequency of the transcription.

7. **QA Search**:

   - Searches previous transcripts and summarizations stored in Pinecone vector database to find related content and insights.

8. **User Authentication**:

   - Built-in user authentication with the ability to create and manage accounts. User data is stored securely in a database.

9. **Conversation Buffer Memory**:
   - Chat interface allows users to interact with AI models in a conversational format, maintaining context through conversation buffer memory.

## Architecture

- **Frontend**: Built with **Streamlit** for an interactive and user-friendly interface.
- **Backend**: Uses OpenAI Whisper for transcription and OpenAI GPT-4 for summarization and sentiment analysis.
- **Database**: Transcriptions, summaries, and other metadata are stored in a database using custom functions for user management and transcript handling.
- **Vector Store**: **Pinecone** is used for storing and retrieving transcriptions and summaries based on their embeddings for efficient QA search.
- **APIs and Tools**:
  - OpenAI GPT-4 for text generation, correction, and summarization.
  - DuckDuckGo, Wikipedia, and PubMed for research and fact-checking.
  - Pydub for audio processing.
  - LangChain for orchestrating AI models and connecting tools.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/doniaskima/OpenAI-Transcription-Tool
   ```

2. Install dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Create a `.env` file with your OpenAI API key:
     ```
     OPENAI_API_KEY=your-openai-api-key
     ```

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Login or Create Account**: Authenticate through the user authentication tab.
2. **Upload or Record Audio**: Choose between uploading an audio file or recording one directly through the interface.
3. **Generate Transcription**: Click "Generate Transcript and Summary" to transcribe the audio and generate a summary, sentiment analysis, and other insights.
4. **Interact with the Transcript**: Review the transcription, summary, and fact-check results. Chat with AI based on the transcript data.
5. **View Previous Transcriptions**: Use the "Previous Transcriptions" tab to review and interact with earlier sessions.

## Technologies Used

- **Streamlit**: For creating the front-end interface.
- **OpenAI Whisper**: For audio transcription.
- **OpenAI GPT-4**: For text summarization, sentiment analysis, and fact-checking.
- **LangChain**: To orchestrate multiple AI models and tools.
- **Pinecone**: Vector database for storing and querying transcripts.
- **Pandas**: For data manipulation and word frequency analysis.
- **Pydub**: For handling and processing audio files.

## Future Improvements

- Integration of more AI tools for advanced fact-checking.
- Support for additional languages in transcription.
- Enhanced user interface and experience for better usability.
