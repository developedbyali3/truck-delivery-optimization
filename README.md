# truck-delivery-optimization
finds the shortest path from warehouse to delivery locations and back to warehouse using the artificial bee colony algorithm.

--> generates NUM_BEES number of random paths
--> evaluates total distance of each path
--> keeps the top 50% of paths with lowest distance
--> adds new mutated paths
--> repeats steps 2-4 for ITERATIONS number of iterations
--> gives the best path
