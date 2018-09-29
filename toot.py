from mastodon import Mastodon

# Create actual API instance
mastodon = Mastodon(
    access_token = 'pytooter_usercred.secret',
    api_base_url = 'mastdon_instance'
)

cnt = 0
while(cnt<10):
    mastodon.toot('hello world!!! #python #bottest count ' + str(cnt))
    cnt=cnt+1
