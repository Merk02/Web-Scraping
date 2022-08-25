import requests
# import shutil

# r = requests.get('https://mazwai.com/videvo_files/video/free/2019-07/small_watermarked/190625_07_RooftopFlightNight_Drone_04_preview.mp4')
r = requests.get('https://video.fnap3-1.fna.fbcdn.net/v/t42.9040-2/84547356_183504089528307_5965471740329984000_n.mp4?_nc_cat=106&ccb=1-7&_nc_sid=985c63&efg=eyJybHIiOjMwMCwicmxhIjo1MTIsInZlbmNvZGVfdGFnIjoic3ZlX3NkIn0%3D&_nc_ohc=4oG-oLYFHpIAX_WLHRc&_nc_ht=video.fnap3-1.fna&oh=00_AT82i2lwWGur6hOrClifWnWm3NT22Ux1q7drT9rCWNfvug&oe=62EBB86E')
file = open('video.mp4', 'wb')

for c in r.iter_content():
    file.write(c)

# if r.status_code == '200':
#   shutil.copyfileobj(r.raw, file)

