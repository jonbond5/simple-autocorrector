# simple-autocorrector
## Purpose
This is a Python script that takes a list of words and attempts to guess what you meant.  
It is meant for small lists (less than 50 or so) that contain decently diversified words.  The more similar words you have (e.g.: there/here, you/your, place/lace, etc.) the less accurate this corrector becomes.

## Why should you care
It's **plenty fast** and requires NO imports.  Not because I'm some algorithmic genius, but because it takes a straightforward, simple approach to a simple problem (somewhat).  There are no neural nets or deep machine learning involved here (yet).  If you're trying to build Google SE better than Google, you're in the wrong repo, man.

*Note: originally this script was used to autocorrect names, which is why the syntax uses variable names like 'prof' and 'list_of_people'.  For privacy reasons, the original list was changed to fruits (though let's be honest, a banana can be an awesome professor).*



## Examples
### These examples are for the **simpleCorrector** function.  The **advancedCorrector** hasn't been built yet.

**Input = grape**
```cmd
Input:  grape
The name dragonfruit has a confidence of....3
The name tomato has a confidence of....1
The name grape has a confidence of....5
The name apple has a confidence of....3
The name peach has a confidence of....3
The name strawberry has a confidence of....3
The name pomegranate has a confidence of....5
The name blackberr has a confidence of....3
The name pear has a confidence of....4
The name blueberry has a confidence of....2
The name orange has a confidence of....4
The name mango has a confidence of....2
The name cantelope has a confidence of....3
The name banana has a confidence of....1


I believe you meant:
grape
Input:
```

Cool, it works.  That was the 'no shit test'; basically if that failed...yeah.


**dragonfruit without the 'd'**
```cmd
Input:  ragonfruit
The name dragonfruit has a confidence of....10
The name tomato has a confidence of....3
The name grape has a confidence of....4
The name apple has a confidence of....1
The name peach has a confidence of....1
The name strawberry has a confidence of....4
The name pomegranate has a confidence of....7
The name blackberr has a confidence of....3
The name pear has a confidence of....3
The name blueberry has a confidence of....3
The name orange has a confidence of....6
The name mango has a confidence of....4
The name cantelope has a confidence of....4
The name banana has a confidence of....2


I believe you meant:
dragonfruit
```

**blueberry forgetting to type straw**
```cmd
Input:  berry
The name dragonfruit has a confidence of....2
The name tomato has a confidence of....0
The name grape has a confidence of....3
The name apple has a confidence of....1
The name peach has a confidence of....1
The name strawberry has a confidence of....5
The name pomegranate has a confidence of....3
The name blackberr has a confidence of....4
The name pear has a confidence of....3
The name blueberry has a confidence of....5
The name orange has a confidence of....3
The name mango has a confidence of....0
The name cantelope has a confidence of....1
The name banana has a confidence of....1


I believe you meant:
strawberry
```

There's my point about the well-diversified list.  Using the simpleCorrector, the output just spits out the first item it finds that matches the criteria.


**pear, but without the r
```cmd
Input:  pea
The name dragonfruit has a confidence of....1
The name tomato has a confidence of....1
The name grape has a confidence of....3
The name apple has a confidence of....3
The name peach has a confidence of....3
The name strawberry has a confidence of....2
The name pomegranate has a confidence of....3
The name blackberr has a confidence of....2
The name pear has a confidence of....3
The name blueberry has a confidence of....1
The name orange has a confidence of....2
The name mango has a confidence of....1
The name cantelope has a confidence of....3
The name banana has a confidence of....1


I believe you meant:
grape
```

However, notice how about half the list has the same confidence.  Exhibit B for why simpleCorrector needs a diverse list.

