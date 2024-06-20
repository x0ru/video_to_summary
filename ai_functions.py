from openai import OpenAI
import download_subtitles
import os

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    # api_key="My API Key",
)

def splitting_tasks(all_text):
    print(len(all_text))
    summary = ''
    summary2 = ''
    for split_text in all_text:
        summary += summary_paragraph(split_text)
        summary2 += summary_key_points(split_text)
    if len(all_text) == 1:
        return [summary, summary2.split('\n')]
    print(summary)
    os.remove('sub.srt.en.vtt')
    return [summary_paragraph(summary), summary_key_points(summary2).split('\n')]


def summary_paragraph(split_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in "
                           "language comprehension and summarization. "
                           "I would like you to read the following text which is based on video "
                           "and summarize it into a concise "
                           
                           "abstract paragraph. Don't mention it is based on text."
                           "Don't mention it is based on text. If you refer to it refer as in the video no in the text. "
                           "Aim to retain the most important points, providing a coherent and "
                           "readable summary that could help a person understand the main points of the discussion "
                           "without needing to read the entire text. Please avoid unnecessary details or tangential "
                           "points.Don't include anything about sponsor of video and advertisement "
                                      "included in text"
            },
            {
                "role": "user",
                "content": f'{split_text}'
            }
        ]
    )
    text = response.choices[0].message.content
    return text

def summary_key_points(split_text):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=[
        {"role": "system", "content": "You are a proficient AI with a specialty in distilling information into key "
                                      "points. " "Based on the following text which is based on video, "
                                      "identify and list the main points that"
                                      " were"
                                      " discussed or brought up. These should be the most important ideas, findings, "
                                      "or topics that are crucial to the essence of the discussion. Your goal is to"
                                      " provide a list that someone could read to quickly understand what was "
                                      "talked about. Don't include anything about sponsor of video and advertisement "
                                      "included in text. Don't mention it is based on text. "
                                      "If you refer to it refer as in the video no in the text. "},
        {"role": "user", "content": f'{split_text}'}
      ]
    )
    text = response.choices[0].message.content
    return text

