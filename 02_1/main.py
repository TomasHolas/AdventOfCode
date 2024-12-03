if __name__ == "__main__":
   result = 0

   with open("02_1/input.txt", 'r') as f:
      for report in f:
         level = list(map(int, report.split()))
         offset = 0
         safe = 0

         for x, y in zip(level, level[1:]):
            prev_offset = offset
            offset = y - x
            if 0 < abs(offset) < 4 and offset * prev_offset >= 0:
               safe += 1

         if safe == len(level) - 1:   
            result += 1
  
   print(result)