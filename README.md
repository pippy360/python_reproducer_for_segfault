# python_reproducer_for_segfault
This is a reproducer for a segfault in Python 3.6.7

To reproduce this issue I run the following commands on a newly deployed vm on Debian GNU/Linux 9 (stretch):

```
sudo apt-get install git -y
git clone https://github.com/pippy360/python_reproducer_for_segfault.git
cd python_reproducer_for_segfault/
sudo apt-get install python3-pip -y
pip3 install .
pip3 install .
```

output:
```
user@instance-3:~/python_reproducer_for_segfault$ pip3 install .
Processing /home/user/python_reproducer_for_segfault
Collecting hiredis (from lets-cause-a-segfault==0.0.0)
  Downloading https://files.pythonhosted.org/packages/51/df/d2a08fb767247c0acea66255908e60cdeb4cd13cf71d42a1e2ca5803a1f8/hiredis-1.0.0-cp35-cp35m-manylinux1_x86_64.whl (49kB)
    100% |████████████████████████████████| 51kB 1.7MB/s 
Collecting numpy (from lets-cause-a-segfault==0.0.0)
  Downloading https://files.pythonhosted.org/packages/ad/15/690c13ae714e156491392cdbdbf41b485d23c285aa698239a67f7cfc9e0a/numpy-1.16.1-cp35-cp35m-manylinux1_x86_64.whl (17.2MB)
    100% |████████████████████████████████| 17.2MB 82kB/s 
Collecting redis (from lets-cause-a-segfault==0.0.0)
  Downloading https://files.pythonhosted.org/packages/f1/19/a0282b77c23f9f9dbcc6480787a60807c78a45947593a02dbf026636c90d/redis-3.1.0-py2.py3-none-any.whl (63kB)
    100% |████████████████████████████████| 71kB 11.3MB/s 
Collecting scikit-learn (from lets-cause-a-segfault==0.0.0)
  Downloading https://files.pythonhosted.org/packages/18/d9/bea927c86bf78d583d517f24cbc87606cb333bfb3a5c99cb85b547305f0f/scikit_learn-0.20.2-cp35-cp35m-manylinux1_x86_64.whl (5.3MB)
    100% |████████████████████████████████| 5.3MB 279kB/s 
Collecting scipy (from lets-cause-a-segfault==0.0.0)
  Downloading https://files.pythonhosted.org/packages/ab/19/c0ad5b9183ef97030edd6297d1726525ff2c369a09fbb6ea52a1e616ffd6/scipy-1.2.0-cp35-cp35m-manylinux1_x86_64.whl (26.5MB)
    100% |████████████████████████████████| 26.5MB 48kB/s 
Collecting tqdm>=4.29.1 (from lets-cause-a-segfault==0.0.0)
  Downloading https://files.pythonhosted.org/packages/76/4c/103a4d3415dafc1ddfe6a6624333971756e2d3dd8c6dc0f520152855f040/tqdm-4.30.0-py2.py3-none-any.whl (47kB)
    100% |████████████████████████████████| 51kB 10.9MB/s 
Installing collected packages: hiredis, numpy, redis, scipy, scikit-learn, tqdm, lets-cause-a-segfault
  Running setup.py install for lets-cause-a-segfault ... done
Successfully installed hiredis-1.0.0 lets-cause-a-segfault-0.0.0 numpy-1.16.1 redis-3.1.0 scikit-learn-0.20.2 scipy-1.2.0 tqdm-4.30.0
user@instance-3:~/python_reproducer_for_segfault$ ^C
user@instance-3:~/python_reproducer_for_segfault$ pip3 install .
Processing /home/user/python_reproducer_for_segfault
Collecting hiredis (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/51/df/d2a08fb767247c0acea66255908e60cdeb4cd13cf71d42a1e2ca5803a1f8/hiredis-1.0.0-cp35-cp35m-manylinux1_x86_64.whl
Collecting numpy (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/ad/15/690c13ae714e156491392cdbdbf41b485d23c285aa698239a67f7cfc9e0a/numpy-1.16.1-cp35-cp35m-manylinux1_x86_64.whl
Collecting redis (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/f1/19/a0282b77c23f9f9dbcc6480787a60807c78a45947593a02dbf026636c90d/redis-3.1.0-py2.py3-none-any.whl
Collecting scikit-learn (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/18/d9/bea927c86bf78d583d517f24cbc87606cb333bfb3a5c99cb85b547305f0f/scikit_learn-0.20.2-cp35-cp35m-manylinux1_x86_64.whl
Collecting scipy (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/ab/19/c0ad5b9183ef97030edd6297d1726525ff2c369a09fbb6ea52a1e616ffd6/scipy-1.2.0-cp35-cp35m-manylinux1_x86_64.whl
Collecting tqdm>=4.29.1 (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/76/4c/103a4d3415dafc1ddfe6a6624333971756e2d3dd8c6dc0f520152855f040/tqdm-4.30.0-py2.py3-none-any.whl
Installing collected packages: hiredis, numpy, redis, scipy, scikit-learn, tqdm, lets-cause-a-segfault
  Running setup.py install for lets-cause-a-segfault ... done
Successfully installed hiredis-1.0.0 lets-cause-a-segfault-0.0.0 numpy-1.16.1 redis-3.1.0 scikit-learn-0.20.2 scipy-1.2.0 tqdm-4.30.0
Segmentation fault
user@instance-3:~/python_reproducer_for_segfault$ 
```
gdb stack 
```
(gdb) r /usr/bin/pip3 install .
Starting program: /usr/bin/python3 /usr/bin/pip3 install .
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Processing /home/tomnomnom1/python_reproducer_for_segfault
Collecting hiredis (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/51/df/d2a08fb767247c0acea66255908e60cdeb4cd13cf71d42a1e2ca5803a1f8/hiredis-1.0.0-cp35-cp35m-manylinux1_x86_64.whl
Collecting numpy (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/ad/15/690c13ae714e156491392cdbdbf41b485d23c285aa698239a67f7cfc9e0a/numpy-1.16.1-cp35-cp35m-manylinux1_x86_64.whl
Collecting redis (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/f1/19/a0282b77c23f9f9dbcc6480787a60807c78a45947593a02dbf026636c90d/redis-3.1.0-py2.py3-none-any.whl
Collecting scikit-learn (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/18/d9/bea927c86bf78d583d517f24cbc87606cb333bfb3a5c99cb85b547305f0f/scikit_learn-0.20.2-cp35-cp35m-manylinux1_x86_64.whl
Collecting scipy (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/ab/19/c0ad5b9183ef97030edd6297d1726525ff2c369a09fbb6ea52a1e616ffd6/scipy-1.2.0-cp35-cp35m-manylinux1_x86_64.whl
Collecting tqdm>=4.29.1 (from lets-cause-a-segfault==0.0.0)
  Using cached https://files.pythonhosted.org/packages/76/4c/103a4d3415dafc1ddfe6a6624333971756e2d3dd8c6dc0f520152855f040/tqdm-4.30.0-py2.py3-none-any.whl
Installing collected packages: hiredis, numpy, redis, scipy, scikit-learn, tqdm, lets-cause-a-segfault
  Running setup.py install for lets-cause-a-segfault ... done
Successfully installed hiredis-1.0.0 lets-cause-a-segfault-0.0.0 numpy-1.16.1 redis-3.1.0 scikit-learn-0.20.2 scipy-1.2.0 tqdm-4.30.0

Program received signal SIGSEGV, Segmentation fault.
0x00005555556aa054 in visit_decref () at ../Modules/gcmodule.c:373
373     ../Modules/gcmodule.c: No such file or directory.
(gdb) bt
#0  0x00005555556aa054 in visit_decref () at ../Modules/gcmodule.c:373
#1  0x00005555557443d5 in dict_traverse.lto_priv () at ../Objects/dictobject.c:2570
#2  0x00005555556ae773 in subtract_refs () at ../Modules/gcmodule.c:398
#3  collect () at ../Modules/gcmodule.c:951
#4  0x00005555557a591d in collect_with_callback () at ../Modules/gcmodule.c:1119
#5  0x00005555557a5981 in PyGC_Collect () at ../Modules/gcmodule.c:1583
#6  0x00005555557ab1ac in Py_Finalize () at ../Python/pylifecycle.c:567
#7  0x00005555557ab2a8 in Py_Exit (sts=sts@entry=0) at ../Python/pylifecycle.c:1465
#8  0x00005555557ab38e in handle_system_exit () at ../Python/pythonrun.c:602
#9  0x00005555557ab3f6 in PyErr_PrintEx () at ../Python/pythonrun.c:612
#10 0x00005555557ac667 in PyErr_Print () at ../Python/pythonrun.c:508
#11 PyRun_SimpleFileExFlags () at ../Python/pythonrun.c:401
#12 0x00005555557d92e7 in run_file (p_cf=0x7fffffffe40c, filename=0x555555c0e2a0 L"/usr/bin/pip3", fp=0x555555cca200) at ../Modules/main.c:318
#13 Py_Main () at ../Modules/main.c:768
#14 0x0000555555668d71 in main () at ../Programs/python.c:65
#15 0x00007ffff6cee2e1 in __libc_start_main (main=0x555555668c90 <main>, argc=4, argv=0x7fffffffe618, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffe608) at ../csu/libc-start.c:291
#16 0x000055555576fa7a in _start ()
(gdb) 
```
python stack 
```
(gdb) py-bt
Traceback (most recent call first):
  Garbage-collecting
(gdb) 
```
