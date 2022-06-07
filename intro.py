import numpy as np

'''
absmag
	inputs: 
		- m: floating point or numpy array of apparent magnitudes
		- d: floating point or numpy array of distances in parsecs
	outputs: 
		- M: floating point or numpy array of absolute magnitudes
'''

def absmag(m,d):
    M = m + 5 - 5*np.log10(d)
    return M
'''
scale_density
	input: 
		- distlist: floating point or numpy array of distances in light years
	output: 
		- dscale: floating point or numpy array of distances in parsecs
'''

def scale_density(distlist):
    dscale = []
    for dist in distlist:
        dist_pc = dist*0.306601
        dscale.append(dist_pc)
    return dscale

# create initial dictionary of messier objects:
messier_objects = {'names':['M1','M2','M3','M4'],
                   'dist (ly)': [6.523,5.5e4,3.39e4,7175],
                   'apparent mag' : [8.4, 6.5, 6.2, 5.6]}

messier_objects['dist (pc)'] = scale_density(messier_objects['dist (ly)'])

# convert lists into numpy arrays to do math
appmags = np.array(messier_objects['apparent mag'])
dists = np.array(messier_objects['dist (pc)'])
absolutemags = absmag(appmags,dists)
messier_objects['absolute mags'] = absolutemags
print(messier_objects)  # show resulting dictionary

