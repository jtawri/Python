# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:15:12 2020

@author: Vijay
"""

from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/result', methods=['POST' , 'GET'])
def result():
    number1=float(request.form["number1"])
    number2=float(request.form["number2"])
    
    if request.method=="POST":
        if request.form["process"]=="addition":
            return str(number1+number2)
        if request.form["process"]=="substraction":
            return str(number1-number2)
        if request.form["process"]=="multiplication":
            return str(number1*number2)
        if request.form["process"]=="division":
            return str(number1/number2)
        
        
        
        
if __name__=='__main__':
    app.run()
