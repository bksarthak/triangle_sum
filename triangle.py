import sys

def calc_max_sum(filename):
#open file,set default start key, sum=0 and dictionary
  file_open = open(filename,'r')
  key = 1
  dict = {}
  sum = 0 
#start a loop to create a dictionary with key as the line number and set of numbers in each line being the values
  for lines in file_open:
   values = lines.split()
   dict[key]= values
   key = key + 1
#loop through the created dictionary to find the maximum of each line and cumulatively adding to find the final sum
  for keys in dict:
   line_max = max(map(int,dict.get(keys)))
   sum = sum + line_max
  print sum

def main():
 if len(sys.argv) != 2:
    print 'usage: ./triangle.py file-to-read'
    sys.exit(1)
 calc_max_sum(sys.argv[1])
 
if __name__=='__main__':
 main()
