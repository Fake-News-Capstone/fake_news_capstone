# Fake News Capstone

What is our goal?
- Our team seeks to differentiate fake news from real news through the exploration and analysis of keywords and phrases of random news articles. We will utilize NLP tools and build a classification model in hopes to shed light on purposely misleading information.

# <a name="top"></a> Fake News Capstone - README.md
![Fake News](Photos/fof.jpg)
***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Acquire & Prep](#acquire_and_prep)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___
​
## <a name="project_description"></a>Project Description:
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Description
- Within this project we will be using the fake news dataset acquired from the Kaggle database.
- We will clean the data through tokenizing, lemmatizing, vectorizing, and removing stop words.
- Then we will explore the data through bigrams and trigrams, while also generating word clouds. 
- Lastly we will make a model that can accurately identify fake news articles.

### Goals
- Create a classification model that can accurately identify fake news and real news articles while utilizing NLP tools like NLTK, Sentiment Analysis, and TF-IDF Vectorizer in addition to the standard data science tools.
- Our secondary goal is to create a public web application that can be used to identify fake news.
- After acquiring our MVP, we would like to create a deep learning model.

### Where did you get the data?
- We acquired the data from the Kaggle online database.

### Data Contents:
- 20,826 unqiue Real articles
- 17,903 unique Fake articles
- 38,729 total unique articles
- Title of article
- Text of article
- Subject of article
- Date of when the article was posted.

### Link to data: 
https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset?select=Fake.csv

</details>

    
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

### Projet Outline:
    
- Acquisition of data through Kaggles online database.

- Prepare and clean data with python/NLP tools - Jupyter Labs
    - Tokenize
    - Lemmatize
    - Remove stop words
    - Vectorize

- Explore data
    - Identify top 10 words in fake news and real news articales.
    - Compare the proportion of words that show up in fake news vs real news.
    - Generate bigrams and trigrams to visualize two to three word sequences and their relationships to fake or real news.
    - Generate single word, bigram, trigram, word clouds to vizualize reiterations for specific words and word sequences.
    - Calculate TF, IDF, TF-IDF.
    - Create a final explore.py with helper fucntions

- Feature Engineering (after MVP)
    - Use sentiment anaylis to add extra features to second iteration model.
    - Add more features based on findings in exploration.

- Modeling
    - Establish baseline
    - Evaluate training data on each calssifcation model type
    - Select MVP model
    - Create final model.py with helper functions

- Presentation
    - Finalize README
    - Create story board
    - Write script
    - Create MVP presentation
    - Practice presentation
    - Record
        
### Hypothesis
- Fake news articles are more prone to be polarized and subjective.

### Target variable
- is_fake (If the news article is fake news)

</details>

    
## <a name="findings"></a>Key Findings:
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Explore:
- Findings:

### Statistics:
- Findings: 

### Modeling:
- Findings:

***
</details>

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Data Used
    
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| title  |  The title of the article | string |     
| text |  The text of the article | string |    
| subject | The subject of the article | string |
| date | The date at which the article was posted | string |
  
|target|
| is_fake | If the news article is fake news | boolean |


</details>

## <a name="wrangle"></a>Wrangle:
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Wrangle.py:
- Gather fake news dataset from Kaggle online database.

| Function Name | Purpose |
| ----- | ----- |
|  |  |


### Prepare Data
- To clean the data we had to:
    - 
    - 
    - 

- From here we :
    - 
    - 
    - 

| Function Name | Purpose |
| ----- | ----- |
|  |  |
​
***
    
</details>

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Findings:
- 

### Explore.py 
| Function Name | Definition |
| ------------ | ------------- |
|  |  |


### Function1 used:
- Outcome of the use of the function 
​
### Function2 used:
- Outcome of the use of the function 
​
***

</details>    

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

### Stats

- Stat Test 1: 
    - **T-Testing**:
        - HO: 
        - HA:
        - t-stat: 
        - p-value:
        - Result:

- Stat Test 2: 
    - **Test Type**:
        - HO: 
        - HA:
        - t-stat: 
        - p-value:
        - Result:
  

## <a name="model"></a>Modeling:
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

Summary of modeling choices...
        
### Models
- Will run the following models:
    - 
    -
    -


### Baseline Model

Training/In-Sample:

Validation/Out-of-Sample: 



### Model 1
    
Training/In-Sample: 
    
Validation/Out-of-Sample: 
    

    
### Model 2
    
Training/In-Sample:  
    
Validation/Out-of-Sample: 
    

    
### Model 3
    
Training/In-Sample: 
    
Validation/Out-of-Sample: 
    

    
### Model 4
    
Training/In-Sample: 
    
Validation/Out-of-Sample: 



### Model.py 
| Function Name | Definition |
| ------------ | ------------- |
|  |  |


### Use Table below as a template for all Modeling results for easy comparison:

| Model | Training/In Sample | Validation/Out of Sample | R<sup>2</sup> Value |
| ---- | ----| ---- | ---- |
|  |   |  |  |
|  |   |  |  |
|  |   |  |  |
|  |   |  |  |
|  |   |  |  |
|  |   |  |  |

## Best Model:
- 

- Why did you choose this model?
    - 

## Testing the Model

- Model Test Results
     - Performance: 


***

</details>  

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>



    

</details>  

>>>>>>>>>>>>>>>
