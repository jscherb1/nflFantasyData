import pandas as pd


def getFantasyFootballData(pos,year,weekNum,rulesFormat):
    #Translate the rules format into the value used by the URL    
    if rulesFormat.lower() == 'ppr':
        rulesVal = '2'
    elif rulesFormat.lower() == 'standard':
        rulesVal = '1'
    else:
        #error on the scoring format of the leage
        rulesVal = '-1'

    baseUrl = 'https://www.footballdb.com/fantasy-football/index.html'
    url = baseUrl +'?pos='+pos \
                +'&yr='+year \
                +'&wk='+weekNum \
                +'&rules='+rulesVal \

    dfs = pd.read_html(url)

    df = dfs[0]
    
    
    #TODO: remove double headers and rename columns
    df.columns = df.columns.droplevel()
    columnNames = ['Player Name','Game','Fantasy Point','Passing - Att','Passing - Cmp','Passing - Yds'
                   ,'Passing - TD','Passing - Int','Passing - 2Pt'
                   ,'Rushing - Att','Rushing - Yds','Rushing - TD'
                   ,'Rushing - 2Pt','Receiving - Rec','Receiving - Yds'
                   ,'Receiving - TD','Receiving - 2Pt','Receiving - FL','Receiving - TD']
    df.columns = columnNames

    #add in some values to the results for analysis later.
    df['week'] =  weekNum
    df['year'] = year
    df['position'] = pos
    #TODO: calculate the points for each player based on league specific rules
    return df

positionArray = ['QB','RB','WR','TE']
rulesFormat = 'PPR'

#TODO: calculate these on the fly
yearArray = ['2019']
weekNum = ['1','2','3','4','5','6']

weeklyPositionResults = getFantasyFootballData(positionArray[0],yearArray[0],weekNum[0],rulesFormat)

print(weeklyPositionResults.head())