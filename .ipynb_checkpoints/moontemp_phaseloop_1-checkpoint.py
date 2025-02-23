import sys
import os
import math


#Model Constants
delta_phase = 0.05                #Phase increment in degrees

lunation_count = 16              #number of lunations

#set up the output array
#AA =[[0 for col in range(1)]for row in range (30)]

#set up output file
fname = "moontemp_phaseloop.csv"
opfile=open(fname,'w')

#############################################################################################
def soilstack(LTK, phase, delta_phase):
#Physical Constants
  pi      = 3.1415926536           #pi
  sigma   = 5.67e-8                #Stefan's Constant
  BasCond = 1.50e3                 #Basalt conductivity in W.m-3.K-1
  BasCap  = 670.0                  #Basalt thermal capacity in J Kg-1.K-1  
  rho     = 1500.0                 #Lunar regolith density in Kg.m-3
  a       = 0.15                   #Lunar albedo
  I00     = 1365.0                 #Solar irradiance in W.m-2 
  I0      = (1 - a)*I00            #Solar energy absorbed by the lunar surface
  T_mean  = 225.0                  #Mean lunar soil temperature in Kelvins
 
  lunation = ((29*24 + 12)*60 + 44)*60
  delta_t        = delta_phase * lunation/360   #time step in seconds
  A = 1.0                          #surface area of element (square metres)
  delta_z = 0.01                   #thickness of element (metres)
  m = A * delta_z * rho            #mass of element
  RF_Absorption_Coeff =  1    #0.4        # RF Transmission Coefficient 

#Shorthand constants for model
  beta = 0.15         #BasCond * A/delta_z         #conductivity parameter
  gamma = 10050 #BasCap * m                 #thermal capacity parameter
  alpha = math.exp(-RF_Absorption_Coeff*delta_z) # RF Transmission Coefficient

  za = phase - 180                  #zenith angle of sun 
  if za<0: za = -za
  if za > 90:
   I = 0
  else:
   I = I0*math.cos(za/57.29) 
   
  j = 0
  while j < 29:
      if j==0: 
        LTK[j] =  LTK[j] + (A*(I - sigma*LTK[j]**4) + (LTK[j+1] - LTK[j])*beta)*delta_t/gamma        
      else:
        LTK[j] = LTK[j] + ((LTK[j+1]-LTK[j])*beta + (LTK[j-1] - LTK[j])*beta)*delta_t/gamma 
      j = j + 1

  Tb = 225
  k = 29
  #radio brightness temperature
  while k >= 0:
    Tb = alpha*Tb + (1- alpha)*LTK[k]
    k = k - 1
  LTK[30] = Tb 
  return LTK  


#############################################################################################

#set all the array temperatures to T_mean

#There are 30 soil temperature values (LTK[0] to LTK[29], initialized to 225.0K. The last (LTK[30] is the radio brightness temperature 
LTK = [
225.0, 225.0, 225.0, 225.0, 225.0,
225.0, 225.0, 225.0, 225.0, 225.0,
225.0, 225.0, 225.0, 225.0, 225.0,
225.0, 225.0, 225.0, 225.0, 225.0,
225.0, 225.0, 225.0, 225.0, 225.0,
225.0, 225.0, 225.0, 225.0, 225.0,
225.0]


####################################################################################

lc = 0
while lc < lunation_count:      #counting the lunations
  phase = 0.0
  while phase <=360:

    LTK = soilstack(LTK, phase, delta_phase)   
    phase = phase + delta_phase

    T00 = str(0.1*int(10*LTK[0]))
    T01 = str(0.1*int(10*LTK[1]))
    T02 = str(0.1*int(10*LTK[2]))
    T03 = str(0.1*int(10*LTK[3]))
    T04 = str(0.1*int(10*LTK[4]))
    T05 = str(0.1*int(10*LTK[5]))
    T06 = str(0.1*int(10*LTK[6]))
    T07 = str(0.1*int(10*LTK[7]))
    T08 = str(0.1*int(10*LTK[8]))
    T09 = str(0.1*int(10*LTK[9]))
    T10 = str(0.1*int(10*LTK[10]))
    T11 = str(0.1*int(10*LTK[11]))
    T12 = str(0.1*int(10*LTK[12]))
    T13 = str(0.1*int(10*LTK[13]))
    T14 = str(0.1*int(10*LTK[14]))
    T15 = str(0.1*int(10*LTK[15]))
    T16 = str(0.1*int(10*LTK[16]))
    T17 = str(0.1*int(10*LTK[17]))
    T18 = str(0.1*int(10*LTK[18]))
    T19 = str(0.1*int(10*LTK[19]))
    T20 = str(0.1*int(10*LTK[20]))
    T21 = str(0.1*int(10*LTK[21]))
    T22 = str(0.1*int(10*LTK[22]))
    T23 = str(0.1*int(10*LTK[23]))
    T24 = str(0.1*int(10*LTK[24]))
    T25 = str(0.1*int(10*LTK[25]))
    T26 = str(0.1*int(10*LTK[26]))
    T27 = str(0.1*int(10*LTK[27]))
    T28 = str(0.1*int(10*LTK[28]))
    T29 = str(0.1*int(10*LTK[29]))
    T30 = str(0.1*int(10*LTK[30]))   #This one is the radio brightness temperature

    if lc>14:
       opstring = str(lc)+", "+str(phase)+", "+ T00+", "+T01+", "+T02+", "+T03+", "+T04+", "+ T05+", "+T06+", "+T07+", "+T08+", "+T09+", "+T10+", "+T11+", "+T12+", "+T13+", "+T14+", "+T15+", "+T16+", "+T17+", "+T18+", "+T19+", "+T20+", "+T21+", "+T22+", "+T23+", "+T24+", "+T25+", "+T26+", "+T27+", "+T28+", "+T29+", "+T30
 
       print opstring
       opfile.write(opstring + "\n")
 
  lc = lc + 1
print "Done"    
opfile.close

