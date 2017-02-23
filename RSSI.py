def motor_southwest():
    print("south west")
def motor_southeast():
    print("south east")
def motor_northeast():
    print("north east")  
def motor_northwest():
    print("north west")
def motor_north():
    print("north")
def motor_west():
    print("west")
def motor_south():
    print("south")
def motor_east():
    print("east")
    
other_buoy=[-2,-2]
#for i in range(2):
#    other_buoy[i]=float(input("coordinates of the buoy which is close"))

my_buoy=[1,-1]
mod_x=other_buoy[0]-my_buoy[0]
mod_y=other_buoy[1]-my_buoy[1]


if mod_y>0 and mod_x>0:
    motor_southwest()
if mod_y>0 and mod_x<0:
    motor_southeast()
if mod_y<0 and mod_x<0:
    motor_northeast()
if mod_y<0 and mod_x>0:
    motor_northwest()
if mod_y==0 and mod_x>0:
    motor_west()
if mod_y==0 and mod_x<0:
    motor_east()
if mod_y>0 and mod_x==0:
    motor_south()
if mod_y<0 and mod_x==0:
    motor_north()
    
