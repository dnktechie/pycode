# Import necessary package to run function
import numpy as np
from mean_mm_to_in_arr import mean_mm_to_in_arr

# 2d array of average monthly precip (mm) for 2002 and 2013 in Boulder, CO
precip_2002_2013_mm = np.array([[27.178, 11.176, 38.1, 5.08, 81.28, 29.972, 2.286, 36.576, 38.608, 61.976, 19.812, 0.508], [6.858, 28.702, 43.688, 105.156, 67.564, 15.494,26.162, 35.56 , 461.264, 56.896, 7.366, 12.7]
                               ])
# Calculate monthly mean (inches) for precip_2002_2013
monthly_mean_in = mean_mm_to_in_arr(arr_mm = precip_2002_2013_mm, axis_value = 0)

monthly_mean_in
##array([0.67 , 0.785, 1.61 , 2.17 , 2.93 , 0.895, 0.56 , 1.42 , 9.84 ,2.34 , 0.535, 0.26 ])

print(monthly_mean_in)