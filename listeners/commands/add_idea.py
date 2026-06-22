from slack_bolt import Ack, Respond
from logging import Logger
from slack_sdk import WebClient
from database import add_idea
from listeners.events.app_home_opened import app_home_opened_callback

def idea_callback(command, ack: Ack, client: WebClient, respond: Respond, logger: Logger):
    try:
        ack()
        idea = command['text']
        user_id =  command['user_id']

        if idea:
            respond(f"Idea added: {idea}")
            add_idea(idea, user_id)
            app_home_opened_callback(client, {"user": user_id, "tab": "home"}, logger)
        else:
            respond("NO idea :heaviersob: :heaviersob: :heaviersob: go HAVE one then come back to save it!!!")
    except Exception as e:
        logger.error(e)