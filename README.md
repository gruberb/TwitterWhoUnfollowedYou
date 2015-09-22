# TwitterWhoUnfollowedYou

A first, simple solution to find out who unfollowed you on twitter.
First, run

`python init.py`

to save your list of friends, and then, later the day or whenever you want to
know who unfollowed you until then, run

`python find_unfollowers.py`

Future improvements are to run the script every hour, to have a clearer dataset, since a lot can happen during a day.

## Install

1. Clone the repo `git clone git@github.com:gruberb/TwitterWhoUnfollowedYou.git`
2. Navigate to project folder `cd TwitterWhoUnfollowedYou`
3. Create a virtualenvironment with `virtualenv venv`
4. Activate virtualenv with `source venv/bin/activate`
5. Install the requirements with `pip install -r requirements.txt`

Now, you have to add your own credentials. Either via a credentials.py file with the following format:

```python
twitter = {
    "consumer_key": "YOUR_CONSUMER_KEY",
    "consumer_secret": "YOUR_CONSUMER_SECRET_KEY",
    "access_token_key": "YOUR_ACCESS_TOKEN_KEY",
    "access_token_secret": "YOUR_ACCESS_TOKEN_SECRET"
 }
```
Any help to create your tokens can be found on the official [twitter site](https://dev.twitter.com/oauth/overview/application-owner-access-tokens).


## Usage

-- work in progess --
