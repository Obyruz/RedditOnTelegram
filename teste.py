import sys
import telepot
import praw
import random
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent

already_done = list()

TOKEN = sys.argv[1]  # get token from command-line
user = sys.argv[2]
password = sys.argv[3]

def retrieve_something_from_subreddit(query_string):
    r = praw.Reddit(client_id='xawRpGMefmhiQA',
                    client_secret='Zjqm6ia5a8Gmx8s5ioNNKZPVebU',
                    password=password,
                    user_agent='testscript by /u/scripaman',
                    username=user)
    r.config._ssl_url = None
    subreddit = r.subreddit(query_string)
    submissions = subreddit.hot()
    #limit = 100
    #randNumber = random.randint(1,limit)

    for submission in submissions:
        if submission.id in already_done:
            continue
        else:
            break


    url_text = submission.url
    print ('[LOG] getting url: ' + url_text)
    already_done.append(submission.id)
    print ('[LOG] Done Getting ' + url_text)

    return submission

def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
        print('Inline Query:', query_id, from_id, query_string)

        response = retrieve_something_from_subreddit(query_string)

        articles = [InlineQueryResultArticle(
                        id='abc',
                        title=response.title,
                        input_message_content=InputTextMessageContent(
                            message_text=response.url
                        )
                   )]

        return articles

    answerer.answer(msg, compute)

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)


bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

bot.message_loop({'inline_query': on_inline_query,
                  'chosen_inline_result': on_chosen_inline_result},
                 run_forever='Listening ...')
