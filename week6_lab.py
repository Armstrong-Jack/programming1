player_health = 100
def take_damage():
    # This 'player_health' is LOCAL, not the global one
    global player_health
    player_health -= 10
    print("Player took damage!")
    # Missing return statement
    # Function is called, but the new value is never returned or assigned

take_damage()
take_damage()
print(f"Player health is: {player_health}")
# Expected Output: Player health is: 80
# Actual Output: Player health is: 100