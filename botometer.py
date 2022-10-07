import botometer
from _init_ import Botometer

rapidapi_key = "0341eaa6b2mshfc43c2af180ff13p19d4a5jsne4e00c13532a"
twitter_app_auth = {
    'consumer_key': 'MNjVsWBuINDdWxx9A4hFEHmvT',
    'consumer_secret': 'xtgI6rg2Jcd0I8KjeyFZTh1PKMaBrHJcPCZA2RHMxvwtgoEmkN',
    'access_token': '1577736170212950017-to2AOGt32CqYfIB1Ycboz0MzI5vuMJ',
    'access_token_secret': 'ZUICchF0w76OKEevaLybC10bqnoLexVLAnvJBRml8okhe',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@DisneyPlus')
#print(result)
# Check a single account by id
result = bom.check_account(1548959833)
#print(result)
# Check a sequence of accounts
accounts = ['@hourlyyuzu', '@vismyg', '@emmekalin']
for screen_name, result in bom.check_accounts_in(accounts):
    print(screen_name)
    print(result)