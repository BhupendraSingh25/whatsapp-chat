import pandas as pd
from urlextract import URLExtract
from collections import Counter
import emoji

def dataframe(selected_user,df):
    if selected_user!='overall':
        df=df[df['user']==selected_user]

    return df

def fetch_stats(selected_user,df):
    if selected_user!='overall:'
        df=df[df['user']==selected_user]



    num_message=df.shape[0]


    words=[]
    links=[]
    for i in df['msgs']:
        words.extend(i.split())
        extract=URLExtract()
        links.extend(extract.find_urls(i))

    num_media=df[df['msgs']=='<Media omitted>\n'].shape[0]

    return num_messages, len(words), num_media, len(links)

def monthly_timeline(selected_user, df):
    if selected_user!= 'overall':
        df=df[df['user']==selected_user]


    timeline_df= df.groupby(['year', 'month_num', 'mont']).count()['msgs'].reset_index()

    time=[]
    for i in range(timeline_df.shape[0]):
        time.append(timeline_df['month'][i]+"-"+ str(timeline_df['year'][i]))


    timeline_df['time']= time

    return timeline_df

def daily_timeline(selected_user, df):
    if selected_user!= 'overall':
        df=df[df['user']==selected_user]

    daily_timeline_df= df.groupby(['date']).count()['msgs'].reset_index()


    return daily_timeline_df

def weekly_activity(selected_user, df):
    if selected_user!= 'overall':
        df=df[df['user']==selected_user]


    return df['day_name'].value_counts()

def month_activity(selected_user, df):
    if selected_user!= 'overall':
        df=df[df['user']==selected_user]

    return df['month'].value_counts()





def most_busy_user(df):
    x= df['user'].value_counts().head()
    df= round((df['user'].value_counts()/df.shape[0])*100, 2).reset_index().rename(columns={'index': 'name', 'user': 'percent'})
    return x, df


def most_common_words(selected_user,df):
    if selected_user!= 'overall':
        df=df[df['user']==selected_user]

    temp= df[df['user']!='group_notification']
    temp= temp[temp['msgs']!= '<Media omitted>\n']

    words=[]
    for message in df['msgs']:
        for word in message.lower().split():
            words.append(word)

    common_df= pd.DataFrame(Counter(words).most_common(10))

    return common_df

def show_emoji(selected_user, df):
    if selected_user!= 'overall':
        df=df[df['user']==selected_user]

    emojis=[]
    for message in df['msgs']:
        # emoji=emojis.get('message')
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
        # emojis1=emojis.unique()
        # emojis2= emojis.count()            

