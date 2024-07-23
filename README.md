# YouTube Video Summarizer App

Welcome to the YouTube Video Summarizer App! This application, developed using Python and various APIs, allows users to generate concise text summaries of YouTube videos. It's an efficient tool for quickly understanding the key points of lengthy videos without watching them in their entirety. Additionally, the app can generate a PDF file containing the summarized text.

## Features

- **Video URL Input**: Enter a YouTube video URL to generate a summary.
- **Text Summarization**: Uses natural language processing to create concise summaries.
- **PDF Generation**: Converts the summarized text into a PDF document.
- **User-Friendly Interface**: Simple and intuitive interface for easy use.

## Requirements

To run this project, you'll need to have Python installed on your machine. Additionally, you will need to install the following Python libraries:

- `requests`
- `pytube`
- `transformers`
- `youtube_transcript_api`
- `reportlab`

You can install these libraries using pip:

```bash
pip install requests pytube transformers youtube_transcript_api reportlab
```

## Getting Started

1. **Clone the repository**:

```bash
git clone https://github.com/GoKu21g/youtube-video-summarizer-app.git
cd youtube-video-summarizer-app
```

2. **Obtain API Key**: Sign up at a language processing provider (e.g., Hugging Face) to get an API key if needed.

3. **Configuration**: Create a configuration file or set up environment variables to store your API key.

4. **Run the Application**:

```bash
python summarizer_app.py
```

## Usage

Once the application is running, you can use it to summarize YouTube videos by entering the video URL. The application will fetch the video, extract the transcript, and generate a summary based on the transcript. Additionally, it will generate a PDF file of the summarized text.

## Code Overview

### `summarizer_app.py`

This is the main script of the application. It handles:

- Fetching video data from YouTube
- Extracting the transcript using `youtube_transcript_api`
- Summarizing the transcript using a language model from the `transformers` library
- Generating a PDF file from the summarized text

Here is an example code snippet:

```python
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Function to generate a PDF from text
def generate_pdf_from_text(text, pdf_filename, left_margin=20, top_margin=20):
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4
    text_object = c.beginText(left_margin, height - top_margin)
    text_object.setFont("Helvetica", 12)

    for line in text.split('\n'):
        text_object.setFont("Helvetica", 12)
        text_object.textLine(line)

    c.drawText(text_object)
    c.showPage()
    c.save()

# Your YouTube video URL
youtube_video = "https://www.youtube.com/watch?v=KnFj9qW6QkM"
video_id = youtube_video.split("=")[1]

# Get the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

# Process the transcript in chunks of 1000 characters and summarize each chunk
chunk_size = 1000
result = ""
for i in transcript:
    result += ' ' + i['text']

# Summarizing the text
num_iters = int(len(result) / chunk_size)
summarized_text = []
for i in range(0, num_iters + 1):
    start = i * chunk_size
    end = (i + 1) * chunk_size
    out = summarizer(result[start:end])
    summarized_text.append(out[0]['summary_text'])

# Generate a PDF file from the summarized text
pdf_filename = "summarized_text.pdf"
generate_pdf_from_text('\n'.join(summarized_text), pdf_filename)
```

## GUI Overview

The app can also be extended to include a graphical user interface using `tkinter` for a more user-friendly experience.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Contact

For any questions or suggestions, please open an issue on GitHub or contact me at [GoKu21g](https://github.com/GoKu21g).

---

Thank you for using the YouTube Video Summarizer App! We hope it helps you save time and quickly grasp the essential points of YouTube videos.
