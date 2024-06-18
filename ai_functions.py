from openai import OpenAI
import download_subtitles
import os

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    # api_key="My API Key",
)


def summary():
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=[
        {"role": "system", "content": "You are a proficient AI with a specialty in distilling information into key points. Based on the following text, identify and list the main points that were discussed or brought up. These should be the most important ideas, findings, or topics that are crucial to the essence of the discussion. Your goal is to provide a list that someone could read to quickly understand what was talked about."},
        {"role": "user", "content": f'{download_subtitles.give_me_subs()}'}
      ]
    )
    print(response.choices[0].message.content)
    os.remove('sub.srt.en.vtt')
    text = "" + response.choices[0].message.content
    return text
