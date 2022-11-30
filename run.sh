docker run -v`pwd`:`pwd` -p 0.0.0.0:7070:7070 -it drsin bash -c "cd `pwd`; python setup.py install; paster serve development.ini"

