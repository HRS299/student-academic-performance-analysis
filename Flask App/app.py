

from flask import Flask, render_template, request, redirect, url_for, jsonify

from db_config import get_connection



app = Flask(__name__)


# -----------------------------------
# LOGIN PAGE
# -----------------------------------
@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        # ADMIN
        if username == 'admin' and password == 'admin123':

            return redirect(
                "https://app.powerbi.com/groups/me/reports/36385c50-d094-47f3-92e9-8333625279bb/ce8c2e2bb050c0662c36?experience=power-bi"
            )

            # return redirect(
            #     url_for(
            #         'dashboard',
            #         role='Admin',
            #         username=username
            #     )
            # )

        # FACULTY
        elif username == 'faculty' and password == 'faculty123':

            return redirect(
                "https://app.powerbi.com/groups/me/reports/36385c50-d094-47f3-92e9-8333625279bb/8c8da43dea52739509ad?experience=power-bi"
            )

            # return redirect(
            #     url_for(
            #         'dashboard',
            #         role='Admin',
            #         username=username
            #     )
            # )

        # COORDINATOR
        elif username == 'coordinator' and password == 'coord123':

            return redirect(
                "https://app.powerbi.com/groups/me/reports/36385c50-d094-47f3-92e9-8333625279bb/c9e657312298414e3119?experience=power-bi"
            )

            # return redirect(
            #     url_for(
            #         'dashboard',
            #         role='Admin',
            #         username=username
            #     )
            # )

        else:
            return "Invalid Credentials"

    return render_template('login.html')


# -----------------------------------
# DASHBOARD PAGE
# -----------------------------------
@app.route('/dashboard/<role>/<username>')
def dashboard(role, username):

    return render_template(
        'dashboard.html',
        role=role,
        username=username
    )

# -----------------------------------
# API — GET STUDENTS
# -----------------------------------
@app.route('/api/students')
def get_students():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM student_performance_view
    LIMIT 20
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(data)




# -----------------------------------
# API — HIGH RISK STUDENTS
# -----------------------------------
@app.route('/api/high-risk-students')
def high_risk_students():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM student_performance_view
    WHERE risk_level = 'High Risk'
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(data)




# -----------------------------------
# API — DEPARTMENT PERFORMANCE
# -----------------------------------
@app.route('/api/department-performance')
def department_performance():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT
        department_name,
        ROUND(AVG(gpa), 2) AS average_gpa,
        ROUND(AVG(avg_attendance), 2) AS average_attendance
    FROM student_performance_view
    GROUP BY department_name
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(data)


# -----------------------------------
# RUN FLASK
# -----------------------------------
if __name__ == '__main__':
    app.run(debug=True)