import sys
import telepot
import praw
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent

checkWords = ['i.imgur.com',  'jpg', 'png',]

r = praw.Reddit(client_id='Igz_l72azyYSag',
                 client_secret='6RqOPrzRQC79SabNbIktD-QkoYA',
                 password='somethinghere',
                 user_agent='testscript by /u/scripaman',
                 username='scripaman')

def retrieve_something_from_subreddit(query_string):
    subreddit = r.subreddit(query_string)
    already_done = list()
    for submission in subreddit.hot(limit=1):
        url_text = submission.url
        has_domain = any(string in url_text for string in checkWords)
        print '[LOG] getting url: ' + url_text
        if submission.id not in already_done and has_domain:
            already_done.append(submission.id)
            print '[LOG] Done Getting ' + url_text
    return url_text

def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
        print('Inline Query:', query_id, from_id, query_string)

        articles = [InlineQueryResultArticle(
                        id='abc',
                        title=query_string,
                        input_message_content=InputTextMessageContent(
                            message_text=retrieve_something_from_subreddit(query_string)
                        )
                   )]

        return articles

    answerer.answer(msg, compute)

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

bot.message_loop({'inline_query': on_inline_query,
                  'chosen_inline_result': on_chosen_inline_result},
                 run_forever='Listening ...')
