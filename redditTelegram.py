import sys
import telepot
import praw
import random as rand
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultGif, InlineQueryResultPhoto

nsfw_list = ['gonewild','holdthemoan','RealGirls','nsfw','NSFW_GIF','nsfw_gifs','rule34','LegalTeens','NSFWFunny','GWCouples','GirlsFinishingTheJob','OnOff','60fpsporn','hentai','TittyDrop','hugeboobs','palegirls','StraightGirlsPlaying','HappyEmbarrassedGirls','GWNerdy','wifesharing','AnalGW','Bondage','juicyasians','GirlswithGlasses','datgap','homemadexxx','SexyButNotPorn','Blowjobs','ShinyPorn','stockings','LipsThatGrip','fitgirls','lingerie','gonewildcolor','legs','BonerMaterial','rearpussy','boobs','ecchi','grool','boltedontits','bdsm','pornvids','gonewildcurvy','Amateur','WouldYouFuckMyWife','suicidegirls','altgonewild','buttplug','collegesluts','TotallyStraight','NSFW_HTML5','O_Faces','gonewildstories','gwcumsluts','AsiansGoneWild','ladybonersgw','GoneWildPlus','HighResNSFW','porn_gifs','asshole','lesbians','CelebFakes','Innie','voluptuous','nsfwoutfits','deepthroat','dirtypenpals','GroupOfNudeGirls','thinspo','GoneWildSmiles','AmateurArchives','BigBoobsGonewild','DarkAngels','pantsu','nsfwhardcore','pussy','Stacked','tightdresses','dirtysmall','TessaFowler','FlashingGirls','treesgonewild','CelebrityButts','facedownassup','EngorgedVeinyBreasts','NSFWCostumes','girlsinleggings','bikinis','FestivalSluts','WomenOfColor','IndiansGoneWild','LabiaGW','boobbounce','leotards','bimbofetish','burstingout','randomsexiness','passionx','BDSMGW','latinas','Bottomless_Vixens','trashyboners','SexyTummies','booty','Hotwife','assinthong','ClopClop','cleavage','Upskirt','bigasses','Sukebei','havoc_bot','bestofcollege','gifsgonewild','UnderwearGW','tight_shorts','shorthairchicks','Unashamed','Blonde','WorkIt','Rule34LoL','brunette','simps','pokies','SoFuckable','NSFW_Japan','porninfifteenseconds','tanlines','dirtykikpals','gonewildcouples','photoplunder','aa_cups','bestofboobies','OnHerKnees','skinnytail','pornID','YogaPants','nsfwcosplay','FacialFun','Saggy','Playboy','whooties','IndianBabes','Ebony','kinksters_gone_wild','iWantToFuckHer','jilling','AsianNSFW','GirlswithNeonHair','GloriaV','BDSMcommunity','RepressedGoneWild','AthleticGirls','ExhibitionistSex','asstastic','celebnsfw','redheads','Hotchickswithtattoos','curvy','wincest','BigBlackBootyGIFS','bigareolas','workgonewild','WtSSTaDaMiT','homegrowntits','TinyTits','anal','GoneMild','PetiteGoneWild','ginger','AsianHotties','Nipples','GirlsinStripedSocks','PornGifs','CelebrityNipples','LoveToWatchYouLeave','rule34_comics','DirtySnapchat','TightShorts','camwhores','Pantyfetish','tits','Sexsells','collared','NSFW_Wallpapers','BreastEnvy','petite','littlespace','GiannaMichaels','NSFW_nospam','xray','snapchat_sluts','runwaynudity','highheelsNSFW','RateMyNudeBody','suctiondildos','assholegonewild','bodyshots','SexyFrex','ThickChixxx','rule34celebs','hardanal','ravenhaired','WomenOfColour','TributeMe','ChangingRooms','Page3Glamour','PornGifsbyBot','TheHangingBoobs','thighhighs','dykesgonewild','hugenaturals','StretchingIt','AvatarPorn','doujinshi','Femdom','bustyasians','cat_girls','dirtyr4r','squirting','nsfw2','BeautifulTitsAndAss','painal','Workoutgonewild','LatinasGW','DirtyFamilyPhotos','naturists','BlowjobGifs','	wet','Exxxtras','MiddleEasternHotties','CamelToeGirls','IncestPorn','sexygirlsinjeans','leannadecker','normalnudes','mycleavage','CelebrityPussy','comics18_story','ImaginaryBoners','YAYamateurs','MouthWideOpen','bustybabes','insertions','gettingherselfoff','downblouse','porn','girlsinyogapants','GoneWildTube','groupsex','realbikinis','forcedorgasms','xxxcaptions','nipslip','VintageBabes','OldSchoolCoolNSFW','Xsome','HomemadeNsfw','BDSMpersonals','GirlsCuddling','facesitting','FilthyGirls','CellShots','randomsexygifs','HENTAI_GIF','panties','sex_comics','creampies','gape','Singlets','petplay','SexInFrontOfOthers','asslick','Presenting','AsianPorn','girlskissing','NSFW_Snapchat','Mooning','NotSafeForNature','SexiestPetites','milf','Boobies','ass','BustyPetite','Sexy','TheUnderbun','adultgifs','BondageBlowjobs','areolas','seethru','augustames','boobgifs','beach','realbrides','UnrealGirls','maturemilf','AsianHottiesGIFS','Curls','buttsex','bestoflingerie','bestofblowjobs','MonsterGirl','mellisaclarke','AssholeBehindThong','vagina','lesdom','HungryButts','PiercedNSFW','girlswhoride','BustyNaturals','ATPorn','hentaibondage','femalepov','JapanesePorn2','HardBoltOns','WeddingRingsShowing','Anjelica_Ebbi','celebsunleashed','thefullbush','WoahPoon','upherbutt','PornStars','O_Face','GirlsInSocks','xsmallgirls','tightsqueeze','throatpies','Hugeboobshardcore','vulva','freshfromtheshower','leggingsgonewild','tailplug','booty_gifs','KanMusuNights','lifeisabeach','BoltedOnBooty','PublicFlashing','Puffies','PantiesToTheSide','SluttyStrangers','treatemright','FaceAndAsshole','bigonewild','SceneGirls','naturaltitties','NSFW_Korea','WarriorWomen','SexyInJeans','cameltoe','gonewilder','FaceFuck','ComplexionExcellence','celebsnaked','Ohlympics','milf_nowandforever','SexyGirlsInBoots','NowYouReallySeeMe','jobuds','Facials','AsianFetish','IntenseBDSM','ToplessInJeans','DrunkGirls','Milfinstockings','SUMMERtimeheat','GOTporn','Hotness','ChristianGirls','GirlsWithToys','youtubetitties','selfshots','BoltedOnMaxed','IndianPorn','lactation','Gemplugs','Trim','womenofcolorXXX','SpreadEm','spreading','KateeOwen','OnlyGoodPorn','dreamjobs','PussyJuices','BigBoobsGW','RuinedOrgasms','JulieKennedy','NSFW411','metart','rule34_albums','funsized','starwarsnsfw','Titties','braandpanties','barelylegalteens','UncutPorn','submittedts','dopplebangher','MariaRyabushkina','Oilporn','rule34pinups','legwrap','twerking','Nekomimi','maturewoman','gingerdudes','cuckquean','yuri','Morphs','nsfw_videos','cunnilingus','NSFW_Hardbodies','rule34feet','pantyhose','TopDownThong','MiaMalkova','titstouchingtits','MyCherryCrush','ButtSharpies','Stoyaxxx','AskRedditAfterDark','TopsAndBottoms','Bisexy','selfservice','BreastExpansion','thick_clothed','pronebone','Gravure','BorednIgnored','chickflixxx','StomachDownFeetUp','ButtsAndBareFeet','legsup','PussyMound','GoneErotic','spreadeagle','outercourse','sodomy','airboobs','cougars','Spanking']

TOKEN = sys.argv[1]  # get token from command-line
user = sys.argv[2]
password = sys.argv[3]

r = praw.Reddit(client_id='xawRpGMefmhiQA',
                client_secret='Zjqm6ia5a8Gmx8s5ioNNKZPVebU',
                password=password,
                user_agent='testscript by /u/scripaman',
                username=user)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        random(msg)
    elif content_type == 'inline_query':
        on_inline_query(msg)
    elif content_type == 'chosen_inline_result':
        on_chosen_inline_result(msg)

def random(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if msg['text'] == '/random' or msg['text'] == '/random@redditTelegram_bot':
        result, subredditName = retrieve_random_submission()
        print(result.url)

        if result.url[-3:] == 'jpg' or result.url[-3:] == 'png':
            bot.sendPhoto(chat_id, result.url)
        elif result.url[-3:] == 'gif' or result.url[-4:] == 'gifv':
            bot.sendDocument(chat_id, result.url)
        else:
            bot.sendMessage(chat_id, result.url)
    bot.sendMessage(chat_id, 'powered by: ' + subredditName)

    

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

        count = 0
        for response in responses:
            urlFormat = response.url[-4:]

            if response.url[:5] == 'https':
                gfycat = response.url[8:14]
            else:
                gfycat = response.url[7:13]

            if urlFormat == 'gifv':
                response.url = response.url[:-1]
            if gfycat == 'gfycat':
                response.url = 'https://thumbs.gfycat.com/' + response.url[19:] + '-small.gif'

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

bot.message_loop(handle,
                 run_forever='Listening ...')
