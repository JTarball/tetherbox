20/10/11 - TODO: unit tests, notes, documentation
10/11/11 - After some thought - I have decid to just implementation a basic redis search with logging of queries. 
           Without more information producing an algorithm might be pointless
10/11/11 - TODO: unit tests, notes, documentation and profiling

decorator.py - decorator for easy adding of content models
models.py - defines the groups (keywords and semantic groups)



'Basic Redis Search'
----------------------------------
 - add decorator (defined in decorator.py) to add indexing from content app (must be django model obviously)
 - django model must define what you want to index and the url e.g. ('title', 'body', url="slug")  # the only kwargs must be url 
 - decorator finally calls function addIndex from utils.py 
 - information is now indexed 
 - returns top 10 results
 
 
 -- use as template tag   {% load redis_tags %} {% search link %}
 
 'Profiling'
 -----------------------------------
- got fixtures and models in models.py






























""""
20/10/11
**cdjcjscjd**

How the REDIS Search Algorithm Works:
-------------------------------------------------------------------------------
 The idea of this search is to be real-time and to use only 
 (uses)(titles)(categories)


 	- Does this keyword match or semantic group
		YES
			DO SOME algorithm
		NO
			autocomplete algorithm
			
			
			
			
			
DO SOME algorithm:
	look for keywords
	e.g. yield   --- 
	
	
There are a number of groups: - predefined
"categories"
"keywords"
"sentences"
"uses"
"computer science words"
"semantic groups"  # e.g. [multithread thread threading] [yield generate]
	

Everytime some enters a query saved for future analysis



-------------------------------------------------------------------------------
'How is a content model Indexed?'
-------------------------------------------------------------------------------
when redis indexs 
url




-------------------------------------------------------------------------------
'Algorithm'
-------------------------------------------------------------------------------
log start time
for words in query:
    1. 'Check groups - Is the word present' 
        'CHECK: KEYWORDS'
            if yes : all urls relating to keyword add or +1 in weighting
            if no continue
        'CHECK: CATEGORIES'
            if yes : all urls relating to keyword add or +1 in weighting
            if no continue
        'CHECK USES'
            if yes : all urls relating to keyword add or +1 in weighting
            if no continue
        'CHECK COMPUTER SCIENCE WORDS'
            if yes : all urls relating to keyword add or +1 in weighting
            if no continue                
        'CHECK: SENTENCES'
            if yes : all urls relating to keyword add or +1 in weighting
            if no continue
        'CHECK SEMANTIC GROUPS'
            if yes: all urls relating to keyword add or +1 in weighting
            if no continue
        if no: goto Step 2
    2. 'autocomplete word
       goto Step 1
top 10 results using urls weighting as a sorting 
log end time
log query, results and time to stats 

-------------------------------------------------------------------------------
'REDIS part of the Algorithm'
-------------------------------------------------------------------------------
- 'for models in content: use this decorator'
@Redis_Search('title', 'uses')

- 'for keyword'
@Redis_Search('name', )


 in redis:
a number of different structures are used:
'set' : unique + not ranked
'z set' : unique + ranked (sorted set) 

for ZSETS:
key is 'tmpurl' -- for get best results       'tmpurl' :   '<model>:<id>'    e.g. Post:4
key is ZKEY_AUTOCOMPLETE - defined in utils.py    -- for autcompleting  (need to read doc for popularity thingy)
for SETS:
key is <SKEY_DOCS_PREFIX + phrase> -- for autcomplete   '<SKEY_DOCS_PREFIX + phrase>' :'<model>:<id>'
key is 'keywords:<id>'  :  <word> <word> ......      where id is the id of the keyword group e.g. 1 == computer science kwyword group
key is 'keyword:<word>' : <model>:<id> <model>:<id> ..............


'three scenarios to think about':
- 'adding keywords' 
- 'adding models'
- 'autocompleting - popularity of words'
- 'add urls weighting for keywords'







