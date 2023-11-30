import streamlit as st
import google.generativeai as genai

st.write("Basics")


"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""



genai.configure(api_key="AIzaSyDB7ec067O7UBLkP9OkMJRUZj6MibdIwAU")

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.6,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2},{"category":"HARM_CATEGORY_HARASSMENT","threshold":2},{"category":"HARM_CATEGORY_HATE_SPEECH","threshold":2},{"category":"HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS_CONTENT","threshold":2}],
}


# prompt = f"""Summarize this paragraph and detail some relevant context.
#
# Text: "I am by birth a Genevese, and my family is one of the most distinguished of that republic. My ancestors had been for many years counsellors and syndics, and my father had filled several public situations with honour and reputation. He was respected by all who knew him for his integrity and indefatigable attention to public business. He passed his younger days perpetually occupied by the affairs of his country; a variety of circumstances had prevented his marrying early, nor was it until the decline of life that he became a husband and the father of a family."
#
# Summary: In this text, the narrator is describing his background and upbringing. He tells us that he is a native of Geneva, Switzerland, and that his family is one of the most distinguished in the republic. He then goes on to describe his father, who was a respected public servant.
#
# Text: "The thing the Time Traveller held in his hand was a glittering metallic framework, scarcely larger than a small clock, and very delicately made. There was ivory in it, and some transparent crystalline substance. And now I must be explicit, for this that follows—unless his explanation is to be accepted—is an absolutely unaccountable thing. He took one of the small octagonal tables that were scattered about the room, and set it in front of the fire, with two legs on the hearthrug."
#
# Summary:"""


prompt = st.text_area("Enter the prompt")
if st.button("Generate"):
  response = genai.generate_text(
    **defaults,
    prompt=prompt
  )

  st.write(response.result)