# BeerVise: Pick the right beer for you!

## Table of Contents 
- [Abstract](#abstract)
- [Research questions](#research-questions)
- [Data](#data)
- [Methods](#methods)
- [Proposed timeline](#proposed-timeline)
- [Organization within the team](#organization-within-the-team)
- [Questions for TAs](#questions-for-tas)
- [Authors](#authors)

## 📝 Abstract 
Nowadays, drinking beer has become a global social habit, whether it be for parties, football games or meeting with friends. In order to answer this demand, the market has become very attractive and diverse with breweries all around the world producing a wide variety of beer styles. This wide range of offer makes it more difficult for costumers to find a style of beer they might like. Being aware of this issue and with the aim to improve their customers’ satisfaction, an international supermarket chain called upon our data scientists’ team to help better organize their beer shelves. Our strategy is to associate each row of the shelves to a customers’ type. Then, for each of these customers’ categories, the most appreciated styles of beers are promoted with a description of their main features. Besides, in order to satisfy the firms’ multidomestic strategy, the arrangement of the beer shelves is customized according to the local tastes and preferences and their evolution over time. 

## ❓ Research questions 
1. What are the main features of each beer style (e.g. abv, countries or breweries where they are produced…)? Can some beer styles be merged?
2. From the reviews, what are the adjectives that best describe each beer style?
3. Is the taste of a user influenced by his country of origin or his expertise? 
4. Is popularity of a beer style evolving with time? (In terms of consumption and appreciation)

## 💾 Data
For this project two dataset have been provided: data from [BeerAdvocate](https://www.beeradvocate.com) as well as from [RateBeer](https://www.ratebeer.com/) websites.
Both dataset are organized following the same relational model (see `ER_diagram.png` and `relations.png` in figures folder). The following analysis will be done on each dataset separately and the results will be compared at the end. Raw data are available [here](https://drive.google.com/drive/folders/1Wz6D2FM25ydFw_-41I9uTwG9uNsN4TCF).
Processed data are available [here](https://drive.switch.ch/index.php/s/QBPV4ptiUoV8XER). In order to reproduce the analysis a data folder with the following architecture should be placed in the root directory of the repository:

<pre>  
├─── data
    ├─── raw
      ├─── BeerAdvocate
        ├─── beers.csv
        ├─── breweries.csv
        ├─── ratings.txt
        ├─── reviews.txt
        ├─── users.csv
      ├─── RateBeer
        ├─── beers.csv
        ├─── breweries.csv
        ├─── ratings.txt
        ├─── reviews.txt
        ├─── users.csv
    ├─── processed
      ├─── BeerAdvocate
        ├─── beers.pkl
        ├─── breweries.pkl
        ├─── ratings.pkl
        ├─── reviews.pkl
        ├─── users.pkl
      ├─── RateBeer
        ├─── beers.pkl
        ├─── breweries.pkl
        ├─── ratings.pkl
        ├─── reviews.pkl
        ├─── users.pkl 
</pre>

If one wants to manually re-produced the processed data from the raw data, simply move to the `src` folder and execute:
    
    python process_raw_data.py

Make sure to have all the requirements and that the data in the raw data folder have been uncompressed. Be aware that running the script took around 20 min on Apple silicon M1 Pro. 

## 📊 Methods 

**Task 1**: Data cleaning and pre-processing.

**Task 2**: Descriptive statistical analysis of each beer style.

Some analyses are quite trivial and will not be detailed here. We will focus on the most interesting methods.

- What are the most common beer style? (based on number of ratings and reviews).
- Investigate if we can merge some style together. (ex: English pale ale vs American pale ale).
- What are the characteristics of each beer style (abv, location)
- What are the grades for each beer style?. (appearance, taste, palate, aroma)
- Analysis of beers style based on location.

**Task 3**: Textual analysis of the reviews.

To determine which adjectives best describe each style, we will carry out a lexical description based on the textual reviews. Either we choose the adjectives that occurred the most in the reviews, therefore we show the adjectives that have been used the most, or we try to find the adjectives closest to all other (taking number of occurrence into account). For the last option we will use NLP and word embedings.  

**Task4**: Categorization of the users based on their level of expertise and the type of beer customers they are.

Users with only a few reviews and ratings or that have only rated a specific type of beer are considered as « beginners ». On the other hand, users which have rated a lot of different beer styles are rather « experts ». Besides, users which have rated and tested a majority of beer coming from their homeland are rather « nationalist ». Some other categories might arise throughout our analysis and note that users can be associated to different categories.

**Task 5**: Analysis of the influence of user features based on their beer style preferences.

For this task we first use a Bayesian approach to estimate ratings given beer features (brewery, location, abv, beer style) and remove ratings which are too far from our prediction. We will then compute the average scores for each user category for each style and sort out the most liked ones

**Task 6**: Github-site building and data story redaction.
## ⏰ Proposed timeline 

| Period                 | Description               |
| ---------------------- | ------------------------- |
| 25.11.2022 - 02.11.2022      | Task 1 and 2|
| 02.11.2022 - 07.11.2022      | Task 3 and 4|
| 08.11.2022 - 16.12.2022      | Task 4 and 5|
| 17.12.2022 - 22.12.2022      | Task 6 |

## 🤝 Team Organization 
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Team member</th>
    <th class="tg-0pky">Tasks</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Lola Vegeas</td>
    <td class="tg-0pky">2 and 5</td>
  </tr>
  <tr>
    <td class="tg-0pky">Jean Decroux</td>
    <td class="tg-0pky">2 and 5</td>
  </tr>
  <tr>
    <td class="tg-0pky">Ramy Charfeddine</td>
    <td class="tg-0pky"> 4 and 6</td>
  </tr>
  <tr>
    <td class="tg-0pky">Tom Mery</td>
    <td class="tg-0pky">1 and 3</td>
  </tr>
</tbody>
</table>

## ❔ Questions for TAs 
Do you think it is a good idea (useful) to merge BeerAdvocate and RateBeer folder together? It seems to require a lot of work as some value will have to be recomputed over the merged dataset (averaged values), ids will have to be reset and changed over the files, also some attribute value are not the same in the two dataset for the same entity (for example nbr_beers in breweries). Finally, in the matched beer data folder, do you know how 'sim' and 'diff' values have been computed? We guess they are values representing difference and similarity, but we are not sure.

## Authors
- Lola Vegeas (lola.vegeas@epfl.ch)
- Jean Decroux (jean.decroux@epfl.ch)
- Ramy Charfeddine (ramy.charfeddine@epfl.ch)
- Tom Mery (tom.mery@epfl.ch)
