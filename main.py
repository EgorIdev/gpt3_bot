import openai
import telebot
from os import getenv

openai.api_key = getenv("OPENAI_API_KEY")
bot = telebot.TeleBot(getenv("TG_KEY_FOR_OPENAI"))

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=2048,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You: "]
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


if __name__ == '__main__':
    bot.polling()