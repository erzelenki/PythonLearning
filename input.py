hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
End_hour = (hour + (mins+dura) // 60) % 24
End_mins = (mins + dura) % 60
print ("End time : ", End_hour, ":",End_mins, sep="")
