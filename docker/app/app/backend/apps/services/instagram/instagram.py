# #!/usr/bin/env python
# """
#     instagram.instagram
#     ===================

#     This is a wrapper for Instagram API

# """
# import logging

# from instagram.client import InstagramAPI
# from instagram import subscriptions

# from project.settings.base import get_env_varible

# logger = logging.getLogger('project_logger')

# ACCESS_TOKEN = get_env_varible("INSTAGRAM_ACCESS_TOKEN")
# CLIENT_SECRET = get_env_varible("INSTAGRAM_CLIENT_SECRET")
# for requests that you dont need auth
# # api = InstagramAPI(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
# CLIENT_ID = get_env_varible("INSTAGRAM_CLIENT_ID")

# SUBSCRIPTION_CALLBACK_URL = 'http://mydomain.com/hook/instagram'

# # Definitions of functions / api calls  -> to id for the database call


# class ServiceInstagram(object):
#     """ A wrapper for the Instagram API.

#         Available calls:
#             get_media_likes: Get a list of users who have liked this media.
#             like_media:      Set a like on this media by the currently authenicated user. THe public_content permission
#                               scope is required to create likes on a media that does not belong to the owner of the access_token.
#             unlike_media:    Remove a like on this media by the currently authenticated user. The public_content
#                               permission scope is required to delete likes on a media that does not belong to the owner of the access_token.

#     """

#     def __init__(self):
#         self.api = InstagramAPI(access_token=ACCESS_TOKEN, client_secret=CLIENT_SECRET)

#     def _check_status(self, response, api_call_name, id):
#         """ Checks the response of a API post or delete call. 
#             Assumes a successful call will give a response:
#             {
#                 "meta": {
#                     "code": 200
#                 },
#                 "data": null
#             }
#         """
#         meta = response['meta']
#         if meta['code'] == 200:
#             return True
#         else:
#             logger.error("Call '%s' failed for id: %s - data: %s " % (api_call_name, id, data))
#             return False

#     # Users
#     # -----
#     def get_user(self):
#         """ Get information about the owner of the access_token.
#             GET /users/self

#             https://api.instagram.com/v1/users/self/?access_token=ACCESS-TOKEN
#             {
#                 "data": {
#                     "id": "1574083",
#                     "username": "snoopdogg",
#                     "full_name": "Snoop Dogg",
#                     "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
#                     "bio": "This is my bio",
#                     "website": "http://snoopdogg.com",
#                     "counts": {
#                         "media": 1320,
#                         "follows": 420,
#                         "followed_by": 3410
#                     }
#             }
#         """
#         user = self.api.user_self()
#         return user['data']

#     def get_user_by_id(self, id):
#         """ Get information about a user. This endpoint requires the public_content scope if the user-id
#             is not the owner of the access_token.

#             GET /users/user-id

#             https://api.instagram.com/v1/users/{user-id}/?access_token=ACCESS-TOKEN
#             {
#                 "data": {
#                     "id": "1574083",
#                     "username": "snoopdogg",
#                     "full_name": "Snoop Dogg",
#                     "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
#                     "bio": "This is my bio",
#                     "website": "http://snoopdogg.com",
#                     "counts": {
#                         "media": 1320,
#                         "follows": 420,
#                         "followed_by": 3410
#                     }
#             }
#         """
#         user = self.api.user(user_id=id, count=10)
#         return user['data']

#     def get_user_recent_media(self, minimum_id, maximum_id, count=10):
#         """ Get the most recent media published by the owner of the access_token.

#             GET /users/self/media/recent

#             https://api.instagram.com/v1/users/self/media/recent/?access_token=ACCESS-TOKEN
#             {
#                 "data": [{
#                     "comments": {
#                         "count": 0
#                     },
#                     "caption": {
#                         "created_time": "1296710352",
#                         "text": "Inside le truc #foodtruck",
#                         "from": {
#                             "username": "kevin",
#                             "full_name": "Kevin Systrom",
#                             "type": "user",
#                             "id": "3"
#                         },
#                         "id": "26621408"
#                     },
#                     "likes": {
#                         "count": 15
#                     },
#                     "link": "http://instagr.am/p/BWrVZ/",
#                     "user": {
#                         "username": "kevin",
#                         "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
#                         "id": "3"
#                     },
#                     "created_time": "1296710327",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "type": "image",
#                     "users_in_photo": [],
#                     "filter": "Earlybird",
#                     "tags": ["foodtruck"],
#                     "id": "22721881",
#                     "location": {
#                         "latitude": 37.778720183610183,
#                         "longitude": -122.3962783813477,
#                         "id": "520640",
#                         "street_address": "",
#                         "name": "Le Truc"
#                     }
#                 },
#                 {
#                     "videos": {
#                         "low_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_102.mp4",
#                             "width": 480,
#                             "height": 480
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_101.mp4",
#                             "width": 640,
#                             "height": 640
#                         },
#                     "comments": {
#                         "count": 2
#                     },
#                     "caption": null,
#                     "likes": {
#                         "count": 1
#                     },
#                     "link": "http://instagr.am/p/D/",
#                     "created_time": "1279340983",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "type": "video",
#                     "users_in_photo": null,
#                     "filter": "Vesper",
#                     "tags": [],
#                     "id": "363839373298",
#                     "user": {
#                         "username": "kevin",
#                         "full_name": "Kevin S",
#                         "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
#                         "id": "3"
#                     },
#                     "location": null
#                 },
#                ]
#             }

#         """
#         media, _next = self.api.user_self_recent_media(count=count, mini_id=minimum_id, max_id=maximum_id)
#         return media['data']

#     def get_user_by_id_recent_media(self, minimum_id, maximum_id, count=10):
#         """ Get the most recent media published by a user. This endpoint requires the public_content scope if the user-id is not the owner of the access_token.

#             GET /users/user-id/media/recent

#             https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN
#             {
#                 "data": [{
#                     "comments": {
#                         "count": 0
#                     },
#                     "caption": {
#                         "created_time": "1296710352",
#                         "text": "Inside le truc #foodtruck",
#                         "from": {
#                             "username": "kevin",
#                             "full_name": "Kevin Systrom",
#                             "type": "user",
#                             "id": "3"
#                         },
#                         "id": "26621408"
#                     },
#                     "likes": {
#                         "count": 15
#                     },
#                     "link": "http://instagr.am/p/BWrVZ/",
#                     "user": {
#                         "username": "kevin",
#                         "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
#                         "id": "3"
#                     },
#                     "created_time": "1296710327",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/6ea7baea55774c5e81e7e3e1f6e791a7_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "type": "image",
#                     "users_in_photo": [],
#                     "filter": "Earlybird",
#                     "tags": ["foodtruck"],
#                     "id": "22721881",
#                     "location": {
#                         "latitude": 37.778720183610183,
#                         "longitude": -122.3962783813477,
#                         "id": "520640",
#                         "street_address": "",
#                         "name": "Le Truc"
#                     }
#                 },
#                 {
#                     "videos": {
#                         "low_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_102.mp4",
#                             "width": 480,
#                             "height": 480
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_101.mp4",
#                             "width": 640,
#                             "height": 640
#                         },
#                     "comments": {
#                         "count": 2
#                     },
#                     "caption": null,
#                     "likes": {
#                         "count": 1
#                     },
#                     "link": "http://instagr.am/p/D/",
#                     "created_time": "1279340983",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "type": "video",
#                     "users_in_photo": null,
#                     "filter": "Vesper",
#                     "tags": [],
#                     "id": "363839373298",
#                     "user": {
#                         "username": "kevin",
#                         "full_name": "Kevin S",
#                         "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
#                         "id": "3"
#                     },
#                     "location": null
#                 },
#                ]
#             }
#         """
#         media, _next = self.api.user_recent_media(count=count, mini_id=minimum_id, max_id=maximum_id)
#         return media['data']

#     def get_user_liked_media(self, max_like_id, count=10):
#         """ Get the list of recent media liked by the owner of the access_token.

#             GET /users/self/media/liked

#             https://api.instagram.com/v1/users/self/media/liked?access_token=ACCESS-TOKEN
#             {
#                 "data": [{
#                     "location": {
#                         "id": "833",
#                         "latitude": 37.77956816727314,
#                         "longitude": -122.41387367248539,
#                         "name": "Civic Center BART"
#                     },
#                     "comments": {
#                         "count": 16
#                     },
#                     "caption": null,
#                     "link": "http://instagr.am/p/BXsFz/",
#                     "likes": {
#                         "count": 190
#                     },
#                     "created_time": "1296748524",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/02/03/efc502667a554329b52d9a6bab35b24a_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/02/03/efc502667a554329b52d9a6bab35b24a_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/02/03/efc502667a554329b52d9a6bab35b24a_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "type": "image",
#                     "users_in_photo": [],
#                     "filter": "Earlybird",
#                     "tags": [],
#                     "id": "22987123",
#                     "user": {
#                         "username": "kevin",
#                         "full_name": "Kevin S",
#                         "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
#                         "id": "3"
#                     }
#                 },
#                 {
#                     "videos": {
#                         "low_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_102.mp4",
#                             "width": 480,
#                             "height": 480
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_101.mp4",
#                             "width": 640,
#                             "height": 640
#                         },
#                     "comments": {
#                         "count": 2
#                     },
#                     "caption": null,
#                     "likes": {
#                         "count": 1
#                     },
#                     "link": "http://instagr.am/p/D/",
#                     "created_time": "1279340983",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "type": "video",
#                     "users_in_photo": null,
#                     "filter": "Vesper",
#                     "tags": [],
#                     "id": "363839373298",
#                     "user": {
#                         "username": "kevin",
#                         "full_name": "Kevin S",
#                         "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_3_75sq_1295574122.jpg",
#                         "id": "3"
#                     },
#                     "location": null
#                 },
#                 ...]
#             }
#         """
#         media, _next = self.api.get_user_liked_media(max_like_id=max_like_id, count=count)
#         return media['data']

#     def user_search(self, query):
#         """ Get a list of users matching the query.

#             GET /users/search

#             https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
#             {
#                 "data": [{
#                     "username": "jack",
#                     "first_name": "Jack",
#                     "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_66_75sq.jpg",
#                     "id": "66",
#                     "last_name": "Dorsey"
#                 },
#                 {
#                     "username": "sammyjack",
#                     "first_name": "Sammy",
#                     "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_29648_75sq_1294520029.jpg",
#                     "id": "29648",
#                     "last_name": "Jack"
#                 },
#                 {
#                     "username": "jacktiddy",
#                     "first_name": "Jack",
#                     "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_13096_75sq_1286441317.jpg",
#                     "id": "13096",
#                     "last_name": "Tiddy"
#                 }]
#             }
#         """
#         users = self.api.user_search(q=query, count=count, lat=latitude, lng=longitude, min_timestamp=minimum_timestamp, max_timestamp=maximum_stamp)
#         return users['data']

#     # Relationships
#     # -------------
#     def get_users_self_follows(self):
#         """ Get the list of users this user follows.

#             GET /users/self/follows

#             https://api.instagram.com/v1/users/self/follows?access_token=ACCESS-TOKEN
#             {
#                 "data": [{
#                     "username": "kevin",
#                     "profile_picture": "http://images.ak.instagram.com/profiles/profile_3_75sq_1325536697.jpg",
#                     "full_name": "Kevin Systrom",
#                     "id": "3"
#                 },
#                 {
#                     "username": "instagram",
#                     "profile_picture": "http://images.ak.instagram.com/profiles/profile_25025320_75sq_1340929272.jpg",
#                     "full_name": "Instagram",
#                     "id": "25025320"
#                 }]
#             }
#         """
#         followers, _next = self.api.user_self_follows()
#         return followers['data']

#     def get_user_self_followers(self):
#         """ Get the list of users this user is followed by.

#             GET /users/self/followed-by

#             https://api.instagram.com/v1/users/self/followed-by?access_token=ACCESS-TOKEN
#             {
#                 "data": [{
#                     "username": "kevin",
#                     "profile_picture": "http://images.ak.instagram.com/profiles/profile_3_75sq_1325536697.jpg",
#                     "full_name": "Kevin Systrom",
#                     "id": "3"
#                 },
#                 {
#                     "username": "instagram",
#                     "profile_picture": "http://images.ak.instagram.com/profiles/profile_25025320_75sq_1340929272.jpg",
#                     "full_name": "Instagram",
#                     "id": "25025320"
#                 }]
#             }
#         """
#         followers, _next = self.api.user_self_followers()
#         return followers['data']

#     def get_users_requested_to_follow_self(self):
#         """ List the users who have requested this user's permission to follow.

#             GET /users/self/requested-by

#             https://api.instagram.com/v1/users/self/requested-by?access_token=ACCESS-TOKEN
#             {
#                 "data": [
#                     {
#                         "username": "mikeyk",
#                         "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_4_75sq_1292324747_debug.jpg",
#                         "id": "4"
#                     }
#                 ]
#             }
#         """
#         requested_by, _next = self.api.user_self_requested_by()
#         return requested_by['data']

#     def get_user_relationship(self, id):
#         """ Get information about a relationship to another user. Relationships are expressed using the following terms in the response:

#             outgoing_status: Your relationship to the user. Can be 'follows', 'requested', 'none'.
#             incoming_status: A user's relationship to you. Can be 'followed_by', 'requested_by', 'blocked_by_you', 'none'.

#             GET /users/user-id/relationship

#             https://api.instagram.com/v1/users/{user-id}/relationship?access_token=ACCESS-TOKEN
#             {
#                 "data": {
#                     "outgoing_status": "none",
#                     "incoming_status": "requested_by"
#                 }
#             }

#         """
#         relationship = self.api.user_relationship(user_id=id)
#         return relationship['data']

#     def set_user_relationship(self, id, action):
#         """ Modify the relationship between the current user and the target user. You need to include an action parameter to specify the relationship action you want to perform. Valid actions are: 'follow', 'unfollow' 'approve' or 'ignore'. Relationships are expressed using the following terms in the response:

#             outgoing_status: Your relationship to the user. Can be 'follows', 'requested', 'none'.
#             incoming_status: A user's relationship to you. Can be 'followed_by', 'requested_by', 'blocked_by_you', 'none'.

#             Parameters
#             action  follow | unfollow | approve | ignore

#             POST /users/user-id/relationship

#             https://api.instagram.com/v1/users/{user-id}/relationship?access_token=ACCESS-TOKEN
#             {
#                 "data": {
#                     "outgoing_status": "requested"
#                 }
#             }
#         """
#         self.api.set_user_relationship(user_id=id, action=action)
#         # status code??

#     def follow_user(self, id):
#         """ Follow user. """
#         self.api.follow_user(user_id=id)

#     def unfollow_user(self, id):
#         """ Unfollow user. """
#         self.api.unfollow_user(user_id=id)

#     def block_user(self, id):
#         """ Block user. """
#         self.api.block_user(user_id=id)

#     def unblock_user(self, id):
#         """ Unblock user. """
#         self.api.unblock_user(user_id=id)

#     def approve_user(self, id):
#         """ Approve user. """
#         self.api.approve_user(user_id=id)

#     def unapprove_user(self, id):
#         """ Unapprove user. """
#         self.api.unapprove_user(user_id=id)

#     def get_user_followers(self, id):
#         """ Get the list of users this user follows.

#             GET /users/self/follows

#             https://api.instagram.com/v1/users/self/follows?access_token=ACCESS-TOKEN
#             {
#                 "data": [{
#                     "username": "kevin",
#                     "profile_picture": "http://images.ak.instagram.com/profiles/profile_3_75sq_1325536697.jpg",
#                     "full_name": "Kevin Systrom",
#                     "id": "3"
#                 },
#                 {
#                     "username": "instagram",
#                     "profile_picture": "http://images.ak.instagram.com/profiles/profile_25025320_75sq_1340929272.jpg",
#                     "full_name": "Instagram",
#                     "id": "25025320"
#                 }]
#             }
#         """
#         followers, _next = self.api.user_followers(user_id=id)
#         return followers['data']

#     # Subscriptions
#     # -------------
#     def create_subscription_users(self):
#         """ Subscribe to updates for ALL users authenticated to our app. 
#             So when a user that is authenticated our app posts new media we will get an post by Instagram (similar to pubsubhubub protocol)
#         """
#         self.api.create_subscription(object='user', aspect='media', callback_url=SUBSCRIPTION_CALLBACK_URL)

#     def create_subscription_from_tag(self, tag):
#         """ Subscribe to all media for ALL user authenticated to our app tagged with <tag>. """
#         self.api.create_subscription(object='tag', object_id=tag, aspect='media', callback_url=SUBSCRIPTION_CALLBACK_URL)

#     def create_subscription_from_location(self, location_id):
#         """ Subscribe to all media for ALL user authenticated to our app tagged with <location>. """
#         self.api.create_subscription(object='location', object_id=location_id, aspect='media', callback_url=SUBSCRIPTION_CALLBACK_URL)

#     def get_subscriptions(self):
#         """ List Subscriptions. """
#         self.api.list_subscriptions()

#     def delete_subscriptions(self, id):
#         """ Delete Subscriptions. """
#         self.api.delete_subscriptions(id=id)

#     # Media
#     # -----
#     def get_media(self, id):
#         """ Get information about a media object. Use the type field to differentiate between image and video media
#         in the response. You will also receive the user_has_liked field which tells you whether the owner of the 
#         access_token has liked this media.
#             The public_content permission scope is required to get a media that does not belong to the owner of the access_token.

#             GET /media/media-id

#             https://api.instagram.com/v1/media/{media-id}?access_token=ACCESS-TOKEN
#             {
#                 "data": {
#                     "type": "image",
#                     "users_in_photo": [{
#                         "user": {
#                             "username": "kevin",
#                             "full_name": "Kevin S",
#                             "id": "3",
#                             "profile_picture": "..."
#                         },
#                         "position": {
#                             "x": 0.315,
#                             "y": 0.9111
#                         }
#                     }],
#                     "filter": "Walden",
#                     "tags": [],
#                     "comments": {
#                         "count": 2
#                     },
#                     "caption": null,
#                     "likes": {
#                         "count": 1
#                     },
#                     "link": "http://instagr.am/p/D/",
#                     "user": {
#                         "username": "kevin",
#                         "full_name": "Kevin S",
#                         "profile_picture": "...",
#                         "id": "3"
#                     },
#                     "created_time": "1279340983",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "id": "3",
#                     "location": null
#                 }
#             }

#             /*------------
#             Video Example
#             -------------*/

#             {
#                 "data": {
#                     "type": "video",
#                     "videos": {
#                         "low_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_102.mp4",
#                             "width": 480,
#                             "height": 480
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_101.mp4",
#                             "width": 640,
#                             "height": 640
#                         },
#                 "users_in_photo": null,
#                     "filter": "Vesper",
#                     "tags": [],
#                     "comments": {
#                         "count": 2
#                     },
#                     "caption": null,
#                     "likes": {
#                         "count": 1
#                     },
#                     "link": "http://instagr.am/p/D/",
#                     "user": {
#                         "username": "kevin",
#                         "full_name": "Kevin S",
#                         "profile_picture": "...",
#                         "id": "3"
#                     },
#                     "created_time": "1279340983",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "id": "3",
#                     "location": null
#                 }
#             }
#         """
#         media = self.api.media(media_id=id)
#         return media['data']

#     def get_media_by_shortcode(self, shortcode):
#         """ This endpoint returns the same response as GET /media/media-id.
#             A media object's shortcode can be found in its shortlink URL. An example shortlink is http://instagram.com/p/tsxp1hhQTG/. Its corresponding shortcode is tsxp1hhQTG.

#             GET /media/shortcode/shortcode

#             Response
#             https://api.instagram.com/v1/media/shortcode/D?access_token=ACCESS-TOKEN
#             {
#                 "data": {
#                     "type": "image",
#                     "users_in_photo": [{
#                         "user": {
#                             "username": "kevin",
#                             "full_name": "Kevin S",
#                             "id": "3",
#                             "profile_picture": "..."
#                         },
#                         "position": {
#                             "x": 0.315,
#                             "y": 0.9111
#                         }
#                     }],
#                     "filter": "Walden",
#                     "tags": [],
#                     "comments": {
#                         "count": 2
#                     },
#                     "caption": null,
#                     "likes": {
#                         "count": 1
#                     },
#                     "link": "http://instagr.am/p/D/",
#                     "user": {
#                         "username": "kevin",
#                         "full_name": "Kevin S",
#                         "profile_picture": "...",
#                         "id": "3"
#                     },
#                     "created_time": "1279340983",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2010/07/16/4de37e03aa4b4372843a7eb33fa41cad_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "id": "3",
#                     "location": null
#                 }
#             }

#             /*------------
#             Video Example
#             -------------*/

#             {
#                 "data": {
#                     "type": "video",
#                     "videos": {
#                         "low_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_102.mp4",
#                             "width": 480,
#                             "height": 480
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_101.mp4",
#                             "width": 640,
#                             "height": 640
#                         },
#                 "users_in_photo": null,
#                     "filter": "Vesper",
#                     "tags": [],
#                     "comments": {
#                         "count": 2
#                     },
#                     "caption": null,
#                     "likes": {
#                         "count": 1
#                     },
#                     "link": "http://instagr.am/p/D/",
#                     "user": {
#                         "username": "kevin",
#                         "full_name": "Kevin S",
#                         "profile_picture": "...",
#                         "id": "3"
#                     },
#                     "created_time": "1279340983",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "id": "3",
#                     "location": null
#                 }
#             }
#         """
#         media = self.api.media_shortcode(shortcode=shortcode)
#         return media['data']

#     def media_search(self, query, latitude, longitude, distance=1000):
#         """ Search for recent media in a given area.
#         """
#         media = self.api.media_search(q=query, lat=latitude, lng=longitude, distance=distance)
#         return media['data']

#     # Likes
#     # -----
#     def get_media_likes(self, id):
#         """ Get a list of users who have liked this media.
#             id: The ID of the media object to reference.

#             returns list of users (i.e. excludes data bit)

#         https://api.instagram.com/v1/media/{media-id}/likes?access_token=ACCESS-TOKEN
#         {
#             "data": [{
#                 "username": "jack",
#                 "first_name": "Jack",
#                 "last_name": "Dorsey",
#                 "type": "user",
#                 "id": "66"
#             },
#             {
#                 "username": "sammyjack",
#                 "first_name": "Sammy",
#                 "last_name": "Jack",
#                 "type": "user",
#                 "id": "29648"
#             }]
#         }

#         """
#         users = self.api.media_likes(media_id=id)
#         return users['data']

#     def like_media(self, id):
#         """ Set a like on this media by the currently authenticated user. The public_content permission scope is 
#             required to create likes on a media that does not belong to the owner of the access_token.
#             id: The ID of the media object to reference


#             curl -F 'access_token=ACCESS-TOKEN' \ https://api.instagram.com/v1/media/{media-id}/likes
#             {
#                 "meta": {
#                     "code": 200
#                 },
#                 "data": null
#             }
#         """
#         response = self.api.like_media(media_id=id)
#         return self._check_status(response, 'like_media', id)

#     def unlike_media(self, id):
#         """ Remove a like on this media by the currently authenticated user. The public_content permission scope 
#         is required to delete likes on a media that does not belong to the owner of the access_token.

#         curl -X DELETE https://api.instagram.com/v1/media/{media-id}/likes?access_token=ACCESS-TOKEN
#         {
#             "meta": {
#                 "code": 200
#             },
#             "data": null
#         }

#         """
#         response = self.api.unlike_media(media_id=id)
#         return self._check_status(response, 'unlike_media', id)

#     # Comments'
#     # ========
#     def get_media_comments(self, id):
#         """ Get a list of recent comments on a media object. The public_content permission scope is required to get
#          comments for a media that does not belong to the owner of the access_token.

#         https://api.instagram.com/v1/media/{media-id}}/comments?access_token=ACCESS-TOKEN
#         {
#             "data": [
#                 {
#                     "created_time": "1280780324",
#                     "text": "Really amazing photo!",
#                     "from": {
#                         "username": "snoopdogg",
#                         "profile_picture": "http://images.instagram.com/profiles/profile_16_75sq_1305612434.jpg",
#                         "id": "1574083",
#                         "full_name": "Snoop Dogg"
#                     },
#                     "id": "420"
#                 },
#                 ...
#             ]
#         }
#         """
#         comments = self.api.media_comments(media_id=id)
#         return comments['data']

#     def add_comment(self, id, comment):
#         """ Create a comment on a media object with the following rules:

#             The total length of the comment cannot exceed 300 characters.
#             The comment cannot contain more than 4 hashtags.
#             The comment cannot contain more than 1 URL.
#             The comment cannot consist of all capital letters.

#             The public_content permission scope is required to create comments on a media that does not belong to the owner of the access_token.
    
#             curl -F 'access_token=ACCESS-TOKEN' \ -F 'text=This+is+my+comment' \ https://api.instagram.com/v1/media/{media-id}/comments
#             {
#                 "meta": {
#                     "code": 200
#                 },
#                 "data": null
#             }
#         """
#         response = self.api.create_media_comment(media_id=id, text=comment)
#         return self._check_status(response, 'add_comment', id)

#     def delete_comment(self, id, comment_id):
#         """ Remove a comment either on the authenticated user's media object or authored by the authenticated user.

#             curl -X DELETE https://api.instagram.com/v1/media/{media-id}/comments/{comment-id}?access_token=ACCESS-TOKEN
#             {
#                 "meta": {
#                     "code": 200
#                 },
#                 "data": null
#             }

#         """
#         response = self.api.delete_comment(media_id=id, comment_id=comment_id)
#         return self._check_status(response, 'delete_comment', id)

#     # Tags
#     # ====
#     def get_tag_info(self, name):
#         """ Get information about a tag object.

#             https://api.instagram.com/v1/tags/{tag-name}?access_token=ACCESS-TOKEN
#             {
#                 "data": {
#                     "media_count": 472,
#                     "name": "nofilter",
#                 }
#             }
#         """
#         tag_info = self.api.tag(tag_name=name)
#         return tag_info['data']

#     def get_recent_tags(self, name, max_tag_id, count=10):
#         """ Get a list of recently tagged media.
#         https://api.instagram.com/v1/tags/{tag-name}/media/recent?access_token=ACCESS-TOKEN
#         {
#             "data": [{
#                 "type": "image",
#                 "users_in_photo": [],
#                 "filter": "Earlybird",
#                 "tags": ["snow"],
#                 "comments": {
#                     "count": 3
#                 },
#                 "caption": {
#                     "created_time": "1296703540",
#                     "text": "#Snow",
#                     "from": {
#                         "username": "emohatch",
#                         "id": "1242695"
#                     },
#                     "id": "26589964"
#                 },
#                 "likes": {
#                     "count": 1
#                 },
#                 "link": "http://instagr.am/p/BWl6P/",
#                 "user": {
#                     "username": "emohatch",
#                     "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1242695_75sq_1293915800.jpg",
#                     "id": "1242695",
#                     "full_name": "Dave"
#                 },
#                 "created_time": "1296703536",
#                 "images": {
#                     "low_resolution": {
#                         "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/f9443f3443484c40b4792fa7c76214d5_6.jpg",
#                         "width": 306,
#                         "height": 306
#                     },
#                     "thumbnail": {
#                         "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/f9443f3443484c40b4792fa7c76214d5_5.jpg",
#                         "width": 150,
#                         "height": 150
#                     },
#                     "standard_resolution": {
#                         "url": "http://distillery.s3.amazonaws.com/media/2011/02/02/f9443f3443484c40b4792fa7c76214d5_7.jpg",
#                         "width": 612,
#                         "height": 612
#                     }
#                 },
#                 "id": "22699663",
#                 "location": null
#             },
#             {
#                 "type": "video",
#                 "videos": {
#                     "low_resolution": {
#                         "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_102.mp4",
#                         "width": 480,
#                         "height": 480
#                     },
#                     "standard_resolution": {
#                         "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_101.mp4",
#                         "width": 640,
#                         "height": 640
#                     },
#                 "users_in_photo": null,
#                 "filter": "Vesper",
#                 "tags": ["snow"],
#                 "comments": {
#                     "count": 2
#                 },
#                 "caption": {
#                     "created_time": "1296703540",
#                     "text": "#Snow",
#                     "from": {
#                         "username": "emohatch",
#                         "id": "1242695"
#                     },
#                     "id": "26589964"
#                 },
#                 "likes": {
#                     "count": 1
#                 },
#                 "link": "http://instagr.am/p/D/",
#                 "user": {
#                     "username": "kevin",
#                     "full_name": "Kevin S",
#                     "profile_picture": "...",
#                     "id": "3"
#                 },
#                 "created_time": "1279340983",
#                 "images": {
#                     "low_resolution": {
#                         "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_6.jpg",
#                         "width": 306,
#                         "height": 306
#                     },
#                     "thumbnail": {
#                         "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_5.jpg",
#                         "width": 150,
#                         "height": 150
#                     },
#                     "standard_resolution": {
#                         "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_7.jpg",
#                         "width": 612,
#                         "height": 612
#                     }
#                 },
#                 "id": "3",
#                 "location": null
#             },
#             ...]
#         }
#         """
#         recent_tags = self.api.tag_recent_media(tag_name=name, count=count, max_tag_id=max_tag_id)
#         return recent_tags['data']

#     def tag_search(self, query, count=10):
#         """ Search for tags by name.

#             https://api.instagram.com/v1/tags/search?q=snowy&access_token=ACCESS-TOKEN
#             {
#                 "data": [
#                     {
#                         "media_count": 43590,
#                         "name": "snowy"
#                     },
#                     {
#                         "media_count": 3264,
#                         "name": "snowyday"
#                     },
#                     {
#                         "media_count": 1880,
#                         "name": "snowymountains"
#                     }
#                 ]
#             }
#         """
#         tags = self.api.tag_search(q=query, count=count)
#         return tags['data']

#     # Location
#     # ========
#     def get_location(self, id):
#         """ Get information about a location.

#             https://api.instagram.com/v1/locations/{location-id}?access_token=ACCESS-TOKEN
#             {
#                 "data": {
#                     "id": "1",
#                     "name": "Dogpatch Labs",
#                     "latitude": 37.782,
#                     "longitude": -122.387,
#                 }
#             }
#         """
#         location = self.api.location(location_id=id)
#         return location['data']

#     def get_recent_media_from_location(self, id, max_id, count=10):
#         """ Get a list of recent media objects from a given location.

#             https://api.instagram.com/v1/locations/{location-id}/media/recent?access_token=ACCESS-TOKEN
#             {
#                 "data": [{
#                     "type": "image",
#                     "users_in_photo": [],
#                     "filter": "Earlybird",
#                     "tags": ["expobar"],
#                     "comments": {
#                         "count": 0
#                     },
#                     "caption": {
#                         "created_time": "1296532028",
#                         "text": "@mikeyk pulls a shot on our #Expobar",
#                         "from": {
#                             "username": "josh",
#                             "full_name": "Josh Riedel",
#                             "type": "user",
#                             "id": "33"
#                         },
#                         "id": "25663923"
#                     },
#                     "likes": {
#                         "count": 35
#                     },
#                     "link": "http://instagr.am/p/BUS3X/",
#                     "user": {
#                         "username": "josh",
#                         "profile_picture": "...",
#                         "id": "33"
#                     },
#                     "created_time": "1296531955",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/01/31/32d364527512437a8a17ba308a7c83bb_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/01/31/32d364527512437a8a17ba308a7c83bb_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distillery.s3.amazonaws.com/media/2011/01/31/32d364527512437a8a17ba308a7c83bb_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "user_has_liked": false,
#                     "id": "22097367",
#                     "location": {
#                         "latitude": 37.780885099999999,
#                         "id": "514276",
#                         "longitude": -122.3948632,
#                         "name": "Instagram"
#                     }
#                 },
#                 {
#                     "type": "video",
#                     "videos": {
#                         "low_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_102.mp4",
#                             "width": 480,
#                             "height": 480
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryvesper9-13.ak.instagram.com/090d06dad9cd11e2aa0912313817975d_101.mp4",
#                             "width": 640,
#                             "height": 640
#                         },
#                     "users_in_photo": null,
#                     "filter": "Vesper",
#                     "tags": [],
#                     "comments": {
#                         "count": 2
#                     },
#                     "caption": null,
#                     "likes": {
#                         "count": 1
#                     },
#                     "link": "http://instagr.am/p/D/",
#                     "user": {
#                         "username": "kevin",
#                         "full_name": "Kevin S",
#                         "profile_picture": "...",
#                         "id": "3"
#                     },
#                     "created_time": "1279340983",
#                     "images": {
#                         "low_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_6.jpg",
#                             "width": 306,
#                             "height": 306
#                         },
#                         "thumbnail": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_5.jpg",
#                             "width": 150,
#                             "height": 150
#                         },
#                         "standard_resolution": {
#                             "url": "http://distilleryimage2.ak.instagram.com/11f75f1cd9cc11e2a0fd22000aa8039a_7.jpg",
#                             "width": 612,
#                             "height": 612
#                         }
#                     },
#                     "id": "3",
#                     "location": {
#                         "latitude": 37.780885099999999,
#                         "id": "514276",
#                         "longitude": -122.3948632,
#                         "name": "Instagram"
#                     }
#                 },
#                 ...]
#             }

#         """
#         locations = self.api.location_recent_media(count=count, max_id=max_id, location_id=id)
#         return locations['data']

#         def location_search(self, query, latitude, longitude, foursquare_id, foursquare_v2_id, count=10):
#             """ Search for a location by geographic coordinate.

#                 GET /locations/search
#                 https://api.instagram.com/v1/locations/search?lat=48.858844&lng=2.294351&access_token=ACCESS-TOKEN
#                 {
#                     "data": [{
#                         "id": "788029",
#                         "latitude": 48.858844300000001,
#                         "longitude": 2.2943506,
#                         "name": "Eiffel Tower, Paris"
#                     },
#                     {
#                         "id": "545331",
#                         "latitude": 48.858334059662262,
#                         "longitude": 2.2943401336669909,
#                         "name": "Restaurant 58 Tour Eiffel"
#                     },
#                     {
#                         "id": "421930",
#                         "latitude": 48.858325999999998,
#                         "longitude": 2.294505,
#                         "name": "American Library in Paris"
#                     }]
#                 }
#                 Search for a location by geographic coordinate.

#                 Requirements
#                 Scope: public_content
#                 Parameters
#                 distance            Default is 1000m (distance=1000), max distance is 5000.
#                 facebook_places_id  Returns a location mapped off of a Facebook places id. If used, a Foursquare id 
#                                      and lat, lng are not required.
#                 access_token        A valid access token.
#                 foursquare_id       Returns a location mapped off of a foursquare v1 api location id. If used, you are not
#                                      required to use lat and lng. Note that this method is deprecated; you should use the
#                                      new foursquare IDs with V2 of their API.
#                 lat                 Latitude of the center search coordinate. If used, lng is required.
#                 lng                 Longitude of the center search coordinate. If used, lat is required.
#                 foursquare_v2_id    Returns a location mapped off of a foursquare v2 api location id. If used, you are 
#                                     not required to use lat and lng.

#             """
#             locations = self.api.location_search(q=query, count=count, lat=latitude, lng=longitude, foursquare_id=foursquare_id, foursquare_v2_id=foursquare_v2_id)
#             return locations['data']
