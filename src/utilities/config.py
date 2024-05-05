from dotenv import load_dotenv
import os

load_dotenv()

dbhost = os.environ.get("dbhost")
dbuser = os.environ.get("dbuser")
dbpassword = os.environ.get("dbpassword")
dbname = os.environ.get("dbname")

secretkey = os.environ.get("secretkey")

root = os.environ.get("root")
minfs = bool(os.environ.get("minfs"))

webhost = os.environ.get("webhost")
webport = os.environ.get("webport")

instancehost = os.environ.get("instancehost")
instanceport = os.environ.get("instanceport")
instancename = os.environ.get("instancename")

checkforupdates = bool(os.environ.get("checkforupdates"))
