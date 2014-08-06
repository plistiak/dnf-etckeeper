dnf-etckeeper
=============

etckeeper plugin for Dandified Yum (DNF) package manager.
For installation just copy etckeeper.py to dnf-plugins directory. You can find this directory on your system via following command:

    python -c "from distutils.sysconfig import get_python_lib; print('%s/dnf-plugins' % (get_python_lib()))"
