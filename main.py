from subtitles.subtitles import get_subtitles,parse_srt_string, group_subtitle_texts
import re
teste = get_subtitles("https://www.youtube.com/watch?v=FAyKDaXEAgc", "a.en")
parsed_srt = parse_srt_string(teste)

all_subs = group_subtitle_texts(parsed_srt)

print(all_subs)