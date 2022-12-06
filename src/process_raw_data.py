import pandas as pd
from tqdm import tqdm


RAW_DATA_FOLDER = '../data/raw/'
PROCESSED_DATA_FOLDER = '../data/processed/'


def parse_ratings(path):
    
    ratings_file = open(path)
    
    rating, ratings = {}, []
    review, reviews = {}, []
    features = ['beer_id', 'user_id', 'date', 'appearance', 'aroma', 'palate', 'taste', 'overall', 'rating']
    
    if path.split('/')[-2] == 'BeerAdvocate':
        nb_lines = 151074576
    
    elif path.split('/')[-2] == 'RateBeer':
        nb_lines = 121075258
    
    for line in tqdm(ratings_file, desc="    -Parsing ratings.txt file ", total=nb_lines, unit=' lines'):
        if line == '\n':            
            ratings.append(rating)
            rating = {}
            
            if bool(review):
                reviews.append(review)
                review = {}
            continue
        
        key, val = line.split(':', maxsplit=1)
        
        if (key in features):
            rating[key] = val[1:-1]
            continue
        
        if key == 'text':
            rating['review'] = True
            review['beer_id'] = rating['beer_id']
            review['user_id'] = rating['user_id']
            review['date'] = rating['date']
            review[key] = val[1:-1]
            continue
        
        if (key == 'review') and (val[1:-1] == 'False'):
            rating['review'] = False
            review = {}
    
    print('    -Converting to dataframe ...')
    return pd.DataFrame(ratings), pd.DataFrame(reviews)


def change_dtype(ratings, reviews):
    print('    -Changing dtypes ...')
    ratings['beer_id'] = ratings['beer_id'].astype(int)
    ratings['date'] = ratings['date'].astype(int)
    ratings['date'] = pd.to_datetime(ratings.date, unit='s')
    
    ratings['appearance'] = ratings['appearance'].astype(float)
    ratings['aroma'] = ratings['aroma'].astype(float)
    ratings['palate'] = ratings['palate'].astype(float)
    ratings['taste'] = ratings['taste'].astype(float)
    ratings['overall'] = ratings['overall'].astype(float)
    ratings['rating'] = ratings['rating'].astype(float)

    reviews['beer_id'] = reviews['beer_id'].astype(int)
    reviews['date'] = reviews['date'].astype(int)
    reviews['date'] = pd.to_datetime(reviews.date, unit='s')
    
    return ratings, reviews


if __name__ == '__main__':
    for dataset in ['BeerAdvocate', 'RateBeer']:
        print('Processing {} dataset:'.format(dataset))
        ratings, reviews = parse_ratings(RAW_DATA_FOLDER + dataset + '/ratings.txt')
        ratings, reviews = change_dtype(ratings, reviews)
        
        print('    -Saving ratings and reviews to pickle file ...')
        ratings.to_pickle(PROCESSED_DATA_FOLDER + dataset + '/ratings.pkl')
        reviews.to_pickle(PROCESSED_DATA_FOLDER + dataset + '/reviews.pkl')
        del ratings, reviews
        
        print('    -Reading breweries.csv, users.csv and and beers.csv ...')
        breweries = pd.read_csv(RAW_DATA_FOLDER + dataset + '/breweries.csv')
        users = pd.read_csv(RAW_DATA_FOLDER + dataset + '/users.csv')
        beers = pd.read_csv(RAW_DATA_FOLDER + dataset + '/beers.csv', 
                            usecols=['beer_id', 'beer_name', 'brewery_id', 'style', 'avg', 'avg_computed'])
        
        print('    -Saving breweries, users and and beers to pickle file ...')
        breweries.to_pickle(PROCESSED_DATA_FOLDER + dataset + '/breweries.pkl')
        users.to_pickle(PROCESSED_DATA_FOLDER + dataset + '/users.pkl')
        beers.to_pickle(PROCESSED_DATA_FOLDER + dataset + '/beers.pkl')
        del breweries, users, beers