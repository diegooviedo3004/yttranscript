from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

app = FastAPI()

@app.get("/transcript/{video_id}")
def read_transcript(video_id: str):
    """
    Retrieve the transcript for a given YouTube video ID.

    Args:
        video_id (str): The YouTube video ID (e.g., "dQw4w9WgXcQ").

    Returns:
        list: The transcript as a list of dictionaries with text and timestamps.

    Raises:
        HTTPException: If transcripts are disabled, not found, or an error occurs.
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except TranscriptsDisabled:
        raise HTTPException(status_code=403, detail="Transcripts are disabled for this video")
    except NoTranscriptFound:
        raise HTTPException(status_code=404, detail="No transcript found for this video")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.get("/health")
def health_check():
    """
    Check the health status of the service.

    Returns:
        dict: A status message indicating the service is operational.
    """
    return {"status": "ok"}
