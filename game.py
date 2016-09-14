inventory = []

def die():
	print "Sorry, please try again"
	exit(0)
	
def left_fork():

	while True:
		print "After traveling for several miles you come to a deep chasm cutting across the road. To the left, along a cliff, is a small dark path. Do you try to jump over the chasm or follow the path along the cliff?"
		choice = raw_input(">")
	
		if "jump" in choice:
			print "You take a running start and attempt to leap across the chasm. You see the other side coming closer and closer but realize too late that you are losing too much height. Your fingers scrape the far wall of the chasm inches below the surface and you fall screaming into the abyss"
			die()
		elif "path" in choice:
			print "You follow the narrow path along the cliff's edge to your left. After a while, you can no longer see anything but chasm and cliff in either direction. You hear a low growl close behind you, too close, and you turn just in time to see the cougar's claws heading for your eyes."
			die ()
		else:
			print "You can't do that. You must choose to either jump or take the path to your left"

def dock():
	
	while True:
	
		print "You come to a dock on a large river. There is a speedboat making a funny noise and a canoe without oars. You can take the boat, the canoe, or turn around"
		choice = raw_input(">")
		
		if "boat" in choice:
			print "You get in the boat and shift into drive. Apparently the boat has an electrical short and has been leaking gas. As soon as you press the accelerator, the boat explodes"
			die()
		elif "canoe" in choice and not "oars" in inventory:
			print "You get in the canoe but have nothing to row with. The current pulls you mercilessly downstream, back to the zombie-ridden wasteland you barely escaped in the first place"
			die()
		elif "canoe" in choice and "oars" in inventory:
			print "You take out your oars and travel by canoe upstream, away from the city you must leave behind"
			cave_dock()
		elif choice == "turn around":
			start()
		else:
			print "You can't do that. You must choose: boat, canoe, or turn around"
			
def fountain():
	print "The road cuts through a dense and quiet forest. You come to a beautiful fountain, marking a place where the road forks to the left and to the right. A bunch of bananas and a knife lay forgotten in front of the fountain. You can go left, right, or go back."
	
	while True: 
		choice = raw_input(">")
		
		if "bananas" in choice:
			print "You know you can't eat wild fruits in these unsafe times, but you put the bananas in your sack anyways. Who knows? They could come in handy."
			inventory.append("bananas")
		elif "knife" in choice:
			print "You place the knife in your sack"
			inventory.append("knife")
		elif "left" in choice:
			forest()
		elif "right" in choice:
			shed()
		elif "back" in choice:
			start()
		else:
			print "You can't do that"

def shed():
	print "You come upon a dilapidated old shed overlooking a large river. There is a steep dropoff down to the water and you know you won't be able to get to the water here, not that there's a boat anyways. You look around inside the shed and find a fishing rod, a tent, oars, and a can of coffee. There is no way forward from here."
	
	while True:
		choice = raw_input(">")
		
		if "fishing" in choice:
			print "You examine the fishing rod and find it is snapped in half. You toss the useless thing away"
		elif "tent" in choice:
			print "You place the tent in your sack"
			inventory.append("tent")
		elif "oars" in choice:
			print "You tie your rucksack to the oars and carry the bundle over your shoulder"
			inventory.append("oars")
		elif "coffee" in choice or "can" in choice:
			print "You pick up the coffee can and find a large hole in the bottom - no need to take this along. You put the can back down"
		elif "back" in choice:
			fountain()
		else:
			print "You can't do that"

def forest():
	print "You continue through the forest until the road turns into a footpath and becomes difficult to follow. It is clear that people do not come here often. The path curves to the right but disappears into what seems to be a large rabbit den. A large tree with good branches for climbing blocks you from going straight. Pieces of tree bark lay at your feet, they smell like cinnamon."
	
	while True:
		choice = raw_input(">")
	
		if "climb" in choice:
			monkey()
		elif "path" in choice or "rabbit" in choice or "den" in choice:
			tunnel()
		elif "bark" in choice:
			print "Yummy cinnamon! You place the pieces of cinnamon bark in your sack"
			inventory.append("bark")
		else:
			print "You can't do that"

def monkey():
	print "You climb the tree easily and nimbly, halfway up you find a more nimble climber than you. A monkey is perched among the branches, watching you suspiciously, he appears to be guarding an inflatable raft"
	monkey_friend = False
	
	while True:
		choice = raw_input(">")
		
		if "bananas" in choice and "bananas" in inventory:
			print "The monkey takes the bananas happily and tells you his name is George. After chatting with you for a while, he assures you it is safe to follow the path into the rabbit's den"
			inventory.remove("bananas")
			monkey_friend = True
		elif "bananas" in choice and "bananas" not in inventory:
			print "The monkey is angered by your false offer of yummy bananas. He suspects you are trying to trick him into a life of a street performer. The monkey knocks you off the tree and leaves you for dead."
			die()
		elif "raft" in choice and not monkey_friend:
			print "The monkey sees you as a threat to his territory and his prized raft. He knocks you off the tree and leaves you for dead"
			die()
		elif "raft" in choice and monkey_friend:
			print "George offers you his raft and his lifelong friendship. He suggests you get going on your quest to find your family, it will be dark soon"
			inventory.append("raft")
		elif "go" in choice:
			print "Tired of spending time perched in a tree, you climb down and continue along the path into the rabbit's den"
			tunnel()
		else:
			print "You can't do that"
			
def tunnel():
	print "You enter the rabbit's den and see that it is warmly lighted by wall sconces. Someone must have lived here but it seems empty for now. You follow the long tunnel until you come to a cave whose mouth is the top of a waterfall. Do you get in the water or go back?"
	
	while True: 
		choice = raw_input(">")
	
		if "water" in choice and "raft" in inventory:
			print "The raft takes you safely down the waterfall into a large river"
			if "oars" in inventory:
				print "You take out your oars and travel by raft upstream, away from the city you must leave behind"
				cave_dock()
			elif "oars" not in inventory:
				print "Unfortunately you have nothing to row with and the current pulls you mercilessly downstream, back to the zombie-ridden wasteland you barely escaped in the first place"
				die()
		elif "water" in choice and "raft" not in inventory:
			print "You try to swim down the waterfall but it is too steep and the water at the bottom too shallow. You don't make it."
			die()
		elif "back" in choice:
			print "The large, apparently carnivorous, rabbit returns and roasts you for supper"
			die()
		else:
			print "You can't do that"

def cave_dock():
	print "You row yourself up the river for what seems like hours, but is actually only 30 minutes. You see a great mountain up ahead, the river appears to flow from a cave in the mountain. /n/nAs you enter the cave, you see a broken down, abandoned dock to your left. You think you can dock there if you act quickly, but you don't know if there is a more sturdy structure to land on further up the river. Do you dock here or keep going?"
	
	choice = raw_input(">")
	
	if "dock" in choice:
		print "You catch ahold of the pier and pull yourself up onto the dock. It is sturdier than it looks!"
		mine_cart()
	elif "going" in choice:
		print "You travel on into the darkness. After some time you hear a whooshing sound and find that you've been drawn into a whirlpool. You search frantically for a way out but it's too late"
		die()
	else:
		print "You took too long to decide and missed the dock. No choice but to keep going now. You travel on into the darkness. After some time you hear a whooshing sound and find that you've been drawn into a whirlpool. You search frantically for a way out but it's too late"
		die()

def mine_cart():
	print "You follow the dock and come upon a small mineyard. An abandoned cart lay upon one set of the tracks down into the mountain. You don't see any other options so you jump in the cart and hope for the best as it rattles along the tracks, deeper and deeper into the mountain. You come to a stop at a small platform, you can see that the tracks go further ahead and there seems to be a light coming from that direction. Do you stop here and look around? Or do you go ahead?"
	
	while True: 
		choice = raw_input(">")

		if "stop" in choice or "look" in choice:
			beaver()
		elif "go" in choice or "going" in choice:
			mole_people()
		else:
			print "You can't do that"

def beaver():
	print "You get out of the cart and look around. Suddenly, you hear a large clatter behind you and find that a large beaver has sent your cart careening into the darkness, there's no escaping now! A pair of large beavers grabs hold of you and carries you through a tunnel to the Beaver Overlord. The Beaver Overlord asks what you are doing here:"
	
	choice = raw_input(">")
	
	if ("bark" in choice or "cinnamon" in choice) and "bark" in inventory:
		print "The Beaver Overlord is pleased with your offering. He has not had cinnamon bark in many years and is pleased by the delicacy you have brought him. He offers you a ship and crew to reunite you with your family"
		exit(0)
	elif "knife" in choice and "knife" in inventory:
		print "You try to fight the Beaver Overlord off with your knife. He's too quick for you and fall quickly - he didn't get to be Beaver Overlord because of his looks, you know."
		die()
	else:
		print "The Beaver Overlord is amused by your foolish attempts at escape. He enslaves you and brings you out to entertain his beaver army at feasts"
		die()
		
def mole_people():
	print "You continue in your cart to another platform. This appears to be the end of the line. You can't believe your eyes, but there appears to be an exit from the mountain a few hundred yards away - and a Tesla parked at the mouth of the cave!! As you exit the cart to go to the car, you hear squeaking noises and see an army of Mole People climbing up from the cavern on the other side of the tracks. Do you run to the car or try to fight them off?"
	
	choice = raw_input(">")
	
	if "run" in choice:
		print "You made it! The keys are inside the car and it has a full battery. You floor it and are at 60mph in under 3 seconds, the Mole People are far behind you and you are headed to your family at last"
		exit(0)
	elif "fight" in choice:
		print "You are overrun by Mole People and they drag you screaming away from your new Tesla and your waiting family"
		die()
	else:
		print "You reacted too slowly and the Mole People have caught you, there's no escaping now"
		die()







def start():
	print "You are on the road with the ruined city behind you. You really need to find a car, preferably something electric that can take you the 200 miles to your family. There is an intersection ahead. Do you go straight, right, or left?"
	choice = raw_input(">")

	if "left" in choice:
		left_fork()
	elif "right" in choice:
		dock()
	elif "straight" in choice:
		fountain()
	else: 
		print "Your indecision costs you dearly - the zombies from the city you narrowly escaped catch up with you and add you to their numbers."
		die()	
		
start()
	