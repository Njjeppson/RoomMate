from importlib.abc import InspectLoader
import json
import firebase_admin
from firebase_admin import db


def main():
	# Set up Firebase

	databaseURL = 'https://roommate-d4e64-default-rtdb.firebaseio.com/'
	cred_obj = firebase_admin.credentials.Certificate('roommate_key.json')

	default_app = firebase_admin.initialize_app(cred_obj, {
		'databaseURL':databaseURL
		})

	ref = db.reference("/")

	# Get firebase data
	with open('roommatedatabase.json', 'w') as outfile:
		json.dump(ref.get(), outfile)
		outfile.close()

	points = {
		'isOlder': 0,
		'isYounger': 0,
		'isSameAge': 0,
		'isMale': 0,
		'isFemale': 0,
		'isOtherGender': 0,
		'isChristian': 0,
		'isJewish': 0,
		'isMuslim': 0,
		'isHindu': 0,
		'isBuddhist': 0,
		'isSecular': 0,
		'isOtherReligion': 0,
		'isRepublican': 0,
		'isDemocrat': 0,
		'isSocialist': 0,
		'isGreen': 0,
		'isOtherParty': 0,
		'isProgressive': 0,
		'isConservative': 0,
		'isEarlyBird': 0,
		'isNightOwl': 0,
		'isNotSocial': 0,
		'isLittleSocial': 0,
		'isSocial': 0,
		'isInterest': {}
	}


	def interview(ref):
		name = input('What is your full name? ').lower()
		age = int(input('How old are you? '))
		gender = input('What is your gender? Male (M), Female (F), Other (O). ').lower()
		religion = int(input('What is your religious affiliation? Christian (1), Jewish (2), Muslim (3), Hindu (4), Buddhist (5), Secular (6), Other (7). '))
		politic = int(input('What would you say is the political party you affiliate the most with? Republican (1), Democrat (2), Socialist (3), Green (4), Other (5).) '))
		alignment = int(input('Would you say you are more progressive (1) or conservative (2)? '))
		time = int(input('Are you an early bird (1) or a night owl (2)? '))
		social = int(input('How social are you? Not at all (1), a little bit (2), or very (3)? '))

		print('What are some other key words that apply to you? Such as interests/hobbies/music/series/etc. (Enter one at a time and input "F" when finished)')
		interests = []
		interest = 'null'
		while interest != 'f':
			interest = input('> ').lower()
			if interest != 'f':
				interests.append(interest)
		if interests == []:
			interests.append('none')

		dictionary = {name: {'name': name,
					'age': age,
					'gender': gender,
					'religion': religion,
					'politic': politic,
					'alignment': alignment,
					'time': time,
					'social': social,
					'interests': interests
					}}

		with open('roommatedatabase.json', "r") as file:
			data = json.load(file)
			data.update(dictionary)

		with open('roommatedatabase.json', 'w') as file:
			json.dump(data, file)

		with open("roommatedatabase.json", "r") as file:
			file_contents = json.load(file)
			ref.set(file_contents)

		return dictionary


	def green_flags(points):
		category = 0
		importance = 100
		while category != 9:
			importance -= 1
			print('Time to establish your green flags! What traits are you looking for in a roommate? Make your selections in order from most important to least important.')
			print('~~~~~~~~~~~~~~~~~~~~')
			print('(1) Age')
			print('(2) Gender')
			print('(3) Religion')
			print('(4) Political party')
			print('(5) Moral alignment')
			print('(6) Times awake')
			print('(7) Sociality')
			print('(8) Interests')
			print('(9) Done')
			category = int(input('> '))

			if category == 1:
				print('Which would you prefer your roommate to be:')
				print('(1) Older')
				print('(2) Younger')
				print('(3) Same age')
				choice = int(input('> '))

				if choice == 1:
					points['isOlder'] += importance

				if choice == 2:
					points['isYounger'] += importance

				if choice == 3:
					points['isSameAge'] += importance

			if category == 2:
				print('Which would you prefer your roommate to be:')
				print('(1) Male')
				print('(2) Female')
				print('(3) Other')
				choice = int(input('> '))

				if choice == 1:
					points['isMale'] += importance

				if choice == 2:
					points['isFemale'] += importance

				if choice == 3:
					points['isOtherGender'] += importance

			if category == 3:
				print('Which would you prefer your roommate to be:')
				print('(1) Christian')
				print('(2) Jewish')
				print('(3) Muslim')
				print('(4) Hindu')
				print('(5) Buddhist')
				print('(6) Secular')
				print('(7) Other')
				choice = int(input('> '))

				if choice == 1:
					points['isChristian'] += importance

				if choice == 2:
					points['isJewish'] += importance

				if choice == 3:
					points['isMuslim'] += importance

				if choice == 4:
					points['isHindu'] += importance

				if choice == 5:
					points['isBuddhist'] += importance

				if choice == 6:
					points['isSecular'] += importance

				if choice == 7:
					points['isOtherReligion'] += importance

			if category == 4:
				print('Which would you prefer your roommate to be:')
				print('(1) Republican')
				print('(2) Democrat')
				print('(3) Socialist')
				print('(4) Green')
				print('(5) Other')
				choice = int(input('> '))

				if choice == 1:
					points['isRepublican'] += importance

				if choice == 2:
					points['isDemocrat'] += importance

				if choice == 3:
					points['isSocialist'] += importance

				if choice == 4:
					points['isGreen'] += importance

				if choice == 5:
					points['isOtherParty'] += importance

			if category == 5:
				print('Which would you prefer your roommate to be:')
				print('(1) Progressive')
				print('(2) Conservative')
				choice = int(input('> '))

				if choice == 1:
					points['isProgressive'] += importance

				if choice == 2:
					points['isConservative'] += importance

			if category == 6:
				print('Which would you prefer your roommate to be:')
				print('(1) Early Bird')
				print('(2) Night Owl')
				choice = int(input('> '))

				if choice == 1:
					points['isEarlyBird'] += importance

				if choice == 2:
					points['isNightOwl'] += importance

			if category == 7:
				print('Which would you prefer your roommate to be:')
				print('(1) Not social')
				print('(2) A little social')
				print('(3) Very social')
				choice = int(input('> '))

				if choice == 1:
					points['isNotSocial'] += importance

				if choice == 2:
					points['isLittleSocial'] += importance

				if choice == 3:
					points['isSocial'] += importance

			if category == 8:
				print('Which interest do you want your roommate to have:')
				choice = input('> ').lower()
				interests = points['isInterest']
				interests[choice] = importance
				points['isInterest'] = interests
	

	def red_flags(points):
		category = 0
		importance = 100
		while category != 9:
			importance -= 1
			print("Now it's time to establish your red flags! What traits are you looking to avoid in a roommate? Make your selections in order from most important to least important.")
			print('~~~~~~~~~~~~~~~~~~~~')
			print('(1) Age')
			print('(2) Gender')
			print('(3) Religion')
			print('(4) Political party')
			print('(5) Moral alignment')
			print('(6) Times awake')
			print('(7) Sociality')
			print('(8) Interests')
			print('(9) Done')
			category = int(input('> '))

			if category == 1:
				print('Which would you prefer your roommate not to be:')
				print('(1) Older')
				print('(2) Younger')
				print('(3) Same age')
				choice = int(input('> '))

				if choice == 1:
					points['isOlder'] -= importance

				if choice == 2:
					points['isYounger'] -= importance

				if choice == 3:
					points['isSameAge'] -= importance

			if category == 2:
				print('Which would you prefer your roommate not to be:')
				print('(1) Male')
				print('(2) Female')
				print('(3) Other')
				choice = int(input('> '))

				if choice == 1:
					points['isMale'] -= importance

				if choice == 2:
					points['isFemale'] -= importance

				if choice == 3:
					points['isOtherGender'] -= importance

			if category == 3:
				print('Which would you prefer your roommate not to be:')
				print('(1) Christian')
				print('(2) Jewish')
				print('(3) Muslim')
				print('(4) Hindu')
				print('(5) Buddhist')
				print('(6) Secular')
				print('(7) Other')
				choice = int(input('> '))

				if choice == 1:
					points['isChristian'] -= importance

				if choice == 2:
					points['isJewish'] -= importance

				if choice == 3:
					points['isMuslim'] -= importance

				if choice == 4:
					points['isHindu'] -= importance

				if choice == 5:
					points['isBuddhist'] -= importance

				if choice == 6:
					points['isSecular'] -= importance

				if choice == 7:
					points['isOtherReligion'] -= importance

			if category == 4:
				print('Which would you prefer your roommate not to be:')
				print('(1) Republican')
				print('(2) Democrat')
				print('(3) Socialist')
				print('(4) Green')
				print('(5) Other')
				choice = int(input('> '))

				if choice == 1:
					points['isRepublican'] -= importance

				if choice == 2:
					points['isDemocrat'] -= importance

				if choice == 3:
					points['isSocialist'] -= importance

				if choice == 4:
					points['isGreen'] -= importance

				if choice == 5:
					points['isOtherParty'] -= importance

			if category == 5:
				print('Which would you prefer your roommate not to be:')
				print('(1) Progressive')
				print('(2) Conservative')
				choice = int(input('> '))

				if choice == 1:
					points['isProgressive'] -= importance

				if choice == 2:
					points['isConservative'] -= importance

			if category == 6:
				print('Which would you prefer your roommate not to be:')
				print('(1) Early Bird')
				print('(2) Night Owl')
				choice = int(input('> '))

				if choice == 1:
					points['isEarlyBird'] -= importance

				if choice == 2:
					points['isNightOwl'] -= importance

			if category == 7:
				print('Which would you prefer your roommate not to be:')
				print('(1) Not social')
				print('(2) A little social')
				print('(3) Very social')
				choice = int(input('> '))

				if choice == 1:
					points['isNotSocial'] -= importance

				if choice == 2:
					points['isLittleSocial'] -= importance

				if choice == 3:
					points['isSocial'] -= importance

			if category == 8:
				print('Which interest do you not want your roommate to have:')
				choice = input('> ').lower()
				interests = points['isInterest']
				interests[choice] = 0 - importance
				points['isInterest'] = interests


	def search(dictionary, key):
		matchScore = 0
		highScore = -1000
		bestMatch = 'null'
		with open('roommatedatabase.json', "r") as file:
			data = json.load(file)
			for entry in data:
				matchScore = 0
				entry = data[entry]
				if entry['name'] != key['name']:
					if entry['age'] > key['age']:
						matchScore += points['isOlder']
					if entry['age'] < key['age']:
						matchScore += points['isYounger']
					if entry['age'] == key['age']:
						matchScore += points['isSameAge']
					if entry['gender'] == 'm':
						matchScore += points['isMale']
					if entry['gender'] == 'f':
						matchScore += points['isFemale']
					if entry['gender'] == 'o':
						matchScore += points['isOtherGender']
					if entry['religion'] == 1:
						matchScore += points['isChristian']
					if entry['religion'] == 2:
						matchScore += points['isJewish']
					if entry['religion'] == 3:
						matchScore += points['isMuslim']
					if entry['religion'] == 4:
						matchScore += points['isHindu']
					if entry['religion'] == 5:
						matchScore += points['isBuddhist']
					if entry['religion'] == 6:
						matchScore += points['isSecular']
					if entry['religion'] == 7:
						matchScore += points['isOtherReligion']
					if entry['politic'] == 1:
						matchScore += points['isRepublican']
					if entry['politic'] == 2:
						matchScore += points['isDemocrat']
					if entry['politic'] == 3:
						matchScore += points['isSocialist']
					if entry['politic'] == 4:
						matchScore += points['isGreen']
					if entry['politic'] == 5:
						matchScore += points['isOtherParty']
					if entry['alignment'] == 1:
						matchScore += points['isProgressive']
					if entry['alignment'] == 2:
						matchScore += points['isConservative']
					if entry['time'] == 1:
						matchScore += points['isEarlyBird']
					if entry['time'] == 2:
						matchScore += points['isNightOwl']
					if entry['social'] == 1:
						matchScore += points['isNotSocial']
					if entry['social'] == 2:
						matchScore += points['isLittleSocial']
					if entry['social'] == 3:
						matchScore += points['isSocial']

					isInterest = points['isInterest']
					for interest in entry['interests']:
						if interest in isInterest:
								matchScore += isInterest[interest]
					
					if matchScore > highScore:
						highScore = matchScore
						bestMatch = entry['name']
						
		return bestMatch
	

	def results(name):
		print(f'Your best match is {name.title()}!')
	

	dictionary = interview(ref)
	key = list(dictionary.values())[0]
	green_flags(points)
	red_flags(points)
	results(search(dictionary, key))

main()