import random as rd

class Pokemon:

     def __init__(self, name, typ):
          self.name = name
          self.type = typ
          self.CP = 0
          self.stats = [0, 0, 0] ## [attack, defense, stamina] - max 15
          self.catch_rate = 0
          self.IV = 0
          self.captured = False

     def get_name(self):
          return self.name

     def get_type(self):
          return self.type

     def get_CP(self):
          return self.CP

     def get_stats(self):
          return self.stats

     def get_IV(self):
          return self.IV
     
     def get_catch_rate(self):
          return self.catch_rate
     
     def get_caught(self):
          return self.captured

     ##! modified this method to print the types properly
     def display_details(self):
          print("Name:\t",self.get_name())

          ##! here
          type1 = self.get_type()[0]
          type2 = self.get_type()[1]
          type_string = type1
          if type2 != "":
               type_string += f' / {type2}'
          print("Type:\t",type_string)

          print("CP:\t",self.get_CP())
          stats = self.get_stats()
          print("Attack:\t",stats[0])
          print("Defense:",stats[1])
          print("Stamina:",stats[2])
          print("IV:\t",self.get_IV())

     def set_CP(self, value):
          self.CP = value
          return self.CP

     def power_up(self, value):
          self.CP += value
          return self.CP

     def set_stats(self, attack, defense, stamina):
          if attack > 15 or defense > 15 or stamina > 15:
               print("Sorry, values cannot exceed 15.")
          else:
               self.stats = [attack, defense, stamina]
               self.IV = sum(self.stats)/45*100
          return self.IV
     
     def set_catch_rate(self):
          highest_stat = max(self.stats)
          lowest_stat = min(self.stats)
          scaled_stats = round(2 * ((7/8) * highest_stat + (1/8) * lowest_stat))
          unscaled_capture_rate = (100 * (scaled_stats/15)**3) + self.CP
          scaled_capture_rate = round(1 - (unscaled_capture_rate / 2300), 2)
          self.catch_rate = scaled_capture_rate

     def capture(self, pokeball, berry):
          pokeball_modifier = pokeball.get_modifier()
          berry_modifier = berry.get_modifier()
          rand_number = rd.random()
          modified_catch_rate = self.catch_rate ** (1/(pokeball_modifier * berry_modifier))

          if pokeball_modifier == 255:
               self.captured = True
          elif rand_number < modified_catch_rate:
               self.captured = True

          return self.captured
     
          
