from flask import Flask,render_template,request
import NewsAPIscheduler
import TwitterAPIcaller
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        form_type = request.form['type']
        form_desc = request.form['desc']
        session_state="inactive"
        execfile(NewsAPIscheduler)
        execfile(TwitterAPIcaller)
       # print form_type,form_desc
        return render_template('index.html',nowstate=session_state)



if __name__ == '__main__':
    app.run()
