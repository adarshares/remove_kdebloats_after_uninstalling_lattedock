# remove_kdebloats_after_uninstalling_lattedock
even after uninstalling the latte-dock many dependencies remain 
to remove dependencies (not all get removed) the python code can be used . The kdebloat.txt file was created by following the commands
written in the python code . kwalletmanager was still left after 
executing the code it can be removed separately by :
sudo apt-get autoremove kwalletmanager
