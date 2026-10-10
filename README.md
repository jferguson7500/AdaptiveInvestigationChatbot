# Adaptive Investigation Services Chatbot

## Project Overview

This project was developed for MSAI 631: Artificial Intelligence
for Human-Computer Interaction at the University of the Cumberlands.

The chatbot is an updated version of a traditional rule-based
chatbot developed earlier in the course.

The purpose of this project is to demonstrate adaptive
human-computer interaction by allowing the chatbot to remember
previous conversation topics and adjust its responses.

## Features

- Provides information about investigative services.
- Recognizes questions about background investigations.
- Recognizes questions about social media investigations.
- Remembers the user's previous topic during a conversation.
- Provides additional information when the user asks "Tell me more."
- Adjusts its responses when the user changes topics.
- Requests clarification when no previous topic is available.

## Technologies Used

- Python
- Microsoft Bot Framework SDK
- Bot Framework Emulator
- Temporary conversation memory using a Python dictionary

## How It Works

The chatbot uses predefined rules to recognize user questions.

When a user asks about background investigations or social media
investigations, the chatbot stores the topic in memory.

If the user asks "Tell me more," the chatbot checks the previous
topic and provides additional information related to that topic.

If no previous topic exists, the chatbot asks the user to clarify
what information they would like.

Conversation memory is temporary and resets when the application
is restarted.

## Running the Chatbot

1. Install the Python dependencies listed in requirements.txt.
2. Run the application using: python app.py
3. Open Microsoft Bot Framework Emulator.
4. Connect to: http://localhost:3978/api/messages
5. Begin interacting with the chatbot.

## Testing

The chatbot was tested using Microsoft Bot Framework Emulator.

Three scenarios were successfully tested:

1. Remembering a background investigation topic.
2. Switching to social media investigations and updating responses.
3. Requesting clarification when no previous topic exists.

All three tests produced the expected responses.

## Limitations

This chatbot is a beginner-level, rule-based adaptive system.
It does not use machine learning or generative artificial intelligence.

The chatbot recognizes a limited number of keywords and follow-up
phrases. Conversation memory is stored temporarily while the
application is running.

## Academic Purpose

This project was developed as an educational demonstration
of adaptive human-computer interaction.
