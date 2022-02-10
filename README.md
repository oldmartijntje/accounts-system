# accounts-system

This is my accounts System. You can use it in your programs to use as save file. and you can open the files in other apps too. so you can use cosmetics or other files in your apps, for example. you bought a crown in 1 game, you can then use that crown in another app too, since it's linked.

How to use?
Its mostly explained in the comments, every account has the same structure, here are the versions:

old variant: [name,[time],{appDictionary},encryption number1,encryption number2,[data with lock],[data with lock],[data with lock]]
new variant: [name,[time],{appDictionary},encryption number1,encryption number2,[data with lock],[data with lock],[data with lock]], {achievements}, {collectables}

the name and time speak for itself. 

appdictionary, every app has its own name, like 'exampleName'. that name is a key in the dictionary, that's where all your data is stored. if you know a specific games name, you can look at their data, you can copy theirs, but please don't edit data outside of your place.

encryption is for the data with lock, it consists of 1 thing, a coin amount. these are coins you can use to buy things with across games, the reason it's encrypted is because people who don't know what they are doing can't easely find out how it works, but it's bad encryption, + it won't keep anyone from making coin farms, but please, don't make coin farms

achievements work the same as the appdictionary, only add achievements in your own gamename. i would advise to store it like this:
[['achievement ID'],{'Achievement ID': 'Description','Name'}]
this way, in the first list you can put all the achievements a person has, the dictionary you can use to identify the achievements with a name and description. but you don't have to ofc

collectabbles are the same as achievements, but then with collectables, like outfits or items, i would personally use it like this: [['item ID'],{'item ID': 'Description','Name', 'costs', 'extra data needed'}] 
this way, everyone can look into your app and use your 'magical bow' in their game if they own it in your game. but ofcoarse, you can use it the way you want, here is another way to do it, with special stats:
[[['item ID','cosmetic rarity ID']],{'item ID': 'Description','Name', 'costs', 'extra data needed'},{'cosmetic rarity ID': 'Description','Name', 'costs multiplier', 'extra data needed'}] 
and ofc you can have items you can't buy. these are just examples of how i will use it.

if you use an old account, it wont have the achievements and collectables, but it will be added to it when u load one, so if you have an og account, make sure to not load it in a newer version than 1.0.0

Data, you don't need to use the coin system in your game, to make sure it's not easy to cheat a lot of coins into your game to buy cosmetics, because it ofc is a possabillity
