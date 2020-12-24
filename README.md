# twitter-word-cloud-generator
Generates word cloud from a user's tweets(and retweets)

## How to Run
First, get your *consumer_key, consumer_secret, access_token_key, access_token_secret* from [here](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)

Then, clone this repository and install the requirements.

```
$ git clone https://github.com/sudeephb/twitter-word-cloud-generator
$ cd twitter-word-cloud-generator
$ pip install -r requirements.txt
```

Them, open the <i> 'keys.json' </i> file. Replace all the 'XXXXX' by the corresponding secret keys that you obtained from https://developer.twitter.com/.   

After that, run the <i> 'generate.py' </i> file passing the username of the user whose tweets you want to see the wordcloud of. You can also pass the desired
filename of the output file, without extenstion. If not passed, it defaults to <i> 'my_wordcloud.png' </i>

```
$ python generate.py username [filename]
```

For example, if I wanted to generate a word cloud of [my tweets](https://twitter.com/sudeeph_b) in the file <i>'output_cloud.png'</i> : 

```
$ python generate.py sudeeph_b output_word_cloud
```

This saves the wordcloud as seen below in 'output_word_cloud.png'
