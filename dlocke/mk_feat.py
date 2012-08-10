#Copyright David Locke, 2012

from augustus.kernel.unitable import *

def main():
  
  a = UniTable().from_csv_file('../Data/train_rel_2.tsv')
  print a.summary()
  
  #Feature #1 Count of double letters used in the essay.
  #Feature #2 Number of spaces in the essay
  #Feature #3 Length of the essay
  #Feature #4 Ratio of double letters to length
  #Feature #5 Ratio of spaces to length
  
  #Initialize the new columns
  a['DblLtrCnt'] = [0] * len(a)
  a['SpaceCnt'] = [0] * len(a)
  a['Length'] = [0] * len(a)
  a['DblLtrRatio'] = [0.0] * len(a)
  a['SpaceRatio'] = [0.0] * len(a)
  
  for x in a:
    #print x['EssayText']
    dbl_ltr_cnt = 0
    space_cnt = 0
    length = len(x['EssayText'])
    
    for i in xrange(0, len(x['EssayText']) - 1):
      if x['EssayText'][i].isalpha():
        if x['EssayText'][i] == x['EssayText'][i + 1]:
          dbl_ltr_cnt += 1
      
      if x['EssayText'][i] == " ":
        space_cnt += 1
    
    #print dbl_ltr_cnt, x['Score1']
    #if dbl_ltr_cnt >= 10:
    #  print x['EssayText']
    
    x['DblLtrCnt'] = dbl_ltr_cnt
    x['SpaceCnt'] = space_cnt
    x['Length'] = length
    x['DblLtrRatio'] = dbl_ltr_cnt / float(length)
    x['SpaceRatio'] = space_cnt / float(length)
  
  #I can't quite figure out how to output this field correctly, for now just remove it from the output
  del a['EssayText']
  
  for i, tbl in a.subtbl_groupby('EssaySet'):
    tbl.to_csv_file('train_%d.csv' % i, sep=",")
    

if __name__ == "__main__":
  main()
