# music_lyric_generatoy

Audio to Lyrics Generator (AI-Powered)

This Python project converts audio files (MP3, WAV, M4A, etc.) into well-formatted song lyrics using OpenAI Whisper for transcription and Google Gemini AI for intelligent lyric structuring.

Features

Speech-to-Text using Whisper (automatic language detection)

AI Formatting — Converts raw transcription into rhythmically structured song lyrics

Multi-Language Support — Keeps lyrics in the original language

User-Friendly GUI — Select files easily using a file dialog

Auto Save — Lyrics are saved as a .txt file beside your audio

Requirements

Python 3.9 or above

Required libraries:

pip install google-generativeai openai-whisper tkinter


Note: tkinter usually comes pre-installed with Python on Windows.

Setup Instructions

Clone this repository

git clone https://github.com/your-username/audio-to-lyrics-generator.git
cd audio-to-lyrics-generator


Install dependencies

pip install -r requirements.txt


Add your Gemini API Key
Open lyrics2.py and replace:

GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY"


with your actual key.

Run the script

python lyrics2.py

How It Works

You select an audio file.

The Whisper model transcribes it into text.

The Gemini AI model reformats it into natural, structured lyrics.

The final lyrics are displayed and saved as a .txt file.

Output Example
Original Language: English

[Verse 1]
The sun goes down, the lights begin to fade,
Echoes of dreams we made...

[Chorus]
We’ll sing forever, hearts open wide,
Dancing through time, side by side.

Technologies Used

OpenAI Whisper

Google Gemini AI

Python (Tkinter GUI, OS, File handling)

Important Notes

Ensure you have a valid Gemini API key.

Whisper’s transcription accuracy improves with clearer audio.

The app works offline for Whisper and online for Gemini.

Contributing

Pull requests and suggestions are welcome.
If you find a bug or have an improvement idea, feel free to open an issue.

License

This project is open-source under the MIT License.

Would you like me to include a short project description line (for the top of your GitHub page under the title)?
For example:

“A desktop tool that turns audio songs into structured lyrics using Whisper and Gemini AI.”
