# What Did I Do

I used the MediaWiki API to access the Slay The Spire Fandom Wiki. Slay the Spire is a video game that has achievements. Achievements are unlocked through doing specific actions in a game. I used the MediaWiki API to give me a list of the achievements that belong to this game. 

I then went on to use the Steam Web API to acquire the achievements belong to Slay the Spire again. This was a question of mine to see if there was consitency between APIs. Along with that, Slay the Spire has reached other devices other than PCs. With each release of Slay the Spire, achievements are relocalized, renamed, and possibly new ones are added. There was an interesting point to see what there was to find.

In the end, I compiled **achievement_data.csv**, which has three fields. Steam API Achievements, MediaWiki API Achievements, and Query Boolean. The first two fields speak for themselves, they are fields that represent the data I pulled from either API. The query boolean column is a boolean, true or false, on whether the achievement is consistent with the other API. In some cases, the achievement does exist with the same name. However, there are times where the formatting of how either API wrote their names resulted in mismatches and lost information. An example that comes to mind is "emerald_+" versus "emerald_plus". 

# The Comparison

I worked with the MediaWiki API and the [Steam Web API](https://developer.valvesoftware.com/wiki/Steam_Web_API). The MediaWiki API does not require a key or account. 
Steam Web only requires an API key if you want to use some methods. Typically, if a method let you get information
about users, you would need an API key. For my purposes, the public methods were enough for my analysis. Steam's API 
is very generous with letting users call the API 100,000 calls a day. The terms of service is large and does express
a lot of concern over safety. Steam is a large company that deals with a lot of users, companies, and money. Steam seems
to expect companies to be most likely to use their API and provides a large rate limit so as to help companies with 
data collection. 

The MediaWiki website I was using, the [Slay The Spire Fandom Wiki](https://slay-the-spire.fandom.com/api.php), has a limit of 5,000 calls. Comparing this to Steam, the MediaWiki seems to be expecting less use than other APIs. Granted, Steam is a multi-billion dollar company that can provide that service much easier than others. MediaWiki is also generally generous like Steam. MediaWiki notes that you should include a user-agent and to be reasonable with the queries. Which means that they want users to run their queries in series rather than in parallel. They might not have the hardware to handle such intense amounts of requests.

The data from both APIs were clean JSON. Though, the MediaWiki API required parsing to get to the information I was interested in compared to the Steam API that was intuitive to get information I wanted. 

In regards to concerns about information going missing, I would think both of these services are likely to last for a long while. The MediaWiki API is an open source API that is maintained by a non-profit, Wikimedia Foundation. Steam is a little more concerning though. Steam has been known as a relatively pro-consumer company. As a private company, they do not have the whims of shareholders to follow. However, if executives change, who is to say that their APIs will be walled off like the internet surrounding it. I would have to resort to manual collection of data, which would not be terribly difficult because of the scale we are working with, but it would still be unfortunate. 

As previously mentioned, there is mismatch in data being saved between MediaWiki and Steam Web's API. Steam is the first place that Slay the Spire appeared. As a result, Steam has more information about these achievements in regards to its own platform. As Slay the Spire was released on other devices, there are more achievements that belong to the game rather than just Steam. In regards to achievements, the open source wiki, has more information pertaining to Slay the Spire. 