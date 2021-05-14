import os
import subprocess
# Creates directory structure
os.mkdir("API")
os.mkdir("Data")
os.mkdir("./API/middleware")
os.mkdir("./API/Routers")
os.mkdir("./API/Models")
# Creates the index.js file
f = open("index.js", "w")
f.write('const server = require("./API/server.js");\nconst dotenv = require("dotenv");\ndotenv.config();\n\nconst PORT = process.env.PORT || 3300;\nserver.listen(PORT, () => {\nconsole.log(`=== Server listening on port ${PORT} ===`);\n});')
# Creates the server.js file 
f = open("./API/server.js", "w")
f.write('const express = require("express");\nconst cors = require("cors");\nconst helmet = require("helmet");\n\nconst server = express();\nserver.use(helmet());\nserver.use(cors());\nserver.use(express.json());\nserver.get("/", (req, res) => {\nres.status(200).json("Its Up");\n});\n\nmodule.exports = server;')
# Initializes NPM
npm_init= subprocess.run(["npm", "init", "-y"])
# Installs Production dependancies
npm_install = subprocess.run(["npm", "i", "express", "cors", "helmet","dotenv"])
print("normal dependancies installed")
# Installs Dev dependancies
npm_dev = subprocess.run(["npm", "i", "-D", "nodemon", "eslint"])
print("Dev dependancies installed")
#Inserts nodemon command into package.json
f = open("package.json", "r")
contents = f.readlines()
f.close()
contents.insert(6, '"server":"nodemon index.js",')
f = open("package.json", "w")
contents = "".join(contents)
f.write(contents)
f.close()
print('\n\n\n\n\n\n\n\n')
print("===========================")
print("Happy hacking")
print("===========================")
f.close()