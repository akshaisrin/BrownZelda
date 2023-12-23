# Constants file to define final constants for our game

# Screen Width/Height:

screen_width=1550
screen_height=800

# x, y coordinates for move function
directions = {"left":(-12,0), "right":(12,0), "up":(0,-12), "down":(0,12)}

# x box controller mapping threshold

controller_threshold=0.15

# Medium Boss Velocity Constant

medium_boss_velocity_constant=50

# Medium boss x, y offsets for projectiles

medium_boss_projectile_offset_x=-100
medium_boss_projectile_offset_y=-100

# Projectile bounds for medium boss

med_boss_projectile_bounds=2

mini_boss_movement_vector={"left":(-3,0), "right":(3,0), "up":(0,-3), "down":(0,3)}

reg_patrol_constant=30
kohli_patrol_constant=17

reg_projectile_constant=15
kohli_projectile_constant=13

monster_player_collision_buffer_x=10
monster_player_collision_buffer_y=5

cooldown=50
kohli_speed=90
kohli_initial_cooldown=25