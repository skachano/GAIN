'''Main function for UCI letter and spam datasets.
'''

# Necessary packages
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import numpy as np

from gain import gain
from utils import rmse_loss

def data_replace(data_path):
  data_x =  np.loadtxt(data_path,delimiter=',')
  data_x = np.reshape(data_x[:,1:37],(-1,18,2))
  for i in range(len(data_x)):
    for j in range(18):
      if data_x[i,j,0]==float(1000) and data_x[i,j,1]==float(-9999):
          data_x[i,j,:]=[np.nan,np.nan]
  data_x = np.reshape(data_x,(-1,36))
  return data_x

def main (args):
  '''Main function for UCI letter and spam datasets.
  
  Args:
    - data_name: letter or spam
    - miss_rate: probability of missing components
    - batch:size: batch size
    - hint_rate: hint rate
    - alpha: hyperparameter
    - iterations: iterations
    
  Returns:
    - imputed_data_x: imputed data
    - rmse: Root Mean Squared Error
  '''
  
  data_path = args.data_path
  output_path = args.output_path
  
  gain_parameters = {'batch_size': args.batch_size,
                     'hint_rate': args.hint_rate,
                     'alpha': args.alpha,
                     'iterations': args.iterations}
  
  # Load data and replace missingness to nan
  miss_data_x = data_replace(data_path)
  
  # Impute missing data
  imputed_data_x = gain(miss_data_x, gain_parameters)

  np.savetxt(output_path,imputed_data_x,delimiter=',')
  
  # # Report the RMSE performance
  # rmse = rmse_loss (ori_data_x, imputed_data_x, data_m)
  
  # print()
  # print('RMSE Performance: ' + str(np.round(rmse, 4)))
  return imputed_data_x

if __name__ == '__main__':  
  
  # Inputs for the main function
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--data_path',
      type=str)
  parser.add_argument(
      '--output_path',
      type=str)
  parser.add_argument(
      '--batch_size',
      help='the number of samples in mini-batch',
      default=128,
      type=int)
  parser.add_argument(
      '--hint_rate',
      help='hint probability',
      default=0.9,
      type=float)
  parser.add_argument(
      '--alpha',
      help='hyperparameter',
      default=100,
      type=float)
  parser.add_argument(
      '--iterations',
      help='number of training interations',
      default=10000,
      type=int)
  
  args = parser.parse_args() 
  
  # Calls main function  
  imputed_data = main(args)
