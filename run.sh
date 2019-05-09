docker run -v`pwd`:`pwd` -p 127.0.0.1:7070:7070 -it drsin bash -c "cd `pwd`; paster serve development.ini"
