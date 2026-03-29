import anthropic
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

while True:
    file_path = input("Enter file path (or 'quit' to exit): ")
    if file_path == "quit":
        break
    with open(file_path) as f:
        content = f.read()
    print("Document loaded! Ask me anything about it. Type 'done' for next document.\n")
    conversation = []

    while True:
        question = input("You: ")
        if question == "done":
            break
        if question == "":
            continue
        conversation.append({"role": "user", "content": question})
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            system=f"You are a document analyzer. Here is the document:\n\n{content}\n\nAnswer questions about this document.",
            messages=conversation
        )
        conversation.append({"role": "assistant", "content": message.content[0].text})
        print(f"\nAnalyzer: {message.content[0].text}\n")

    print("Document closed.\n")
    with open("analysis_log.txt", "w") as file:
        file.write(f"Analysis date: {datetime.now()}\n\n")
        for msg in conversation:
            file.write(f"{msg['role']}: {msg['content']}\n\n")
    print("Analysis saved!")