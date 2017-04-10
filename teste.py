import sys
import telepot
import praw
import random
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultGif, InlineQueryResultPhoto

already_done = list()

TOKEN = sys.argv[1]  # get token from command-line
user = sys.argv[2]
password = sys.argv[3]

r = praw.Reddit(client_id='xawRpGMefmhiQA',
                client_secret='Zjqm6ia5a8Gmx8s5ioNNKZPVebU',
                password=password,
                user_agent='testscript by /u/scripaman',
                username=user)

def retrieve_something_from_subreddit(query_string):
    subreddit = r.subreddit(query_string)
    submissions = subreddit.hot(limit=25)
#    for submission in submissions:
#        vars(submission)
#    count = 0
#    for submission in submissions:
#        print ('Submissão número: ' + str(count) + '\n')
#        print (submission)
#        count += 1
    #limit = 100
    #randNumber = random.randint(1,limit)


#    url_text = submission.url
#    print ('[LOG] getting url: ' + url_text)
#    already_done.append(submission.id)
#    print ('[LOG] Done Getting ' + url_text)

    return submissions

def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
        print ('Inline Query:', query_id, from_id, query_string)

        responses = retrieve_something_from_subreddit(query_string)

        count = 0
        for response in responses:
            iimgur = ''

            urlFormat = response.url[-4:]
            if response.url[:5] == 'https':
                gfycat = response.url[8:14]
                iimgur = response.url[9:10]
            else:
                gfycat = response.url[7:13]

            if urlFormat == 'gifv':
                response.url = response.url[:-1]
            if gfycat == 'gfycat':
                response.url = 'https://thumbs.gfycat.com/' + response.url[19:] + '-small.gif'
            if iimgur == 'i.':
                response.url = response.url[:5] + response.url[11:]
                response.url = response.url[:-3]

            print(response.url)

            if count == 0:
                if response.url[-3:] == 'gif':
                    articles = [InlineQueryResultGif(
                                    id=response.id,
                                    type='gif',
                                    title=response.title,
                                    gif_url=response.url,
                                    gif_width=50,
                                    gif_height=50,
                                    thumb_url=response.url
                               )]
                elif response.url[-3:] == 'png' or response.url[-3:] == 'jpg':
                    articles = [InlineQueryResultPhoto(
                                    id=response.id,
                                    type='photo',
                                    photo_url=response.url,
                                    thumb_url=response.url,
                               )]
                else:
                    articles = [InlineQueryResultArticle(
                                    id=response.id,
                                    title=response.title,
                                    thumb_url=response.url,
                                    input_message_content=InputTextMessageContent(
                                        message_text=response.url + ' powered by: ' + response.subreddit_name_prefixed
                                    )
                               )]                    
                count += 1
            else:
                if response.url[-3:] == 'gif':
                    articles += [InlineQueryResultGif(
                                    id=response.id,
                                    type='gif',
                                    title=response.title,
                                    gif_width=200,
                                    gif_height=200,
                                    gif_url=response.url,
                                    thumb_url=response.url
                               )]
                elif response.url[-3:] == 'png' or response.url[-3:] == 'jpg':
                    articles += [InlineQueryResultPhoto(
                                    id=response.id,
                                    type='photo',
                                    photo_url=response.url,
                                    thumb_url=response.url,
                               )]
                else:
                    articles += [InlineQueryResultArticle(
                                    id=response.id,
                                    title=response.title,
                                    thumb_url=response.url,
                                    input_message_content=InputTextMessageContent(
                                        message_text=response.url + ' powered by: ' + response.subreddit_name_prefixed
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
