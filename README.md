# Chatterbot-terminal-client
In this assignment, I demonstrate what I know about ChatterBot—a machine-learning-based conversational dialog engine built in Python—by creating a pure-Python terminal client. This client trains on a corpus of **known** conversations and then launches a REPL so you can chat with the bot right in your terminal.

---

## What I Know About ChatterBot

- **Data-driven responses**: ChatterBot learns reply patterns by training on existing “known” conversation corpora (e.g., greetings, small talk, FAQs).  
- **Logic adapters**: It uses adapters like `BestMatch` to select the closest known response to your input.  
- **Storage**: By default it persists its knowledge in a local SQLite database (`chatterbot.sqlite3`), so subsequent runs “remember” previous training.  
- **Extensibility**: I can plug in additional corpora or custom conversation data to improve domain-specific responses.



