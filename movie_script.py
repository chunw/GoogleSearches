import os
import re

inputfiles = []
for filename in os.listdir('.'):
    if filename.endswith('.log'):
        if not re.search('[0-9].[a-zA-z0-9]+.log', filename):
            print('============ warning ===============')
            print('{} is not used to generate movie script...'.format(filename))
            print('Make sure you have it named in this format: [play_order.movie_clip_title.log]. E.g. "1.mymovie.log"')
            print('')
        else:
            inputfiles.append(filename)
    else:
        continue
inputfiles.sort(key=lambda filename: int(filename.split('.')[0]))

total_count = 0
with open('movie_script.txt', 'w') as outfile:
    for filename in inputfiles:
         searches = []
         with open(filename, 'r') as f:
             lines = f.readlines()
             for l in lines:
                 m = re.search('VM[0-9]+:[0-9] "*"', l)
                 if m:
                     search_entry = l.split('"')[1]
                     searches.append(search_entry)
             total_count += len(searches)
             print('{} search entries found in {}'.format(len(searches), filename))
             searches.reverse() # show in chronological order
             outfile.write('Title: ' + filename.split('.')[1] + '\n')
             for search_entry in searches:
                outfile.write(search_entry + '\n')


print('Your movie is composed of {} search entries.'.format(total_count))
print('You\'ll find a file named `movie_script.txt` in this folder. Upload it to movie.html.')
