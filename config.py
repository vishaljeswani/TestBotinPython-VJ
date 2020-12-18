#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "0bbcf3eb-f129-4ac6-93af-b0ab224485d6")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "c022d1cf-76cd-40f9-8f56-bc88533b69c3")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId","31076320-63db-4d6c-a30a-a6ce4abc4ba5")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey","18116bf012144730afa5db1593c72591")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName","https://chatbot-demo-vj.cognitiveservices.azure.com/qnamaker")
