from thecatapi import TheCatAPI

catapi = TheCatAPI(api_key='live_FkOnFCtfJUcl5A1CvNBnaqXbX2MpjQcG2UbwI7FXr3Jkh7LfLv7EHOGQJMaGDwdU')

# images
# print(catapi.images.get_images(limit=10, mime_types='png,gif'))
# print(catapi.images.get_image(image_id='2bbSbBC-v'))
# print(catapi.images.get_image_analysis(image_id='2bbSbBC-v'))
# print(catapi.images.get_my_images(limit='10'))
# print(catapi.images.upload_image(file='/Users/ozorku/Desktop/screenshot.png', sub_id='1', breed_ids='abys'))
# print(catapi.images.delete_image(image_id='dMsUj1-nz'))
# print(catapi.images.get_image_breeds(image_id='2bbSbBC-v'))
# print(catapi.images.update_image_breeds(image_id='2bbSbBC-v', breed_id=''))
# print(catapi.images.delete_image_breeds(image_id='2bbSbBC-v', breed_id=''))

# votes
# print(catapi.votes.get_votes(limit='10'))
# print(catapi.votes.get_vote(vote_id=))
# print(catapi.votes.upvote(image_id='2bbSbBC-v', sub_id='1'))
# print(catapi.votes.downvote(image_id='2bbSbBC-v', sub_id='2'))

# breeds
# print(catapi.breeds.get_breeds())
# print(catapi.breeds.get_breed(breed_id='abys'))
# print(catapi.breeds.get_breed_facts(breed_id='ragd'))
# print(catapi.breeds.search_breed(q='ba', attach_image='1'))

# facts - premium
# print(catapi.facts.get_facts(limit='10', page='0', order='ASC'))

# favourites
# print(catapi.favourites.get_favourites())
# print(catapi.favourites.get_favourite(favourite_id=))
# print(catapi.favourites.create_favourite(image_id=, sub_id=))
# print(catapi.favourites.delete_favourite(favourite_id=))
