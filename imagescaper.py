import requests

#  scrape image from facebook
r = requests.get('https://scontent.fnap3-2.fna.fbcdn.net/v/t1.18169-9/14292510_10209029540887132_5932358044782540699_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=RfK9OmfIDgwAX_Nlj7D&_nc_oc=AQlzC5wcTXnKEg5CcYwGJbVTd4e8HT4oMBiHT2Z5bKpwdo2oLFbNroGPilz_jFMcekM&_nc_ht=scontent.fnap3-2.fna&oh=00_AT8bYxyA1t2U2g4klr2hMMGw8zjQYCHvCUFG4vN4uUfD3g&oe=63102309')
print(r)

print(r.content)

binar = open('binar.jpg', 'wb')
binar.write(r.content)
binar.close()
