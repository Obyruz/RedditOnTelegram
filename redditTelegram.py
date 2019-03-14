import sys
import telepot
import urllib3
import praw
import random as rand
import subprocess
import json
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultGif, InlineQueryResultPhoto, InlineQueryResultVideo

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

nsfw_list = ['gonewild','holdthemoan','RealGirls','nsfw','NSFW_GIF','nsfw_gifs','rule34','LegalTeens','NSFWFunny','GirlsFinishingTheJob','OnOff','60fpsporn','hentai','TittyDrop','hugeboobs','palegirls','StraightGirlsPlaying','HappyEmbarrassedGirls','GWNerdy','wifesharing','AnalGW','Bondage','juicyasians','GirlswithGlasses','datgap','SexyButNotPorn','Blowjobs','ShinyPorn','stockings','LipsThatGrip','fitgirls','lingerie','gonewildcolor','legs','BonerMaterial','rearpussy','boobs','ecchi','grool','boltedontits','bdsm','gonewildcurvy','Amateur','WouldYouFuckMyWife','suicidegirls','altgonewild','buttplug','collegesluts','TotallyStraight','NSFW_HTML5','O_Faces','gonewildstories','gwcumsluts','AsiansGoneWild','GoneWildPlus','HighResNSFW','asshole','lesbians','CelebFakes','Innie','voluptuous','nsfwoutfits','deepthroat','GroupOfNudeGirls','thinspo','GoneWildSmiles','AmateurArchives','BigBoobsGonewild','DarkAngels','pantsu','nsfwhardcore','pussy','Stacked','tightdresses','dirtysmall','TessaFowler','FlashingGirls','treesgonewild','CelebrityButts','facedownassup','EngorgedVeinyBreasts','NSFWCostumes','girlsinleggings','bikinis','FestivalSluts','WomenOfColor','IndiansGoneWild','LabiaGW','boobbounce','leotards','bimbofetish','burstingout','randomsexiness','BDSMGW','latinas','Bottomless_Vixens','trashyboners','SexyTummies','booty','Hotwife','assinthong','ClopClop','cleavage','Upskirt','bigasses','Sukebei','havoc_bot','bestofcollege','gifsgonewild','UnderwearGW','tight_shorts','shorthairchicks','Unashamed','Blonde','WorkIt','Rule34LoL','brunette','simps','pokies','SoFuckable','NSFW_Japan','porninfifteenseconds','tanlines','dirtykikpals','photoplunder','aa_cups','bestofboobies','OnHerKnees','skinnytail','YogaPants','nsfwcosplay','FacialFun','Saggy','Playboy','whooties','IndianBabes','Ebony','kinksters_gone_wild','iWantToFuckHer','jilling','AsianNSFW','GirlswithNeonHair','GloriaV','RepressedGoneWild','AthleticGirls','ExhibitionistSex','asstastic','celebnsfw','redheads','Hotchickswithtattoos','curvy','wincest','BigBlackBootyGIFS','bigareolas','workgonewild','WtSSTaDaMiT','homegrowntits','TinyTits','anal','PetiteGoneWild','ginger','AsianHotties','Nipples','GirlsinStripedSocks','CelebrityNipples','LoveToWatchYouLeave','rule34_comics','DirtySnapchat','TightShorts','camwhores','Pantyfetish','tits','collared','NSFW_Wallpapers','BreastEnvy','petite','littlespace','GiannaMichaels','NSFW_nospam','xray','snapchat_sluts','runwaynudity','highheelsNSFW','suctiondildos','assholegonewild','bodyshots','SexyFrex','ThickChixxx','rule34celebs','hardanal','ravenhaired','WomenOfColour','TributeMe','ChangingRooms','Page3Glamour','PornGifsbyBot','TheHangingBoobs','thighhighs','dykesgonewild','hugenaturals','StretchingIt','AvatarPorn','doujinshi','Femdom','bustyasians','cat_girls','squirting','nsfw2','BeautifulTitsAndAss','Workoutgonewild','LatinasGW','DirtyFamilyPhotos','naturists','BlowjobGifs','wet','Exxxtras','MiddleEasternHotties','CamelToeGirls','IncestPorn','sexygirlsinjeans','leannadecker','mycleavage','CelebrityPussy','comics18_story','ImaginaryBoners','YAYamateurs','MouthWideOpen','bustybabes','insertions','gettingherselfoff','downblouse','girlsinyogapants','groupsex','realbikinis','forcedorgasms','xxxcaptions','nipslip','VintageBabes','OldSchoolCoolNSFW','Xsome','HomemadeNsfw','GirlsCuddling','facesitting','FilthyGirls','CellShots','randomsexygifs','HENTAI_GIF','panties','sex_comics','creampies','gape','petplay','SexInFrontOfOthers','asslick','Presenting','AsianPorn','girlskissing','NSFW_Snapchat','Mooning','NotSafeForNature','SexiestPetites','milf','Boobies','ass','BustyPetite','Sexy','TheUnderbun','adultgifs','BondageBlowjobs','areolas','seethru','augustames','boobgifs','beach','realbrides','UnrealGirls','maturemilf','AsianHottiesGIFS','Curls','buttsex','bestoflingerie','bestofblowjobs','MonsterGirl','mellisaclarke','AssholeBehindThong','vagina','lesdom','HungryButts','PiercedNSFW','girlswhoride','BustyNaturals','ATPorn','hentaibondage','femalepov','JapanesePorn2','HardBoltOns','WeddingRingsShowing','Anjelica_Ebbi','celebsunleashed','thefullbush','WoahPoon','upherbutt','O_Face','GirlsInSocks','xsmallgirls','tightsqueeze','throatpies','vulva','freshfromtheshower','leggingsgonewild','tailplug','booty_gifs','KanMusuNights','lifeisabeach','BoltedOnBooty','PublicFlashing','Puffies','PantiesToTheSide','SluttyStrangers','treatemright','FaceAndAsshole','SceneGirls','naturaltitties','NSFW_Korea','WarriorWomen','SexyInJeans','cameltoe','gonewilder','FaceFuck','ComplexionExcellence','celebsnaked','Ohlympics','milf_nowandforever','SexyGirlsInBoots','NowYouReallySeeMe','jobuds','Facials','AsianFetish','IntenseBDSM','ToplessInJeans','DrunkGirls','Milfinstockings','SUMMERtimeheat','GOTporn','Hotness','ChristianGirls','GirlsWithToys','youtubetitties','selfshots','BoltedOnMaxed','IndianPorn','lactation','Gemplugs','Trim','womenofcolorXXX','SpreadEm','spreading','KateeOwen','OnlyGoodPorn','dreamjobs','PussyJuices','BigBoobsGW','RuinedOrgasms','JulieKennedy','NSFW411','metart','rule34_albums','funsized','starwarsnsfw','Titties','braandpanties','barelylegalteens','UncutPorn','dopplebangher','MariaRyabushkina','Oilporn','rule34pinups','legwrap','twerking','Nekomimi','maturewoman','cuckquean','yuri','Morphs','cunnilingus','NSFW_Hardbodies','rule34feet','pantyhose','TopDownThong','MiaMalkova','titstouchingtits','MyCherryCrush','ButtSharpies','Stoyaxxx','TopsAndBottoms','BreastExpansion','thick_clothed','pronebone','Gravure','BorednIgnored','chickflixxx','StomachDownFeetUp','ButtsAndBareFeet','legsup','PussyMound','spreadeagle','outercourse','sodomy','airboobs','cougars','Spanking']

TOKEN = sys.argv[1]  # get token from command-line
user = sys.argv[2]
password = sys.argv[3]
gfycat_user = sys.argv[4]
gfycat_TOKEN = sys.argv[5]

gfycat_auth = "https://api.gfycat.com/v1/oauth/token"
gfycat_credentials = '{"client_id":gfycat_user, "client_secret": gfycat_TOKEN, "grant_type": "client_credentials"}'

r = praw.Reddit(client_id='xawRpGMefmhiQA',
                client_secret='Zjqm6ia5a8Gmx8s5ioNNKZPVebU',
                password=password,
                user_agent='testscript by /u/scripaman',
                username=user)

def handle(msg):
    if 'text' in msg:
        random(msg)
        chat_id = msg['chat']['id']
    elif 'query' in msg:
        on_inline_query(msg)
    elif content_type == 'chosen_inline_result':
        on_chosen_inline_result(msg)

def random(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    json_data = subprocess.run(["curl", "-v", "-XPOST", "-d", gfycat_credentials, gfycat_auth], capture_output=True)
    gfycat_bearer = json.loads(json_data)
    
    if msg['text'] == '/random' or msg['text'] == '/random@redditTelegram_bot':
        result, subredditName = retrieve_random_submission()

        print(result.url)

        if result.url[:5] == 'https':
            gfycat = result.url[8:14]
        else:
            gfycat = result.url[7:13]

        if gfycat == 'gfycat':
            pos_id = [pos for pos, char in enumerate(s) if char == '/']
            gfycat_id = gfycat_id[pos_id+1:]
            
            json_data = subprocess.run(["curl", "-X", "GET", "https://api.gfycat.com/v1/gfycats/" + pos_id, "-H", "Authorization: Bearer " + gfycat_bearer["acess_token"]])
            gfycat_json = json.loads(json_data)

        if result.url[-3:] == 'jpg' or result.url[-3:] == 'png' or result.url[8:17] == "i.redd.it":
            bot.sendPhoto(chat_id, result.url)
        elif gfycat == 'gfycat' or result.url[-3:] == 'gif' or result.url[-4:] == 'gifv':
            bot.sendVideo(chat_id, result.url)
        elif gfycat == 'gfycat':
            bot.sendVideo(chat_id, gfycat_json["gfyItem"]["max5mbGif"])
        elif result.url[8:17] == "v.redd.it":
            bot.sendVideo(chat_id, result.url)
        else:
            bot.sendMessage(chat_id, result.url)
        bot.sendMessage(chat_id, 'sent from: ' + subredditName)

    

def retrieve_random_submission():
    subredditPos = rand.randint(0, len(nsfw_list)-1)
    submissionPos = rand.randint(1, 50)
    subredditName = nsfw_list[subredditPos]
    subreddit = r.subreddit(subredditName)
    submissions = subreddit.hot(limit=50)
    submissionsList = list(submissions)
    submission = submissionsList[submissionPos]

    return submission, subredditName

def retrieve_something_from_subreddit(query_string):
    subreddit = r.subreddit(query_string)
    submissions = subreddit.hot(limit=25)
    
    return submissions

def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
        print ('Inline Query:', query_id, from_id, query_string)
        
        responses = retrieve_something_from_subreddit(query_string)
        
        json_data = subprocess.run(["curl", "-XPOST", "-d", gfycat_credentials, gfycat_auth], capture_output=True)
        print(json_data)
        gfycat_bearer = json.loads(json_data)
        
        count = 0
        for response in responses:
            try:
                urlFormat = response.url[-4:]

                if response.url[:5] == 'https':
                    gfycat = response.url[8:14]
                else:
                    gfycat = response.url[7:13]

                if urlFormat == 'gifv':
                    response.url = response.url[:-1]

                print(response.url)

                if count == 0:
                    if response.url[-3:] == 'gif' or response.url[-4:] == 'gifv':
                        articles = [InlineQueryResultGif(
                                        id=response.id,
                                        type='gif',
                                        title=response.title,
                                        gif_width=10,
                                        gif_height=10,
                                        gif_url=response.url,
                                        thumb_url=response.url
                                   )]
                    elif gfycat == 'gfycat':
                        pos_id = [pos for pos, char in enumerate(s) if char == '/']
                        gfycat_id = gfycat_id[pos_id+1:]
                        
                        json_data = subprocess.run(["curl", "-X", "GET", "https://api.gfycat.com/v1/gfycats/" + gfycat_id, "-H", "Authorization: Bearer " + gfycat_bearer["acess_token"]])
                        gfycat_json = json.loads(json_data)
                        
                        articles = [InlineQueryResultGif(
                                        id=response.id,
                                        type='gif',
                                        title=response.title,
                                        gif_width=10,
                                        gif_height=10,
                                        gif_url=gfycat_json["gfyItem"]["max5mbGif"],
                                        thumb_url=gfycat_json["gfyItem"]["max1mbGif"]
                                    )]
                    elif response.url[-3:] == 'png' or response.url[-3:] == 'jpg' or response.url[8:17] == "i.redd.it":
                        articles = [InlineQueryResultPhoto(
                                        id=response.id,
                                        type='photo',
                                        photo_url=response.url,
                                        thumb_url=response.url,
                                        photo_width=10,
                                        photo_height=10
                                   )]
                    #elif response.url[8:17] == "v.redd.it":
                    #    articles = [InlineQueryResultVideo(
                    #                    id=response.id,
                    #                    type='video',
                    #                    title=response.title,
                    #                    video_url=response.url,
                    #                    thumb_url=response.url,
                    #                    video_width=50,
                    #                    video_height=50,
                    #                    mime_type='video/mp4'
                    #                )]
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
                    if response.url[-3:] == 'gif' or response.url[-4:] == 'gifv':
                        articles += [InlineQueryResultGif(
                                        id=response.id,
                                        type='gif',
                                        title=response.title,
                                        gif_width=10,
                                        gif_height=10,
                                        gif_url=response.url,
                                        thumb_url=response.url
                                   )]
                    elif gfycat == 'gfycat':
                        json_data = subprocess.run(["curl", "-X", "GET", "https://api.gfycat.com/v1/gfycats/" + result.url, "-H", "Authorization: Bearer " + gfycat_bearer["acess_token"]])
                        gfycat_json = json.loads(json_data)
                        
                        articles += [InlineQueryResultGif(
                                         id=response.id,
                                         type='gif',
                                         title=response.title,
                                         gif_width=10,
                                         gif_height=10,
                                         gif_url=gfycat_json["gfyItem"]["max5mbGif"],
                                         thumb_url=gfycat_json["gfyItem"]["max1mbGif"]
                                    )]
                    elif response.url[-3:] == 'png' or response.url[-3:] == 'jpg' or response.url[8:17] == "i.redd.it":
                        articles += [InlineQueryResultPhoto(
                                        id=response.id,
                                        type='photo',
                                        photo_url=response.url,
                                        thumb_url=response.url,
                                        photo_width=10,
                                        photo_height=10
                                   )]
                    #elif response.url[8:17] == "v.redd.it":
                    #    articles += [InlineQueryResultVideo(
                    #                    id=response.id,
                    #                    type='video',
                    #                    title=response.title,
                    #                    video_url=response.url,
                    #                    thumb_url=response.url,
                    #                    video_width=50,
                    #                    video_height=50,
                    #                    mime_type='video/mp4'
                    #                )]
                    else:
                        articles += [InlineQueryResultArticle(
                                        id=response.id,
                                        title=response.title,
                                        thumb_url=response.url,
                                        input_message_content=InputTextMessageContent(
                                            message_text=response.url + ' powered by: ' + response.subreddit_name_prefixed
                                        )
                                   )]
            except:
                print("Error at " + response.url)
                print(response.media)
                print(response.media_embed)
        return articles

    answerer.answer(msg, compute)


def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)


bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

bot.message_loop(handle,
                 run_forever='Listening ...')
