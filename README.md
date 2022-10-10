# multi-drone-quiz

## Question 1:

- Implemented the distance transform method from the [Distance Transforms of Sampled Functions](http://people.cs.uchicago.edu/~pff/papers/dt.pdf) paper.
- The distance transform calculates the distance of from each pixel to the nearest non-zero pixel in case of an image. In our case the colored squares are non-zero pixels.
- The algorithm is implemented in the following steps:
  - `get_dt()`: first calculates the lower evelope of parabolas in a vector (could be a row or column - see below points for clarification) and then calculates the distance tranform values for points in that vector which is nothing but the height of the lower envelope at that point. [as shown in the paper]
  - `calculate_distance_row()`: loops over every row and sends and gets its distance transform from `get_dt`
  - `calculate_distance_col()`: loops over every row and sends and gets its distance transform from `get_dt`
  - `esdf()`: initializes the grid with inf and creates 0 values in place of obstacles and calls the distance transform function for rows and columns.

<hr>

_N.B: Did not get time to properly think on other questions, following are the answers from the top of my head_

### Question 2:

- Assuming a n\*m\*k cuboid as the 3D space and dividing the space into unit cubes of 1\*1\*1
- Like in problem 1, as the obstacles are fixed. We can precompute the distance between every voxel (if you wanna call it that) to the obstacles (problem 1 in 3 dimensions)
- Now we just need to know the drone's location and we can find the disntance in O(1) with some precompute time.

### Question 3:

- Similar to question 2 but we can keep a max heap of size k for each drone (needs extra o(k) time for each drone just once)
- When drones if an obstacle is closer than the root of the max heap, pop out the root and pop in the new obstacle distance. (May not be the most efficient way as we need to check a number of obstalces in every movement)

_PS: This could be thought of nearest neighbours algorithm in Machine learning and probably could give a better solution using some datastructure made for such tasks_

### Question 4:

- We can use Oct Trees to spawn such boxes. ([Reference](https://gist.github.com/belzecue/fe247fbfc4f555137dd36e290e7ff5cb))
