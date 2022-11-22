# pwn_synchrotron_xray_movie
The code for creating animated synthetic synchtrotron map of a pulsar wind nebula model. 

The pulsar wind nebula (PWN) model is built with the use of
publicly available code PLUTO http://plutocode.ph.unito.it/
following the method, described in the paper of
Porth O., Komissarov S. S., Keppens R., 2014, MNRAS, 438, 278

With the output of the PLUTO code -- the distributions of pressure, magnetic field, 
velocity and density of the pulsar wind plasma of the model PWN, the map of the 
model PWN's synthetic synchrotron x-ray emission is calculated as described in the paper of
Del Zanna L., Volpi D., Amato E., Bucciantini N., 2006, A&A, 453, 621

The synthetic x-ray maps of the nebula are stored in ./data/data.zip
The maps are tables in .dat format, named named syn_nnn.dat where nnn corresponds
to the time step of the code (e.g. nnn = 125 corresponds to the model nebula age of 12.5 years)

The file create_movie.py is the main script, which processes .dat-files with PWN synthetic x-ray 
maps: 
1) saves them in .png format (the .png images are stored in the folder "./snapshots/") 
and then
2) creates a .gif movie from these snapshots (the movies are stored in the folder "./movies/")

The file config.py stores the names of the project folders (or creates them if absent).
The file managers.py contains context managers which handle data loading and plotting.
The file tools.py contains all the function for the data processing pipeline.

The folder "old" contains the initial version of the script, much simpler but less flexible one.

In the future, an extended functionality of this code will be provided...
