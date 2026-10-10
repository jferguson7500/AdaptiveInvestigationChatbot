# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount


class EchoBot(ActivityHandler):

    def __init__(self):
        self.user_topics = {}

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    "Hello and welcome! Type 'help' to see what I can do."
                )

    async def on_message_activity(self, turn_context: TurnContext):
        user_message = turn_context.activity.text.lower().strip()

        conversation_id = turn_context.activity.conversation.id
        last_topic = self.user_topics.get(conversation_id)
        topic = None

        if user_message in ["tell me more", "more information", "explain more"]:
            if last_topic == "background":
                response = (
                    "Background investigations may also identify previous addresses, "
                    "business affiliations, and information relevant to legal matters."
                )

            elif last_topic == "social media":
                response = (
                    "Social media investigations may identify public posts, "
                    "photographs, activities, and other information relevant to a case."
                )

            else:
                response = (
                    "What would you like to know more about? "
                    "I can explain background checks or social media investigations."
                )

        elif user_message in ["hello", "hi", "hey"]:
            response = "Hello! I am a simple investigation services chatbot."

        elif user_message in ["help", "services", "what can you do"]:
            response = (
                "I can provide information about background checks, "
                "social media investigations, and general investigation services."
            )

        elif "background" in user_message:
            topic = "background"
            response = (
                "Background checks can include identity verification, "
                "address history, public records, and other available information."
            )

        elif "social media" in user_message:
            topic = "social media"
            response = (
                "Social media investigations can review publicly available online "
                "content that may be relevant to an investigation."
            )

        elif "investigation" in user_message:
            response = (
                "Investigation services may include background research, "
                "social media research, witness information, and other fact-finding."
            )

        else:
            response = (
                "I am sorry, I do not understand that request. "
                "Type 'help' to see what I can answer."
            )

        if topic is not None:
            self.user_topics[conversation_id] = topic

        await turn_context.send_activity(MessageFactory.text(response))
