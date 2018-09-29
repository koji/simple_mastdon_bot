from mastodon import Mastodon

# Register app - only once!

Mastodon.create_app(
     'pytooterapp',
     api_base_url = 'mastdon_instance',
     to_file = 'pytooter_clientcred.secret'
)

# Log in - either every time, or use persisted

mastodon = Mastodon(
    client_id = 'pytooter_clientcred.secret',
    api_base_url = 'mastdon_instance'
)
mastodon.log_in(
    'your_email_address',
    'your password',
    to_file = 'pytooter_usercred.secret'
)
