# PY locator

### What is it ?

Python script to locate raspberry pi and flipper in stock

It work using the RSS feed of [rpi-locator](https://rpilocator.com/) 
and a little bit of scraping for the flipper zero

*/!\ For the official flipper0 store, the script will check if there are stocks for the geographical area of the computer*

For exemple, my server in France will tell me if there are flipper 0 in stock for France.

### How to use it ?

You can simply use it by installing dependancies and running the script :
```
$ git clone https://github.com/Tihmz/pylocator
$ cd pylocator
$ pip install -r requirements.txt
< setup config.json and credentials >
$ python run.py
```

You also need to setup the config file as in the [config_example.json](/config_example.json)
You can add as much emails as you want of course.

Finally, you need to setup the .creds.txt with the following content :
```
$ cat .creds.txt

mysuperemail@gmail.com:mysuperpassword
```

You can add a password to use your google account by following this [guide](https://support.google.com/accounts/answer/185833?)

