import os
import subprocess
#import mysql.connector


#cnx = connection.MySQLConnection(user=os.environ['DBUSERNAME'], 
#                                 password=os.environ['DBPASSWORD'],
#                                 host=os.environ['DBHOST'],
#                                 database=os.environ['DBNAME'])

print os.environ['NAME']
name = os.environ['NAME']
email = os.environ['EMAIL']
githubUser = os.environ['USERNAME']
token = os.environ['TOKEN']

init = "git init"
config = "git config --global user.name {} | git config --global user.email {} | git config --global github.user {} | git config --global github.token {} | git remote add heroku https://github.com/pgilmor/ctg-update.git".format(name, email, githubUser, token)
pull = "git pull heroku master"
govinfo = "./run govinfo --bulkdata=BILLSTATUS --congress=115 --debug"
bills = "./run bills --congress=115 --debug"
votes = "./run votes --congress=115 --session=2018 --force --debug"
commitBashCommand ="git add data | git commit -m 'Update' | git push heroku master"
add = "git add ."
commit = "git commit -m 'Update'"
push = "git push heroku master -ff"

os.chdir('/app/')
print "Init"
subprocess.call(init, shell=True)
print "Config"
subprocess.call(config, shell=True)
print "Govinfo"
#subprocess.call(govinfo, shell=True)
print "Bills"
subprocess.call(bills, shell=True)
print "Votes"
#subprocess.call(votes, shell=True)
print "Add"
subprocess.call(add, shell=True)
print "Pull"
subprocess.call(pull, shell=True)
print "Commit"
subprocess.call(commit, shell=True)
print "Push"
subprocess.call(push, shell=True)


#cnx.close()
