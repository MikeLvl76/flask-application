from flask import abort, redirect, request
from flask import render_template
from copy import deepcopy
from models import db, EmployeeModel, app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/employee')
def RetrieveDataList():
    employees = EmployeeModel.query.all()
    return render_template('employee_list.html', employees=employees)

@app.route('/employee/<int:id>')
def RetrieveSingleEmployee(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('employee_view.html', employee = employee)
    return f"Employee with id ={id} Doenst exist"

@app.route('/employee/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('employee.html')
 
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position=position)
        db.session.add(employee)
        db.session.commit()
        return redirect('/employee')

@app.route('/employee/<int:id>/update', methods = ['GET','POST'])
def update(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
 
            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = EmployeeModel(employee_id=id, name=name, age=age, position = position)
 
            db.session.add(employee)
            db.session.commit()
            return redirect(f'/employee/{id}')
        return f"Employee with id = {id} Does nit exist"
 
    return render_template('employee_update.html', employee = employee)

@app.route('/employee/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/employee')
        abort(404)
 
    return render_template('employee_delete.html')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello', methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
        result = request.form
        return render_template('hello.html', result=result)

@app.route('/sort', methods = ['POST', 'GET'])
def sort():
    if request.method == 'POST':
        formPage = request.form
        array = [formPage.get(f"v{i}") for i in range(1, 6)]
        start = deepcopy(array)
        list.sort(array)
        return render_template('sort.html', unsort=start, form=formPage, sorted=array)

app.run(host='localhost', port=5000)