# IPython log file

get_ipython().run_line_magic('gui', '')
get_ipython().run_line_magic('pinfo', '%gui')
get_ipython().run_line_magic('gui', 'osx')
get_ipython().run_line_magic('logstart', '')
a = 5
b = 6
c = a + b 
c
get_ipython().run_line_magic('logoff', '')
