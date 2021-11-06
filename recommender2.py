import numpy as np
import pandas as pd

def recommender2(movieName):
  #function to convert types when importing
  def convert_dtype(x):
      if not x:
          return ''
      try:
          return str(x)   
      except:        
          return ''

  #import movie data from csv files 
  mdata = pd.read_csv("data2/movies_metadata.csv", converters={'popularity': convert_dtype})
  mdata= mdata[['id', 'original_title', 'original_language', 'poster_path', 'vote_count']]
  mdata= mdata.rename(columns={'id':'movieId'})
  print(mdata.shape)
  mdata = mdata[mdata['original_language']== 'en'] #just want movies in English
  print(mdata.shape)
  mdata = mdata[mdata['vote_count'] > 5] #just want movies with a decent number of votes
  print(mdata.shape)

  #importing movie ratings from small file
  ratings= pd.read_csv("data2/ratings_small.csv")
  #ALTERNATIVELY, import movie ratings from LARGE file
  #ratings= pd.read_csv("data2/ratings.csv")


  ratings= ratings[['userId', 'movieId', 'rating']]
  # FOR LARGE FILE taking a 1MM sample because it can take too long to pivot data later on
  #ratings=ratings.head(1000000)
  print(ratings.head())
  print(ratings.shape)

  #convert data types before merging to avoid errors
  mdata.movieId =pd.to_numeric(mdata.movieId, errors='coerce')
  ratings.movieId = pd.to_numeric(ratings.movieId, errors= 'coerce')

  #merge the two datasets into one
  data= pd.merge(ratings, mdata, on='movieId', how='inner')
  #print(data.head(10))
  print('data:',data.shape)

  #create a movie matrix of users against movie titles to use for the recommender
  matrix=data.pivot_table(index='userId', columns='original_title', values='rating')
  print(matrix.head())
  print('matrix:',matrix.shape)

  ## DATA ANALYSIS FUNCTIONS TAKEN FROM https://www.kaggle.com/flaviobossolan/simple-efficient-movie-recommender/notebook
  # A simple way to compute Pearson Correlation 
  def pearsonR(s1, s2):
      s1_c = s1-s1.mean()
      s2_c= s2-s2.mean()
      return np.sum(s1_c*s2_c) / np.sqrt(np.sum(s1_c**2)* np.sum(s2_c**2))

  # A function to make N recommendations based on Pearson Correlation.
  # The parameters here are: movie name, matrix name and number of recommendations.
  def recommend(movie, M, n):
      reviews=[]
      for title in M.columns:
          if title == movie:
              continue
          cor= pearsonR(M[movie], M[title])
          if np.isnan(cor):
              continue
          else:
              reviews.append({'title':title, 'cor':cor})
              
      reviews.sort(key= lambda tup: tup['cor'], reverse=True)
      return reviews[:n]

  # List with movies I have watched:
  # watched = ['Jarhead', 'Die Hard', 'Donnie Darko', 'Frida', 'Men in Black II' ]
  # print(matrix['The Empire Strikes Back'].isna().sum() )
  #recs = recommend('Star Wars', matrix, 10)
  try:
    recs = recommend(movieName, matrix, 10)
    print('length',len(recs))
    if (len(recs) > 0):
      recsSeries = pd.Series(recs).to_json() 
      print(recsSeries)
      return recsSeries
    else:
      return f'Sorry, no recommendations found for {movieName}'
  except KeyError: 
    return f'Sorry, movie {movieName} not found'
