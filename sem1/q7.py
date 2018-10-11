# Roll no.:
# Registration no.:
# Calculate position of projectile.

vi = float(input("Enter initial velocity: "))
yi = float(input("Enter initial height: "))
g = 9.8
total_time, n = 5, 50
dt = total_time / n
t = 0
fw = open("projectile.dat", "w")
while t < total_time:
	y = yi + vi*t - 0.5*g*t*t
	t += dt
	print(t, y, file=fw)
fw.close()

# EXECUTION
# Enter initial velocity: 100
# Enter initial height: 100