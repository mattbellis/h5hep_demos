set hfiles1000 = 'HEP_narrow_file_t*n1000.hdf5'


time python read_many_h5hep.py $hfiles1000 
time python read_many_h5hep.py HEP_narrow_file_t*n10000.hdf5 
time python read_many_h5hep.py HEP_narrow_file_t*n100000.hdf5 
time python read_many_h5hep.py HEP_narrow_file_t*n1000000.hdf5 

time python read_ROOT_files.py HEP_narrow_file_ROOT*n1000.root 
time python read_ROOT_files.py HEP_narrow_file_ROOT*n10000.root 
time python read_ROOT_files.py HEP_narrow_file_ROOT*n100000.root 
time python read_ROOT_files.py HEP_narrow_file_ROOT*n1000000.root 

