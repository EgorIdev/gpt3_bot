import openai
import telebot

openai.api_key = "token"
bot = telebot.TeleBot("token")

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=3000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You: "]
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])

bot.polling()