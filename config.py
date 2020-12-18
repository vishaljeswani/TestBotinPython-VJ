#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "1b4cc46d-f970-47a8-96d8-849deeb250f7")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "NG~jsW.B6f~y_8vQF0lMq18~3O6DYudQ72")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId","d4932eaf-3c24-4cd6-b46e-018466fd957c")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey","4fc3219d-39f9-4437-88a2-e6e7340a6570")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName","https://chatbot-ks1.azurewebsites.net/qnamaker")
