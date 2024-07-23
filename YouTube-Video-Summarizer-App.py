from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Function to generate a PDF from text
def generate_pdf_from_text(text, pdf_filename, left_margin=20, top_margin=20):
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    width, height = A4
    text_object = c.beginText(left_margin, height - top_margin)
    text_object.setFont("Helvetica", 12)

    for line in text.split('\n'):
        # Adjust the font size or add other formatting options as needed
        text_object.setFont("Helvetica", 12)
        text_object.textLine(line)

    c.drawText(text_object)
    c.showPage()
    c.save()

# Your YouTube video URL
youtube_video = "https://www.youtube.com/watch?v=KnFj9qW6QkM"
video_id = youtube_video.split("=")[1]
YouTubeVideo(video_id)

# Get the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

# Process the transcript in chunks of 1000 characters and summarize each chunk
chunk_size = 1000
summarized_text = []

result = ""
for i in transcript:
    result += ' ' + i['text']

# Summarizing the text
num_iters = int(len(result) / chunk_size)
summarized_text = []
for i in range(0, num_iters + 1):
    start = i * chunk_size
    end = (i + 1) * chunk_size
    print("Input text\n" + result[start:end])
    out = summarizer(result[start:end])
    out = out[0]
    out = out['summary_text']
    print("Summarized text\n" + out)
    summarized_text.append(out)

# Generate a PDF file from the summarized text
pdf_filename = "summarized_text.pdf"
generate_pdf_from_text('\n'.join(summarized_text), pdf_filename)
