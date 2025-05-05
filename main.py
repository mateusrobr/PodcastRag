from subtitles.subtitles import get_subtitles,parse_srt_string, group_subtitle_texts
from database.database import initialize_database

from qdrant_client import QdrantClient

from chatbot.chatbot import main_flow



main_flow()
#client = initialize_database()
