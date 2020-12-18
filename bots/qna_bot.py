# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
from botbuilder.schema import CardAction, ActionTypes, SuggestedActions

from config import DefaultConfig


class QnABot(ActivityHandler):
    def __init__(self, config: DefaultConfig):
        self.qna_maker = QnAMaker(
            QnAMakerEndpoint(
                knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
                endpoint_key=config.QNA_ENDPOINT_KEY,
                host=config.QNA_ENDPOINT_HOST,
            )
        )

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
       """
        Send a welcome message to the user and tell them what actions they may perform to use this bot
        """

       return await self._send_welcome_message(turn_context)

    async def _send_welcome_message(self, turn_context: TurnContext):
        for member in turn_context.activity.members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    MessageFactory.text(
                        f"Hi! I am Vizard. I can help answer your questions on CEMEA solutions."
                    )
                )

                await self._send_suggested_actions(turn_context)


    async def on_message_activity(self, turn_context: TurnContext):
        # The actual call to the QnA Maker service.
        #first_response = ["CLM", "Cross Border", "Global Auth", "EDS"]
        response = await self.qna_maker.get_answers(turn_context)
        
        #if turn_context in first_response:
         #   await turn_context.send_activity("Please type your question")
        if response and len(response) > 0:
            await turn_context.send_activity(MessageFactory.text(response[0].answer))
        else:
            await turn_context.send_activity("I was not able to find a suitable response for your question. Please raise a request with the SST team for further clarification - http://bit.ly/Query_SST")


    async def _send_suggested_actions(self, turn_context: TurnContext):
        """
        Creates and sends an activity with suggested actions to the user. When the user
        clicks one of the buttons the text value from the "CardAction" will be displayed
        in the channel just as if the user entered the text. There are multiple
        "ActionTypes" that may be used for different situations.
        """

        reply = MessageFactory.text("Please select a solution to proceed.")

        reply.suggested_actions = SuggestedActions(
            actions=[
                CardAction(
                    title="CLM",
                    type=ActionTypes.im_back,
                    value="CLM",
		    #text="Please type your question.",
                    #display_text="Please type your question."
                ),
                CardAction(
                    title="Cross Border",
                    type=ActionTypes.im_back,
                    value="Cross Border",
		    #text="Please type your question.",
                    #display_text="Please type your question.",
                ),
                CardAction(
                    title="EDS",
                    type=ActionTypes.im_back,
                    value="EDS",
		    #text="Please type your question.",
                    #display_text="Please type your question."
                ),
                CardAction(
                    title="Global Authorization",
                    type=ActionTypes.im_back,
                    value="Global Authorization",
		    #text="Please type your question.",
                    #display_text="Please type your question."
                ),
            ]
        )

        return await turn_context.send_activity(reply)
