# ai-meeting-assistant
Automated meeting summarizer with AI transcription 

A fully automated system that:
Records your online meetings
Transcribes the audio using Whisper
Generates summaries and action items using Gemini AI
Perfect for remote teams, class recordings, or anyone who hates taking notes manually.

Features
Auto-record meetings using OBS
Transcribe voice to text using OpenAI Whisper
Summarize key points and decisions using Gemini 1.5 Flash
Fully containerized with Docker

Technologies Used
AI Summary: Google Gemini 1.5 Flash
Transcription: OpenAI Whisper (base)
Recording: OBS + obs-websocket
Container: Docker & Docker Compose
Watcher: Python Watchdog

Installation
Install OBS,[Download from: https://obsproject.com](https://github.com/obsproject/obs-studio/releases/tag/27.2.4)
install obs-websocket v4.9.1  https://github.com/obsproject/obs-websocket/releases/tag/4.9.1
OBS-Studio-27.2.4

Go to Tools → WebSocket Server Settings and enable WebSocket
Default Port: 4444 

Install Docker
Install Docker Desktop from https://www.docker.com/products/docker-desktop

Setup

Clone this repo:
git clone https://[github.com/your-username/meeting-assistant.git](https://github.com/adkshsa/ai-meeting-assistant.git)
cd meeting-assistant
