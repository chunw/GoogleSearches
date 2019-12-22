![1](https://github.com/chunw/GoogleSearches/blob/master/img/screen.png "1")

## Instructions to create your own Google Searches movie

First of all you need a copy of your Google Search entries...
and since Google doesn't provide such API, this data needs to be self-served a.k.a. hacked 🤷.

Here is how to scrape your Google searches from an infinitely scrolling web page...

0. Download this code repository.

1. Use Chrome to navigate to your Google My Activity page
(https://myactivity.google.com/item?min=1572580800000000&max=1573793999999999&product=19)
You’ll need to login to your Google account if haven't yet. Filter by a time range as you see fit.

2. Right-click on your Google My Activity page -> Inspect -> Console to bring up Chrome Dev console. Copy-paste-enter the code in `autoScroll.js` into the console - this kicks off automatic scrolling on the Google My Activity page. Wait until page bottom is reached.

3. Copy-paste-enter the code in `scrape.js` into the same Dev console to see your search entries.
Right-click in Dev console -> <em>Save as...</em>, and save it using this naming convention: `[play_order].[your_movie_clip_title].log`, starting from play_order = 1.

* <strong>NOTE 3.1 </strong> You could repeat Step 1-3 to generate as many `.log` files as you want, perhaps with different time range filters -- each one of them will be treated as a movie clip and combined into one single movie. In case of multiple clips, the clips will be played in the order as specified by their `play_order`. For example, I generated `1.January.log`, `2.February.log`, `3.March.log` etc. to play out my searches throughout the year in chronological order, with appropriate titles.

* <strong>NOTE 3.2 </strong> Oh and don't forget, before you save the logs from Dev console, make sure you <em>scroll all the way up to the very top of these logs in the console</em>. Without this hack, not all of the logs you see in Dev console will show up in the downloaded file 🤷.

4. 🎥 Finally. Under this code repository's root, run `python movie_script.py` in Terminal which generates your `movie_script.txt`. Then open up `movie.html` in browser and upload this movie script.



![devtools](https://github.com/chunw/GoogleSearches/blob/master/img/devtools.png "devtools")


![0](https://github.com/chunw/GoogleSearches/blob/master/img/upload.png "0")


