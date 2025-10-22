import numpy as np
def throw_rock (m, V0, theta):
    g = 9.81 #in m/s^2
    theta = theta*np.pi / 180 #in rad
    tf = 2*V0*np.sin(theta) / g #in s
    R = V0**2*np.sin(2*theta) / g #in m
    hm = V0**2*np.sin(theta)**2 / 2*g #in m
    Vh = V0*np.cos(theta) #in m/s
    Kh = 0.5*m*Vh*hm**2 #in J
    print ("For a rock with %5.3f kg mass thrown with %5.3f m/s at an angle of %6.2f degrees:\n"\
           "Time of flight is %10.1e s\nThe range in x-direction is %10.1e m\n"\
           "Maximum height is %10.1e m\nThe speed at maximum height is %10.1e m/s\n"\
           "Kinetic energy at the maximum height is %8.2e J" % (m, V0, theta*180 / np.pi, tf, R, hm, Vh, Kh))
    return (tf, R, hm, Vh, Kh)

     
        
    
    