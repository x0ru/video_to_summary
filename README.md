
<div align="center"> <h1>YouTube video summarization webapp. </h1>
<h2>How does it work ?</h2></div>

![image](https://github.com/user-attachments/assets/3e70364b-f253-4637-b586-51bfb3947f5e)

<h2>Challenges</h2>
<ul>
  <li>Figuring out how to download subtitles as YouTube doesn't allow it through the API</li>
  <li>Dealing with videos without subtitles</li>
  <li>Long videos' subtitle files have too many characters for the OpenAI API to handle in one go. It is managed by splitting the text into a maximum of 50,000 character lengths and then sending multiple requests to the OpenAI API to merge these responses.</li>
  <li>Handling page refresh and storing results in the session so it won't send requests again or return an empty result</li>
</ul>

