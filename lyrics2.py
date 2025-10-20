import tkinter as tk
from tkinter import filedialog, messagebox
import google.generativeai as genai
import whisper
import os

# 🔑 REPLACE WITH YOUR GEMINI API KEY
GOOGLE_API_KEY = "AIzaSyCy83qh6FP8L3jnt-VvW8a3BW2MVtzTIBY"  # ← PASTE YOUR KEY HERE!

def select_audio_file():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    file_path = filedialog.askopenfilename(
        title="Select Audio File (MP3, WAV, M4A, etc.)",
        filetypes=[
            ("Audio files", "*.mp3 *.wav *.m4a *.flac *.ogg"),
            ("All files", "*.*")
        ]
    )
    return file_path

def main():
    print("🎵 Audio to Lyrics Generator (Local Windows Version)")
    print("💡 Make sure you replaced 'YOUR_GEMINI_API_KEY_HERE' with your real key!\n")

    if not GOOGLE_API_KEY.strip():
        error = "❌ Google API key is missing! Please add it in the script."
        print(error)
        messagebox.showerror("Configuration Error", error)
        return

    # Select audio file
    audio_path = select_audio_file()
    if not audio_path:
        print("❌ No file selected. Exiting.")
        messagebox.showerror("Error", "No file selected. Exiting.")
        return

    try:
        # Configure Gemini
        genai.configure(api_key=GOOGLE_API_KEY)

        # Load Whisper model
        print("🧠 Loading Whisper model (may take a minute on first run)...")
        model = whisper.load_model("base")  # Use 'small' for better accuracy if speed allows

        # Transcribe audio
        print(f"🎙️ Transcribing: {os.path.basename(audio_path)}")
        result = model.transcribe(audio_path, fp16=False)
        raw_text = result["text"].strip()
        lang = result.get("language", "unknown")

        print(f"🌍 Detected language: {lang}")
        print(f"📝 Raw transcription:\n{raw_text}\n")

        # ✨ Prompt: Format as song lyrics IN THE ORIGINAL LANGUAGE
        prompt = f"""
You are a professional lyricist. The following text is a raw transcription of a song in **{lang}**.

Your task:
- Clean up the text (remove filler words like 'um', 'uh', repeated words, false starts)
- Format it as natural, rhythmic song lyrics with appropriate line breaks, verses, and structure
- Preserve the **original language ({lang})** — do NOT translate it
- Keep the emotional tone, rhythm, and meaning intact
- Do NOT add explanations, quotes, headers, or markdown

Raw text:
"{raw_text}"

Output only the cleaned lyrics — nothing else.
"""

        print(f"✨ Formatting lyrics in {lang} with Gemini AI...")

        # Use a stable, widely available model
        gemini_model = genai.GenerativeModel('gemini-2.0-flash-lite-001')

        response = gemini_model.generate_content(
            prompt,
            generation_config={"max_output_tokens": 1500, "temperature": 0.6},
            safety_settings={
                "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
                "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
                "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
            }
        )
        lyrics = response.text.strip()

        # Save to file
        output_path = os.path.splitext(audio_path)[0] + "_lyrics.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"Original Language: {lang}\n\n")
            f.write(lyrics)

        print(f"\n🎤 Final Lyrics (in {lang}):\n")
        print("="*50)
        print(lyrics)
        print("="*50)
        print(f"\n💾 Saved to:\n{output_path}")

        messagebox.showinfo("Success", f"Lyrics saved to:\n{output_path}")

    except Exception as e:
        error_msg = f"💥 Error: {e}"
        print(error_msg)
        messagebox.showerror("Error", str(e))
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()