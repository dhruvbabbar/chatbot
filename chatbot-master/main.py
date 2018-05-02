from flask import Flask, render_template, request, jsonify
import aiml
import json
import os
import dates as dt
import pymysql.cursors
#from flask.ext.mysql import MySQL

connection = pymysql.connect(host='localhost',
                             user='Springstudent',
                             password='Springstudent',
                             db='Web_customer_service',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)


@app.route("/",methods=['POST','GET'])
def main():    
#        if(request.method=="POST"):
#            return ("inside main post")
        
        print("inside main get")
        return render_template('chat1.html')


#Error: this saves the data into the database but happens only once. Second time the control somehow returns the main menu by calling the "/" controller stated above. 
@app.route("/contact", methods=['POST'])
def contact():  
            print ("inside contact post")
            name="null"
            phone="null"
            result = request.get_json(force=True)
            name= result.get('name')
            phone=result.get('phone')
            print(name)
            print(phone)
              
            try:      
                with connection.cursor() as cursor:
                # Read a single record
                    sql = "INSERT INTO customer (Namez,Phone) VALUES (%s, %s)";
                    cursor.execute(sql, (name,phone))
                    connection.commit()  
                    print(info.phone)
                    print(info.name)
                    console.log("this is a dummy method")
                    
            finally:     
#                    connection.close()
                    return "Saved successfully."
        
#app.route("/test",method=['POST','GET'])
#def test():
            
        
@app.route("/policyStatus", methods=['POST'])
def status():  
            result = request.get_json(force=True)
            number = result.get('policyNumber')           
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT policyStatus FROM policydetails WHERE policyNumber = %s";
                cursor.execute(sql, number)
                status=cursor.fetchone()
                status=status.get('policyStatus')
                status=json.dumps(status)                
                connection.commit()   
            return jsonify({'status':'OK','answer':status})  
        
@app.route("/renewalStatus", methods=['POST'])
def renewalStatus():  
            result = request.get_json(force=True)
            number = result.get('policyNumber')            
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT renewalStatus FROM policydetails WHERE policyNumber = %s";
                cursor.execute(sql, number)
                renewalStatus=cursor.fetchone()
                renewalStatus=renewalStatus.get('renewalStatus')
                renewalStatus=json.dumps(renewalStatus)                
                connection.commit()   
            return jsonify({'status':'OK','answer':renewalStatus})  
        
@app.route("/maturityBenefit", methods=['POST'])
def maturityBenefit():  
            result = request.get_json(force=True)
            number = result.get('policyNumber')            
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT maturityBenefit FROM policydetails WHERE policyNumber = %s";
                cursor.execute(sql, number)
                maturity=cursor.fetchone()
                maturity=maturity.get('maturityBenefit')
                maturity=json.dumps(maturity)   
                print(maturity)
                connection.commit()   
            return jsonify({'status':'OK','answer':maturity})  
        
@app.route("/fundValue", methods=['POST'])
def fundVal():      
            result = request.get_json(force=True)
            number = result.get('policyNumber')                
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT fundValue FROM policydetails WHERE policyNumber = %s";
                cursor.execute(sql, number)
                fundValue=cursor.fetchone()
                fundValue=fundValue.get('fundValue')              
                fundValue=json.dumps(fundValue)     
                connection.commit()   
            return jsonify({'status':'OK','answer':fundValue})       
        
@app.route("/surrenderValue", methods=['POST'])
def surrenderVal():      
            result = request.get_json(force=True)
            number = result.get('policyNumber') 
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT surrenderValue FROM policydetails WHERE policyNumber = %s";
                cursor.execute(sql, number)
                surrenderValue=cursor.fetchone()
                surrenderValue=surrenderValue.get('surrenderValue')              
                surrenderValue=json.dumps(surrenderValue)                      
                connection.commit()   
            return jsonify({'status':'OK','answer':surrenderValue})

@app.route("/neftStatus", methods=['POST'])
def neftStatus():      
            result = request.get_json(force=True)
            number = result.get('policyNumber') 
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT neftStatus FROM policydetails WHERE policyNumber = %s";
                cursor.execute(sql, number)
                neftStatus=cursor.fetchone()
                neftStatus=neftStatus.get('neftStatus')              
                neftStatus=json.dumps(neftStatus)                      
                connection.commit()   
            return jsonify({'status':'OK','answer':neftStatus})
        
@app.route("/revivalAmount", methods=['POST'])
def revivalAmount():      
            result = request.get_json(force=True)
            number = result.get('policyNumber') 
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT revivalAmount FROM policydetails WHERE policyNumber = %s";
                cursor.execute(sql, number)
                revivalAmt=cursor.fetchone()
                revivalAmt=revivalAmt.get('revivalAmount')              
                revivalAmt=json.dumps(revivalAmt)                      
                connection.commit()   
            return jsonify({'status':'OK','answer':revivalAmt})
        
@app.route("/premiumDifference", methods=['POST'])
def premiumDifference():      
            result = request.get_json(force=True)
            number = result.get('policyNumber') 
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT premiumDiff FROM policydetails WHERE policyNumber = %s";
                cursor.execute(sql, number)
                premiumDifference=cursor.fetchone()
                premiumDifference=premiumDifference.get('premiumDiff')              
                premiumDifference=json.dumps(premiumDifference)                      
                connection.commit()   
            return jsonify({'status':'OK','answer':premiumDifference})
        
@app.route("/premiumStatus", methods=['POST'])
def premiumStatus():      
            result = request.get_json(force=True)
            number = result.get('policyNumber') 
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT premiumStatus FROM policydetails WHERE policyNumber = %s";
                cursor.execute(sql, number)
                premiumStatus=cursor.fetchone()
                premiumStatus=premiumStatus.get('premiumStatus')              
                premiumStatus=json.dumps(premiumStatus)                      
                connection.commit()   
            return jsonify({'status':'OK','answer':premiumStatus})
        
@app.route("/prevPremium", methods=['POST'])
def prevPremium():      
            result = request.get_json(force=True)
            number = result.get('policyNumber') 
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT prevPremium FROM policydetails WHERE policyNumber = %s";
                cursor.execute(sql, number)
                previousPremium=cursor.fetchone()
                previousPremium=previousPremium.get('prevPremium')              
                previousPremium=json.dumps(previousPremium)                      
                connection.commit()   
            return jsonify({'status':'OK','answer':previousPremium})
        
@app.route("/ask", methods=['POST','GET'])
def ask():  
            if (request.method=="POST"):
                print("inside ask post")
            message = str(request.form['messageText'])
            kernel = aiml.Kernel()
            print("inside ask  "+message)
            if os.path.isfile("bot_brain.brn"):
                kernel.bootstrap(brainFile = "bot_brain.brn")
            else:
                kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
                kernel.saveBrain("bot_brain.brn")

            # kernel now ready for use
            while True:
                if message == "quit":
                    exit()
                elif message == "save":
                    kernel.saveBrain("bot_brain.brn")
#                elif message == "Contact Us":
#                    print ("inside contact ")
##                    name="null"
##                    phone="null"
#                    result = request.get_json(force=True)
#                    name= result.get('name')
#                    phone=result.get('phone')
#                    print(name)
#                    print(phone)
#
#                    try:      
#                        with connection.cursor() as cursor:
#                        # Read a single record
#                            sql = "INSERT INTO customer (Namez,Phone) VALUES (%s, %s)";
#                            cursor.execute(sql, (name,phone))
#                            connection.commit()   
#
#                    finally:     
#                            #connection.close()
#                            return "Saved successfully."
                else:
                    bot_response = kernel.respond(message);                       
                    return jsonify({'status':'OK','answer':bot_response})
                
def answer():
            answer = str(request.form['messageText'])
            print(answer)
            kernel = aiml.Kernel()
            
            if os.path.isfile("bot_brain.brn"):
                kernel.boostrap(brainFile= "bot_brain.brn")
                
            else:
                kernel.boostrap(learngFiles = os.path.abspath("aim/std-starup.xml"),commands = "Load aiml b")
                kernel.saveBrain("bot_brain.brn")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
