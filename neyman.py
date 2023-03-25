"""
Name: Craig Brooks
PHSX 815 Spring 2023
HW # 8
Due Date 3/24/2023
This code performs the Neyman construction given parameters of mu_experimental, standard deviation, number of experiments, number of measurements
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

if __name__ == "__main__":

	# if the user includes the flag -h or --help print the options
	if '-h' in sys.argv or '--help' in sys.argv:
		print ("Usage: %s [-mu -sigma -n -meas ]" % sys.argv[0])
		print
		sys.exit(1)

	if '-mu' in sys.argv:
		p = sys.argv.index('-mu')
		mu_experiment = int(sys.argv[p+1])
	else:
		mu_experiment = 10
	if '-sigma' in sys.argv:
		p = sys.argv.index('-sigma')
		sigma = float(sys.argv[p+1])
	else:
		sigma = .1
	if '-N' in sys.argv:
		p = sys.argv.index('-N')
		N_exp = int(sys.argv[p+1])
	else:
		N_exp = 10
	if '-meas' in sys.argv:
		p = sys.argv.index('-meas')
		N_meas = int(sys.argv[p+1])
	else:
		N_meas = 10
	# data array for mu_true
	mu_true_array = []
	# array containing mu_best from simulation
	mu_best_array = []

	np.random.seed(666)
	
	# draws samples from a normal distribution with N_measurements for N_exp experiments 
	for i in range(-100,100):
	    mu_true = i/10
	    
	    for exp  in range(N_exp):
	        mu_best = 0
	        for m in range(N_meas):
	            sample = np.random.normal(mu_true, sigma)
	            mu_best += sample
	        mu_best = mu_best / N_meas
	        mu_true_array.append(mu_true)
	        mu_best_array.append(mu_best)
	   
	# Plots 2D histogram
	
	plt.hist2d(mu_true_array, mu_best_array, bins = 100,norm = colors.LogNorm())
	plt.xlabel('$\mu_{true}$')
	plt.ylabel('$\mu_{best}$')
	plt.title(f'mu_best vs mu_true for {N_exp} experiments, {N_meas} measurements')
	plt.colorbar()
	plt.show()
