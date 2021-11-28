from django.shortcuts import render
from django.http import HttpResponse
from .models import ShootingLocation 
import json

def table (request) :
  shootings = ShootingLocation.objects.all()
  cnt_high, cnt_middle, cnt_low = 0, 0, 0
  num_head_neck, num_waist, num_left_leg, num_right_leg, num_left_arm, num_right_arm, num_left_chest, num_right_chest = 0, 0, 0, 0, 0, 0, 0, 0
  str = ''
 
  cumsum = ''
  for shooting in shootings :

    if shooting.position == None :
      pass
    elif shooting.position == '000' or shooting.position == '010' :
      cnt_high += 1
      if shooting.position == '000' : 
        num_head_neck += 1
      else :
        num_left_chest += 1

    elif shooting.position == '001' or shooting.position == '011':
      cnt_middle += 1
      if shooting.position == '001' :
        num_waist += 1
      else :
        num_right_chest += 1
    elif shooting.position == '101' or shooting.position == '100' or shooting.position == '111' or shooting.position == '110':
      cnt_low += 1
      if shooting.position == '101' :
        num_right_arm += 1
      elif shooting.position == '100' :
        num_left_arm += 1
      elif shooting.position == '111' : 
        num_right_leg += 1
      else :
        num_left_leg +=1 

    if cnt_high == 1 or cnt_middle >= 2 :
      str += "피해 정도 : 사망 <br>"
    elif cnt_middle == 1 or cnt_low >= 3 :
      str += "피해 정도 : 중상 <br>"
    elif cnt_high == 0 and cnt_middle == 0 and cnt_low < 3:
      str += "피해 정도 : 경상 <br>"
    else : 
      str += "피해 정도 : None <br>"
    result = str + "<br>* 최종 피해 정도 : " + str[-7:-4] + "\n"
    cumsum = "<누적 피해 횟수> <br><br>" + \
      "left_leg : {} 번 <br>".format(num_left_leg) + \
      "right_leg : {} 번 <br>".format(num_right_leg) + \
      "left_arm : {} 번 <br>".format(num_left_arm) + \
      "right_arm : {} 번 <br>".format(num_right_arm) + \
      "left_chest : {} 번 <br>".format(num_left_chest) + \
      "right_chest : {} 번 <br>".format(num_right_chest) + \
      "waist : {} 번 <br>".format(num_waist) + \
      "head_neck : {} 번 <br>".format(num_head_neck)
    
  return HttpResponse(cumsum + result)

def home (request) :
  shootings = ShootingLocation.objects.all()
  cnt_high, cnt_middle, cnt_low = 0, 0, 0
  num_head_neck, num_waist, num_left_leg, num_right_leg, num_left_arm, num_right_arm, num_left_chest, num_right_chest = 0, 0, 0, 0, 0, 0, 0, 0
  str = ''
  for shooting in shootings :
  
    if shooting.position == None :
      pass
    elif shooting.position == '000' or shooting.position == '010' :
      cnt_high += 1
      if shooting.position == '000' : 
        num_head_neck += 1
      else :
        num_left_chest += 1

    elif shooting.position == '001' or shooting.position == '011':
      cnt_middle += 1
      if shooting.position == '001' :
        num_waist += 1
      else :
        num_right_chest += 1
    elif shooting.position == '101' or shooting.position == '100' or shooting.position == '111' or shooting.position == '110':
      cnt_low += 1
      if shooting.position == '101' :
        num_right_arm += 1
      elif shooting.position == '100' :
        num_left_arm += 1
      elif shooting.position == '111' : 
        num_right_leg += 1
      else :
        num_left_leg +=1 

    if cnt_high >= 1 or cnt_middle >= 2 :
      str += "피해 정도 : 사망<br>"
    elif cnt_middle == 1 or cnt_low >= 3 :
      str += "피해 정도 : 중상<br>"
    elif cnt_high == 0 and cnt_middle == 0 and cnt_low < 3:
      str += "피해 정도 : 경상<br>"
    else : 
      str += "피해 정도 : None<br>"
    result = str[-7:-4]


    context = {
      "position" : shooting.position,
      "result" : result,
      "num_head_neck" : num_head_neck, 
      "num_waist" : num_waist, 
      "num_left_leg" : num_left_leg, 
      "num_right_leg" : num_right_leg, 
      "num_left_arm" : num_left_arm, 
      "num_right_arm" : num_right_arm, 
      "num_left_arm" : num_left_arm,
      "num_left_chest" : num_left_chest, 
      "num_right_chest" : num_right_chest
    }
    
  return render(request, 'home.html', context)