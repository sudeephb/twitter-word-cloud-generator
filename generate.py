import json
import twitter 
import preprocessor as p
import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import sys

def main():
    if len(sys.argv) < 2:
        print('Error! \nUsage: python generate.py username [filename]')
        return

    else:
        if len(sys.argv) == 3:
            file_name = f'{sys.argv[2]}.png'
        else:
            file_name = 'my_wordcloud.png'
        screen_name = sys.argv[1]

    try:
        f = open('keys.json', 'r')
        data = json.load(f)
        f.close()

        api = twitter.Api(
            consumer_key=data['consumer_key'],
            consumer_secret=data['consumer_secret'],
            access_token_key=data['access_token_key'],
            access_token_secret=data['access_token_secret'])


    except:
        print('Error in authentication! \nMake sure you have all the credentials filled properly in keys.json file.')
        return

    all_statuses = []

    try:
        statuses = api.GetUserTimeline(screen_name=screen_name, count=200, exclude_replies=True)
    except print(0):
        print('Error! \n Make sure the username is valid.')
        return

    try:
        n = len(statuses)
        all_statuses.extend([status.text for status in statuses])

        while n>1:
            oldest_id = statuses[-1].id
            n = len(statuses)
            statuses = api.GetUserTimeline(screen_name=screen_name, count=200,exclude_replies=True, max_id=oldest_id)
            all_statuses.extend([status.text for status in statuses])

            

        statuses = list(set(all_statuses))
        statuses = list(map(lambda status: status.replace('\n', ' '), statuses))
        statuses = list(map(lambda status: p.clean(status), statuses))
        statuses = list(map(lambda status: status.lower(), statuses))
        to_drop = string.punctuation
        to_drop = to_drop.replace('$', '').replace("'", '')
        for punct in to_drop:
            statuses = list(map(lambda status: status.replace(punct, ' '), statuses))        
        status_all = ' '.join(statuses)
        status_all = status_all.replace(" '", ' ')
        status_all = ' ' + status_all + ' '
        status_all = status_all.replace(' i ', ' I ')

        wordcloud = WordCloud(width = 800, height = 800, 
                        background_color ='white', 
                        min_font_size = 10).generate(status_all)

        #plot the WordCloud image                        
        plt.figure(figsize = (8, 8), facecolor = None) 
        plt.imshow(wordcloud) 
        plt.axis("off") 
        plt.tight_layout(pad = 0) 
        plt.savefig(file_name)
        print(f'Wordcloud of user {screen_name} saved in {file_name}')

    except:
        print("Error! \nMake sure everything's good.")



if __name__ == "__main__":
    main()