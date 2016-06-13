import os
import sys
import subprocess
from HDF5converter import convert

snap_dir_list = [#"/scratch/01708/cfaucher/B1_hr_Dec5_2013_11",
  #"/scratch/01708/cfaucher/m09_hr_Dec16_2013",
  #"/scratch/01708/cfaucher/m10_hr_Dec9_2013"]#,
  #"/scratch/01708/cfaucher/m11_hhr_Jan9_2013"]#,
  #"/scratch/01708/cfaucher/m12qq_hr_Dec16_2013",
  #"/scratch/01708/cfaucher/m12v_mr_Dec5_2013_3",
  #"/scratch/01708/cfaucher/m13_mr_Dec16_2013",
   "/Users/murray/Gizmo/m12v_mr_Dec5_2013_3" ]
  

#snap_id_list = [290, 340, 440]
#snap_id_list = range(290, 441)
#snap_id_list = range(90, 290)
#snap_id_list = range(90, 441)
snap_id_list = [440]

for snap_dir in snap_dir_list:
  for snap_id in snap_id_list:
  
    snap_id_str = str(snap_id)

    if len(snap_id_str)<3:
      snap_id_str = "0" + snap_id_str
    if len(snap_id_str)<3:
      snap_id_str = "0" + snap_id_str

    file_case = snap_dir + "/snapshot_" + snap_id_str + ".hdf5"
    dir_case = snap_dir + "/snapdir_" + snap_id_str
    if os.access(file_case, os.F_OK):
      rootdir = file_case
    elif os.access(dir_case, os.F_OK):
      rootdir = dir_case
    else:
      print "snap_id="
      print snap_id,
      print "not found in",
      print snap_dir
      continue

    print "rootdir=",
    print rootdir

    if os.path.exists(rootdir):
  	  if os.path.isfile(rootdir):
		  convert(rootdir)
	  else:
		  for root, subFolders, files in os.walk(rootdir):
		      for file in files:
		          if (file.find(".hdf5")!=-1):
			  	  convert(root+"/"+file)

    else:
	  print "FILE/PATH DOES NOT EXIST"
