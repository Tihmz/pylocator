def create_link(link):
    i1 = link.index("vendor=")
    i2 = link.index("&")
    vendor = link[i1:i2]

    result =  "https://rpilocator.com/?instock&" + vendor
    return result

def create_message(target,product):

    link = create_link(product["link"])

    message = """From: PY Locator <python.testhere@gmail.com>
To: To {} <{}>
Subject: {}

Hello {},

{}

Here is a link to all the raspberry pi currently available in this store:

{}

Here is a link to all the raspberry pi currently available everywhere :

https://rpilocator.com/?instock

Have a nice day !

Powered by https://rpilocator.com/
""".format(target["name"],target["email"],product["title"],target["name"],product["summary"],link)
    return message


