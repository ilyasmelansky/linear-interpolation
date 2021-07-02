
# This class provides methonds for filling in data between known [x,y] points using linear interpolation.

# method interp_x returns an [x,y] point at a desired x which lies between two given [x,y] points

# method interp_nSpaced returns a list of n number of [x,y] points that are evenly spaced between two given [x,y] points


class linear_interpolation: 

    # takes two points [x,y] and calculates the y value for any given x using linear interpolation, then returns the new [x,y] point
    # given points must be in ascending x values
    # x value must be between the two given points
   
    def interp_x(self,x_new, point1, point2):


        # checks that given points are in ascending order
        if point1[0] > point2[0]:               
            print("coordinates not in ascending order")

        # checks that desired x is between the two givne points
        if  x_new < point1[0] or x_new > point2[0]:        
            print("target x coordinate outside of scope")

        else:
            x_left = point1[0]
            x_right = point2[0]
            y_left = point1[1]
            y_right = point2[1]

            slope = (y_right - y_left)/(x_right - x_left)
            intercept = y_left - slope * x_left
            y_new = slope * x_new + intercept # y = mx + b


            return [x_new,y_new]


    # calculates n-number of evenly spaced points between two given [x,y] points
    # number of desired points must be a positive whole number greater than 0
    # returns evenly spaced points as a list of [x,y] values
    def interp_nSpaced(self, n, point1, point2):

        #check that n is whole number greater than 0
        if n < 1 or n - int(n) != 0   :
            print("n must be a positive interger greater than 0")

        else:

            # calculates the x-axis spacing of the desired points 
            spacing = (point2[0] - point1[0]) / ( n + 1 ) 
            
            # list of new x values to interpolate y values for
            x_new = []

            #adds the first x value to x_new
            x_new.append(point1[0]+spacing)


            
            #adds the rest of x values if n > 1
            for i in range(n - 1):
                x_new.append(x_new[-1] + spacing)


            new_points = []

            for i in x_new:
                new_points.append(self.interp_x(i,point1,point2))
          

        return new_points

           


# creates instance of linear_interpolation class and names it data
data = linear_interpolation()

# returns [x,y] values at x = 5 between points [1,1] and [10,10]
print(data.interp_x(5,[1,1],[10,10]))


# returns 8 evenly spaced [x,y] points between [10,10] and [100,100]
print(data.interp_nSpaced(8,[10,10],[100,100]))


