# Boot.Dev - Learn Python

## CH6: Computing

### Python Numbers

``` Python
def calculate_damage(sword, arrow, spear, dagger, fireball):
	total_damage = sword + arrow + spear + dagger + fireball
	average_damage = total_damage / 5
	return total_damage, average_damage
```


### Floor Division

	11 // 2 = 5
	-7 // 3 = -3


### Changing in Place

```Python
def update_player_score(current_score, increment):
	current_score = current_score + increment
	return current_score
```


### Plus Equals

```Python
def get_hurt(current_health, damage):
	current_health -= damage
	return current_health
```


### Scientific Notation

```Python
def max_players_on_server():
	small = 1.024e18
	medium = 1.024e19
	large = 1.024e20
	return small, medium, large
```


### Bitwise '&' Operator

```Python
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
	return user_permission & can_create_guild


def get_review_bits(user_permissions):
	return user_permissions & can_review_guild


def get_delete_bits(user_permissions):
	return user_permissions & can_delete_guild


def get_edit_bits(user_permissions):
	return user_permissions & can_edit_guild
```


### Bitwise "|" Operator

```Python
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
	return glorfindel | galadriel | elendil | elrond
```


### Damage Meter

```Python
def main():
	calculate_dps(8_000_000, 45)
	calculate_dps(10_000_000, 49)


def calculate_dps(damage, time):
	dps = damage / time
	print(f"Damage per second: {dps}")
	print("==================================")


main()
```


### Converting Binary

```Python
def binary_string_to_int(num_servers, num_players, num_admins):
	servers = int(num_servers, 2)
	players = int(num_players, 2)
	admins = int(num_admins, 2)
	return servers, players, admins
```





## CH7: Comparisons

### Comparison Operators

```Python
def player_2_wins(player_1_score, player_2_score):
	return player_1_score > player_2_score
```


```Python
def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
	is_mustang_edward_same = mustang_height == edward_height
	is_alphonse_edward_same = alphonse_height == edward_height
	is_winry_alphonse_same = winry_height == alphonse_height
	return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same
```


### If Statements

```Python 
def show_status(boss_health):
	if boss_health > 0:
		print("Gandorf is alive!")
		return
	print("Gandorf is unalive!")


def print_status(player_health):
	if player_health <= 0:
		print("dead")
	print("status check complete")


def check_swords_for_army(number_of_swords, number_of_soldiers):
	if number_of_swords == number_of_soldiers:
		return "correct amount"
	return "incorrect amount"
```


### If-Else

```Python
if score > high_score:
	print("High score beat!")
elif score > second_highest_score:
	print("You got second place!")
elif score > third_highest_score:
	print("You got third place!")
else:
	print("Better luck next time")
```


```Python
def player_status(health):
	if health <= 0:
		return "dead"
	elif health <= 5:
		return "injured"
	else:
		return "healthy"
```


```Python
def check_high_score(current_player_name, high_scoring_player_name):
	if current_player_name == high_scoring_player_name:
		return "You are the highest scoring player!"
	else:
		return "You are not the highest scoring player!"
```


```Python
def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
	if player_name == high_scoring_player_name:
		return "high"
	elif player_name == low_scoring_player_name:
		return "low"
	else:
		return "neither"
```


### Boolean Logic

```Python
def does_attack_hit(attack_roll, armor_class):
	return (attack_roll != 1 and attack_roll >= armor_class) or attack_roll == 20
```


### Should Serve Drinks

```Python
def should_serve_customer(customer_age, on_break, time):
	return customer_age >= 21 and not on_break and 5 <= time <= 10
```


```Python
def should_serve_customer(customer_age, on_break, time):
	if customer_age >= 21:
		return False
	if on_break:
		return False
	if time < 5 or time > 10:
		return False
	return True
```


### Mount Rental

```Python
def check_mount_rental(time_used, time_purchased):
	if time_used >= time_purchased:
		return "overtime charged"
	return "no charges yet"
```


### Combat Advantage

```Python
def combat_evaluation(player_power, enemy_defense):
	advantage, disadvantage, evenly_matched = False, False, False

	if player_power > enemy_defense:
		advantage = True
	elif Player_power < enemy_defense:
		disadvantage = True
	else:
		evenly_matched = True
	
	return advantage, disadvantage, evenly_matched
```



