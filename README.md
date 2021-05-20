# fake_news_capstone

What are the goals?
- Create a classification model that can accurately identify fake news and not-fake news articles while utilizing NLP tools like NLTK, Sentiment Analysis, and TF-IDF Vectorizer in addition to the standard data science tools.
- Our secondary goal is to create a public web application that can be used to identify fake and not fake news.
- After acquiring our MVP, we would like to create a deep learning model.

# Fake News Capstone

# <a name="top"></a>Fact or Fiction - README.md
![Zillow Logo](Users/liamjackson/Desktop/Fake News Capstone/fof.jpg)
​
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
- Our team seeks to differentiate fake news from real news through the exploration and analysis of keywords and phrases of random news articles. We will utilize NLP tools and build a classification model in hopes to shed light on purposely misleading information. 

### Goals
- What are the goals?
    - Create a classification model that can accurately identify fake news and not-fake news articles while utilizing NLP tools like NLTK, Sentiment Analysis, and TF-IDF Vectorizer in addition to the standard data science tools.
    - Our secondary goal is to create a public web application that can be used to identify fake and not fake news.
    - After acquiring our MVP, we would like to create a deep learning model.

### Where did you get the data?
- We acquired the data from the Kaggle online database.

### Data Contents:
- 20,826 unqiue Real articals
- 17,903 unique Fake articals
- 38,729 total unique articals
- Title of artical
- Text of artical
- Subject of artical
- Date of when the artical was posted.

### Link to data: 
https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset?select=Fake.csv

</details>
    
    
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

### Projet Outline:
    
- Acquisiton of data through Kaggles online database.

- Prepare and clean data with python/NLP tools - Jupyter Labs
    - Tokenize
    - Lemmatize
    - Remove stop words

- Explore data
    - Identfy top 10 words in fake news and non-fake news articales.
    - Comapre the propation of words that show up in fake news vs real news.
    - Generate bigrams and trigrams to vizualize two to three word sequences and their relationships to fake or real news.
    - Generate single word, bigram, trigram, word clouds to vizualize reiterations for specifc words and word sequences.
    - Calcaute TF, IDF, TF-IDF.
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
- Fake news articals are more prone to have politically driven words such as:
    -

### Target variable
- is_fake (If the news article is fake news)

</details>

    
## <a name="findings"></a>Key Findings:
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Explore:
- Findings:

### Stats
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
| title  |  The title of the artical | string |     
| text |  The text of the artical | string |    
| subject | The subject of the artical | string |
| date | The date at which the artical was posted | string |
| is_fake | If the news article is fake news | string |

***
</details>

## <a name="acquire_and_prep"></a>Acquire & Prep:
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Acquire Data:
- Gather data from Kaggle online database.

### Acquire.py 
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

### Wrangle.py 
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

## <a name="model"></a>Modeling:
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

Summary of modeling choices...

### Baseline

- Baseline Results: 
    - Median In sample = 0.16
    - Median Out of sample = 0.15
        
### Models and R<sup>2</sup> Values:
- Will run the following models:
    - 
    -
    -


### Baseline Model

Training/In-Sample:

Validation/Out-of-Sample: 



### Model 1
    
Training/In-Sample:  0.012348907010552293 
    
Validation/Out-of-Sample:  0.011532822479710627
    

    
### Model 2
    
Training/In-Sample:  0.01234045919349956 
    
Validation/Out-of-Sample:  0.011536767590909373
    

    
### Model 3
    
Training/In-Sample:  0.012288891953326782 
    
Validation/Out-of-Sample:  0.011543443686491118
    

    
### Model 4
    
Training/In-Sample:  0.012288891953326782 
    
Validation/Out-of-Sample:  0.011543443686491118



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
     - Out-of-Sample Performance:  0.1518694361646674


***

</details>  

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>



    

</details>  

![Folder Contents]()


>>>>>>>>>>>>>>>
.
