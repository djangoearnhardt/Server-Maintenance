import os

# establish network paths
s = os.path.abspath('D:\\BBBack')
n = os.path.abspath('B:\\EE.SQL')

# sort directories by oldest to newest
maa_13 = sorted(os.listdir((os.chdir(s))), key=os.path.getctime)
netserv_5 = sorted(os.listdir((os.chdir(n))), key=os.path.getctime)

# see how many files are in each backup directory, set max for directory size
maa_total = len(maa_13)
netserv_total = len(netserv_5)
s_max = 20
n_max = 10

# find oldest backup file
m_alpha = os.path.join(s, maa_13[0])
m_beta = os.path.join(s, maa_13[1])
n5_alpha = os.path.join(n, netserv_5[0])

# tests if files and paths exist
# print(m_alpha, m_beta, n5_alpha)
# print(os.path.exists(m_alpha), os.path.exists(m_beta), os.path.exists(n5_alpha))

# deletes the oldest file while there are more than 10 in each directory
if maa_total > s_max: os.remove(m_alpha); os.remove(m_beta)
# elif maa_total > max: os.remove(m_beta)
if netserv_total > n_max: os.remove(n5_alpha)

# pyclean.py maintains 20 RE backup files on MAA_13 and 10 files on Netserv5
