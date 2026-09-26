import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()


from prompt import (
    TOP_10_TOPICS_PROMPT,
    TOPIC_SELECTION_PROMPT,
    SCRIPT_GENERATOR_PROMPT
)

client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_groq(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content


def main():
   # Main topic
    topic = "Java"

    # Step 1: Generate top 10 topics
    prompt1 = TOP_10_TOPICS_PROMPT.format(
        topic=topic
    )

    top_10_topics = ask_groq(prompt1)

    print("\n===== TOP 10 TOPICS =====")
    print(top_10_topics)


    # Step 2: Select one topic
    prompt2 = TOPIC_SELECTION_PROMPT.format(
        top_10_topics=top_10_topics
    )

    selected_topic = ask_groq(prompt2)

    print("\n===== SELECTED TOPIC =====")
    print(selected_topic)

    # Step 3: Generate YouTube script
    prompt3 = SCRIPT_GENERATOR_PROMPT.format(
        selected_topic=selected_topic
    )

    script = ask_groq(prompt3)

    print("\n===== YOUTUBE SCRIPT =====")
    print(script)



if __name__ == "__main__":
    main()