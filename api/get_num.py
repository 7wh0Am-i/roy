import requests
import json
from telegram.ext import ContextTypes

async def get_num(update, context: ContextTypes.DEFAULT_TYPE):
    """ Fetch mobile information for the /num command """
    if not context.args:
        await update.message.reply_text(
            "Please provide a 10-digit mobile number, e.g., /num 1234567890"
        )
        return

    mobile_number = context.args[0]
    if not (mobile_number.isdigit() and len(mobile_number) == 10):
        await update.message.reply_text("Please provide a valid 10-digit mobile number.")
        return

    try:
        cookies = {
            '__test': '70c6868076eba2e46440dadfa9d446f7',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                      'image/avif,image/webp,image/apng,*/*;q=0.8,'
                      'application/signed-exchange;v=b3;q=0.7',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'http://osintx.info/API/krobetahack.php?key=P6NW6D1',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,bn;q=0.6',
        }

        params = {
            'key': 'P6NW6D1',
            'type': 'mobile',
            'term': mobile_number,
        }

        response = requests.get(
            'http://osintx.info/API/krobetahack.php',
            params=params,
            cookies=cookies,
            headers=headers
        )

        # Try JSON
        try:
            raw_data = response.json()
        except ValueError:
            raw_data = response.text

        # If still string, try parsing again
        if isinstance(raw_data, str):
            try:
                raw_data = json.loads(raw_data)
            except Exception:
                pass

        response_data = {
            "status": "success",
            "message": f"Information retrieved for {mobile_number}",
            "data": raw_data
        }

        # Format JSON in quote block
        pretty_json = json.dumps(response_data, ensure_ascii=False, indent=2)
        quoted_msg = f"```json\n{pretty_json[:3900]}\n```"  # keep inside Telegram limit

        await update.message.reply_text(quoted_msg, parse_mode="MarkdownV2")

    except Exception as e:
        response_data = {
            "status": "error",
            "message": f"Error occurred: {str(e)}",
            "data": {}
        }
        pretty_error = json.dumps(response_data, ensure_ascii=False, indent=2)
        quoted_msg = f"```json\n{pretty_error}\n```"
        await update.message.reply_text(quoted_msg, parse_mode="MarkdownV2")