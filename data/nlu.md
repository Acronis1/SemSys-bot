## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:query_knowledge_base
- I am [hungry](object_type:restaurant), I want to eat something, what can you recommend?
- what [restaurants](object_type:restaurant) can you recommend?
- I am [hungry](object_type:restaurant), I want to eat.
- I am [starving](object_type:restaurant), feed me.
- I am [hungry](object_type:restaurant) for some [austrian](cuisine:traditional) food.
- list some [restaurants](object_type:restaurant)
- can you name some [restaurants](object_type:restaurant) please?
- can you show me some [restaurant](object_type:restaurant) options
- list [austrian](cuisine:traditional) [restaurants](object_type:restaurant)
- do you have any [modern](cuisine) [restaurants](object_type:restaurant)?
- do you know the [price](attribute:price) range of [that one](mention)?
- Does the [first one](mention:1) have [outside seating](attribute:outside-seating)?
- what is the [price](attribute:price) range of the [second one](mention:2)?
- what is the [price](attribute:price) range of the [second one](mention:2)?
- what [cuisine](attribute) is [it](mention)?
- How many Michelin [stars](attribute:stars) does [it](mention) have?
- what is [its](mention) Michelin [rating](attribute:stars)?
- does [it](mention) have any Michelin [star](attribute:stars)?
- do you know what [cuisine](attribute) the [last one](mention:LAST) has?
- does [Donath](restaurant) have [outside seating](attribute:outside-seating)?
- what is the [price range](attribute:price) of [Berlin Burrito Company](restaurant)?
- what is the [price](attribute:price) range of [Berlin Burrito Company](restaurant)?
- what is with [Anna Sacher](restaurant)?
- Do you also have any [Vietnamese](cuisine) [restaurants](object_type:restaurant)?
- What about any [Mexican](cuisine) [restaurants](object_type:restaurant)?
- What about any [traditional](cuisine) [restaurants](object_type:restaurant)?
- Do you also know some [Italian](cuisine) [restaurants](object_type:restaurant)?
- can you tell me the [price range](attribute:price) of [that restaurant](mention)?
- what [cuisine](attribute) do [they](mention) have?
- can you send me the [url](attribute:url) for [that](mention)?
- can you send me the [website](attribute:url) for [that](mention)?
- send me the [url](attribute:url) for [Anna Sacher](restaurant)
- can you send me the [location](attribute:address) for [that](mention)?
- can you send me the [location](attribute:address) for [that](mention)?
- send me the [location](attribute:address) for [Anna Sacher](restaurant)?
- can you send me the [address](attribute:address) for [that](mention)?
- can you send me the [address](attribute:address) for [that](mention)?
- send me the [address](attribute:address) for [Anna Sacher](restaurant)?

- what [hotels](object_type:hotel) can you recommend?
- please list some [hotels](object_type:hotel) in [Frankfurt am Main](city) for me
- what [hotels](object_type:hotel) do you know in [Berlin](city)?
- name some [hotels](object_type:hotel) in [Berlin](city)
- show me some [hotels](object_type:hotel)
- what are [hotels](object_type:hotel) in [Berlin](city)
- does the [last](mention:LAST) one offer [breakfast](attribute:breakfast-included)?
- does the [second one](mention:2) [include breakfast](breakfast-included)?
- what is the [price range](attribute:price-range) of the [second](mention:2) hotel?
- does the [first](mention:1) one has [wifi](attribute:free-wifi)?
- does the [third](mention:3) one has a [swimming pool](attribute:swimming-pool)?
- what is the [star rating](attribute:star-rating) of [Berlin Wall Hostel](hotel)?
- Does the [Hilton](hotel) has a [swimming pool](attribute:swimming-pool)?


## lookup:restaurant
- Donath
- Berlin Burrito Company
- I due forni
- Lụa Restaurant
- Pfefferberg
- Marubi Ramen
- Gong Gan

## lookup:hotel
- Hilton
- B&B
- Berlin Wall Hostel
- City Hotel
- Jugendherberge
- Berlin Hotel

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:capabilities
- what can you do?
- what are your capabilities?
- what are you used for?
- what do you do?
- what should I do with you?

## intent:thanks
- thank you
- thanks
- danki
- danke
- it was a pleasure
- thank you very much
- thank you
- that was helpful
- very helpful, thank you