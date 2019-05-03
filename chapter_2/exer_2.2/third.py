d_f=float(input("distance travelled in first run"))
s_f=float(input("speed for first run"))
d_s=float(input("distance travelled in second run"))
s_s=float(input("speed for second run"))
total_time=(d_f/s_f) + (d_s/s_s)
print("total time = " , total_time)
time_in_minutes= total_time * 60
print("time in minutes  =  ",time_in_minutes)
time_reached_hours=int((((6*60) + 52 + time_in_minutes ) / 60 ))
time_reached_minutes_ini= ((6*60) + 52 + time_in_minutes ) % 60
print("time rached minutes in   =", time_reached_minutes_ini)
time_reached_minutes=int(time_reached_minutes_ini)
print("time_reached", time_reached_hours,":",time_reached_minutes)  
