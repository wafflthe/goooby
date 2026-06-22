from logging import Logger
from slack_sdk import WebClient
from database import get_ideas


def app_home_opened_callback(client: WebClient, event: dict, logger: Logger):
    # ignore the app_home_opened event for anything but the Home tab
    if event["tab"] != "home":
        return
    
    user_id = event["user"]
    ideas = get_ideas(user_id)
    user_info = client.users_info(user=user_id)
    display_name = user_info["user"]["profile"]["display_name"]

    blocks = []

    if ideas:
        blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"Heres yer awesome ideas {display_name}"}
        })
        
        for idea in ideas:
            blocks.append({
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"- {idea}"}
            })

    else:
        blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": "No ideas yet :heaviersob: :heaviersob: :heaviersob: use /add_ideas to add some!"}
        })

    try:
        client.views_publish(
            user_id=user_id,
            view={ 
                "type": "home",
                "blocks": blocks
            }
        )
        
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
