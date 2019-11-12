import NumPy as np

# Converting NumPy array to byte format
byte_output = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]).tobytes()

# Converting byte format back to NumPy array
array_format = np.frombuffer(byte_output)
