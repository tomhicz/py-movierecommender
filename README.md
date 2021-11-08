_(This was created during my time as a student at Code Chrysalis, during Polyglot week as a chance to learn about an entirely new language (Python))_

# Movie Recommender API

A basic movie recommender that will take a movie name and recommend movies that similar users like.

Built in Python 3 using the Flask Framework and Pandas library.

[https://film-recs.herokuapp.com/movies?name=Star%20Wars](https://film-recs.herokuapp.com/movies?name=Star%20Wars)

## How to use

The API currently has one endpoint at `https://film-recs.herokuapp.com/movies`
This endpoint takes a query string with a key of 'name' and a value of the seed movie name.
The endpoint returns a json object containing up to 10 movies with their name and confidence of a match.
(**Note:** This API may change in the future)

## How to edit locally

- Install python.
- Fork and clone this reqpository.
- Create a virtual environemnt. (venv)
  `python3 -m venv .venv`
- Install dependencies
  `pip install -r requirements.txt`

## How to deploy to heroku

- Install heroku cli
- From the directory use `heroku create` to create a new heroku app
- Commit changes to git
- Use `git push heroku main` to upload the app

## Notes:

- If you install additional libraries, you can use the following command to create a new requirements.txt: `pip freeze > requirements.txt`
  (Note: you may need to edit this file if a bug on some versions causes `pkg-resources==0.0.0` to be added, as heroku will choke on this. Just delete or comment out that line. )
