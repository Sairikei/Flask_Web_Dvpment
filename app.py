from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Ananlyst',
    'location': 'Nairobi Kenya',
    'salary': 'Ksh. 2,000,000'
},
{
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Mombasa Kenya',
    'salary': 'Ksh. 2,300,000'
},
{
    'id': 3,
    'title': 'Front-end engineer',
    'location': 'Remote, Kenya',
    'salary': 'Ksh. 900,000'
},
{
    'id': 4,
    'title': 'Back-end Engineer',
    'location': 'Nairobi Kenya',
    #'salary': 'Ksh. 1,500,000'
}
]

@app.route('/')
def hello_world():
    return render_template('home.html',
                            jobs = JOBS,
                            company_name = 'Ferra')
@app.route("/api/jobs")
def hello_ferra():
    return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  