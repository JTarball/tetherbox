# import logging

# from instagram import subscriptions

# logger = logging.get_logger('project_logger')


# def process_user_update(update):
#     logger.info('process_user_update')
#     print(update)


# def process_tag_update(update):
#     logger.info('process_tag_update')
#     print(update)


# def process_location_update(update):
#     logger.info('process_location_update')
#     print(update)

# # React to user type updates
# reactor = subscriptions.SubscriptionsReactor()
# reactor.register_callback(subscriptions.SubscriptionType.USER, process_user_update)
# reactor.register_callback(subscriptions.SubscriptionType.TAG, process_tag_update)
# reactor.register_callback(subscriptions.SubscriptionType.LOCATION, process_location_update)
