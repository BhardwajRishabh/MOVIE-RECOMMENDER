import pandas as pd
column_name=['user_id','item_id','rating','timestamp']
data=pd.read_csv("u.data",sep='\t',names=column_name)
data.head()
movies_title=pd.read_csv('Movie_Id_Titles')
movies_title.head()
# merging two dataframes
data=pd.merge(data,movies_title,on='item_id')
data.head()
# sorting 
data.groupby("title")['rating'].count().sort_values(ascending=False).head()
# Mean
data.groupby("title")['rating'].mean().sort_values(ascending=False).head()
ratings=pd.DataFrame(data.groupby("title")['rating'].mean().sort_values())
ratings["Rating_By"]=pd.DataFrame(data.groupby("title")['rating'].count())
ratings.head()
#pre processing the data
moviemat=data.pivot_table(index="user_id",columns='title',values='rating')
moviemat.head()
ratings.sort_values('Rating_By',ascending=False).head()
StarWar_user_rating=moviemat['Star Wars (1977)']
LiarLiar_user_rating=moviemat['Liar Liar (1997)']
similar_to_starwar=moviemat.corrwith(StarWar_user_rating)
similar_to_liarliar=moviemat.corrwith(LiarLiar_user_rating)
#for Star wars(1977) movie
corr_starwar=pd.DataFrame(similar_to_starwar,columns=["Correlation"])
corr_starwar.dropna(inplace=True)
corr_starwar.sort_values("Correlation",ascending=False).head()
corr_starwar=corr_starwar.join(ratings["Rating_By"])
corr_starwar[corr_starwar["Rating_By"]>100].sort_values("Correlation",ascending=False).head()
# for liar liar movie
corr_LiarLiar=pd.DataFrame(similar_to_liarliar,columns=["Correlation"])
corr_LiarLiar.dropna(inplace=True)
corr_LiarLiar=corr_LiarLiar.join(ratings['Rating_By'])
corr_LiarLiar[corr_LiarLiar["Rating_By"]>100].sort_values("Correlation",ascending=False).head()
#for contact (1997) movie
Contact_user_rating=moviemat['Contact (1997)']
similar_to_Contact=moviemat.corrwith(Contact_user_rating)
corr_Contact = pd.DataFrame(similar_to_Contact,columns=["Correlation"])
corr_Contact.dropna(inplace=True)
corr_Contact=corr_Contact.join(ratings["Rating_By"])
corr_Contact[corr_Contact["Rating_By"]>100].sort_values("Correlation",ascending=False).head()