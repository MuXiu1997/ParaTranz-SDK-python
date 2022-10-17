# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from paratranz_client.paths.users_user_id import Api

from paratranz_client.paths import PathValues

path = PathValues.USERS_USER_ID