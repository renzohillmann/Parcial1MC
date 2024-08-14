


def DECtoDMS(deg): #convertir grados a grados, minutos y segunndos

    min = (deg - int(deg))*60
    sec = (min - int(min))*60

    #print("el ángulo en el formato D M S es:", int(deg), "°", int(min), "mins", sec, "segs" )
    return {'degs' : int(deg), 'mins': abs(int(min)), 'secs': abs(sec)}

def DMStoDEC (deg, min, sec): #convert angle from degrees, mins and seconds to Degrees

    return deg + min/60 + sec/3600





def HMStoDEC (h, m, s): #convert hours minutes and seconds to decimal
    return h*15 + m/60*15 + s/3600*15


def DECtoHMS(angle): # Convert angle in degrees to hours
    
    total_hours = angle / 15.0
    
    # Extract hours
    hours = int(total_hours)
    
    # Extract minutes
    total_minutes = (total_hours - hours) * 60
    minutes = int(total_minutes)
    
    # Extract seconds
    total_seconds = (total_minutes - minutes) * 60
    seconds = total_seconds
    
    return {'hours' : hours, 'mins': minutes, 'secs': seconds}



def UAperDay_KMs(v):
    UA =  149597870.7 #km
    Day = 86400 #secs

    v = v*(UA/Day)

    return v


def UAperDay_MS(v):
    return UAperDay_KMs(v)*1000

def KMs_UAperDay(v):
    UA =  149597870.7 #km
    Day = 86400 #secs

    v = v*(Day/UA)
    return v
    


def UAtoM(x):
    UA =  149597870.7 #km
    
    return x*UA*1000




