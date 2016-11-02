# simple-autocorrector
## simpleGuessing()

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

## advancedGuessing()
## Purpose
Better guessing.  Works by looking for substring similarities rather than just bunching letters together.
simpleGuessing could correct   teh -> the
advancedGuessing could correct ppl -> apple

## Example

**Input: pple**
```
Name:  pple
dragonfruit has confidence.........  0
tomato has confidence.........  0
grape has confidence.........  1
apple has confidence.........  3
peach has confidence.........  1
strawberry has confidence.........  0
pomegranate has confidence.........  1
blackberr has confidence.........  1
pear has confidence.........  1
blueberry has confidence.........  1
orange has confidence.........  0
mango has confidence.........  0
cantelope has confidence.........  1
banana has confidence.........  0


I believe you meant:   apple
```

 
This is where advancedGuessing surpassing simpleGuessing: I'll add my own fruit called 'wlackberry' to the list at the top.  Because 'strawberry' and 'wlackberry' have the same confidence, the choice closest to the top is selected
```
Name:  wberry
wlackberry has confidence.........  6
dragonfruit has confidence.........  2
tomato has confidence.........  0
grape has confidence.........  1
apple has confidence.........  1
peach has confidence.........  1
strawberry has confidence.........  6
pomegranate has confidence.........  3
blackberr has confidence.........  4
pear has confidence.........  3
blueberry has confidence.........  5
orange has confidence.........  2
mango has confidence.........  0
cantelope has confidence.........  1
banana has confidence.........  0


I believe you meant:   wlackberry
```

Whereas the advancedGuessing() spits out...
```
Name:  wberry
wlackberry has confidence.........  3
dragonfruit has confidence.........  0
tomato has confidence.........  0
grape has confidence.........  0
apple has confidence.........  0
peach has confidence.........  0
strawberry has confidence.........  5
pomegranate has confidence.........  0
blackberr has confidence.........  3
pear has confidence.........  0
blueberry has confidence.........  4
orange has confidence.........  0
mango has confidence.........  0
cantelope has confidence.........  0
banana has confidence.........  0


I believe you meant:   strawberry
```

because 'wberry' is a substring of strawberry, while only 'berry' is a substring of blackberry (I swear it's typed right in the file), blueberry, and wlackberry.