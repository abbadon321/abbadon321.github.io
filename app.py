from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/opportunities')
def show_opportunities():
   return render_template('opportunities.html')

@app.route('/enrollee')
def to_enrolee():
   return render_template('enrollee.html')

@app.route('/dept-activities')
def get_dept_activities():
   return render_template('dept-activities.html')

@app.route('/student-activities')
def get_student_activities():
   return render_template('student-activities.html')


if __name__ == '__main__':
  app.run(debug=True)