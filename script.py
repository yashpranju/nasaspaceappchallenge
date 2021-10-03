from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
   return"""This is our first Website !Hello Guys,\n

I am Harshada Ananta Gharat.I have completed my B.E. in Computer Science in 2020. \n

I am feeling honour to serve myself for NASA through my contribution. \n 

I have some analysis report which I have completed during this event and I wanted showcase that in front of you guys. \n 

This are the things which I have researched and I hope you will give your valubale time thank you !\n 


Regards,\n 
Harshada Ananta Gharat"""

if __name__=="__main__":
    app.run(debug=True)
