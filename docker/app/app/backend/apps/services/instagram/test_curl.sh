#curl -F 'client_id=1c6e23fc21894d5186ae33d0bf7fafd3' \
#     -F 'client_secret=3ef2d019f81643d781b14b40cd03ffb0' \
#     -F 'object=user' \
#     -F 'aspect=media' \
#     -F 'verify_token=2175573059.1c6e23f.4a599e218d174393867459d993a9b96f' \
#     -F 'callback_url=http://192.168.99.100:8000/services/instagram/subscription_callback/' \
#     https://api.instagram.com/v1/subscriptions/

    curl -F 'client_id=1c6e23fc21894d5186ae33d0bf7fafd3' \
    -F 'client_secret=3ef2d019f81643d781b14b40cd03ffb0' \
    -F 'grant_type=authorization_code' \
    -F 'redirect_uri=http://www.tetherboxapp.com' \
    -F 'code=7f1cfac636bc4c839d47efd1d93e55a0' \
    https://api.instagram.com/oauth/access_token




{"access_token":"2175573059.1c6e23f.4a599e218d174393867459d993a9b96f","user":{"username":"james.tarball","bio":"","website":"","profile_picture":"https:\/\/scontent.cdninstagram.com\/t51.2885-19\/11906329_960233084022564_1448528159_a.jpg","full_name":"","id":"2175573059"}}