nric = input('Enter an NRIC number: ')

# Type your code below

check = 'invalid'
weight = [2,7,6,5,4,3,2]
Grp1 = ["J","Z","I","H","G","F","E","D","C","B","A"]
Grp2 = ["X","W","U","T","R","Q","P","N","M","L","K"]
nric = nric.upper()
letter = ["S","T","F","G"]
if len(nric) == 9:
  if nric[0] in letter:
    a = nric[0]
    if (nric[8]).isalpha:
      b = nric[8]
      new = nric[1:8]
      sum = (int(new[0]) * weight[0]) + (int(new[1]) * weight[1]) + (int(new[2]) * weight[2]) + (int(new[3]) * weight[3]) + (int(new[4]) * weight[4]) + (int(new[5]) * weight[5]) + (int(new[6]) * weight[6])
      if a == "T" or a == "G":
        sum += 4
      r = (sum % 11) 
      if a == "T" or a == "S":
        digit = Grp1[r]
      else:
        digit = Grp2[r]
      if b == digit:
        check = "valid"

print("NRIC is {}.".format(check))