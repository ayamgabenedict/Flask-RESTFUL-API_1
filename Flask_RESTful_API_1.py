from flask import Flask, jsonify, abort


#Initialization
app= Flask(__name__)


students=[{
    'student_id': 1,
    'first_name':'Jane',
    'Last_name': 'Doe',
    'age': 30,
    'isMale': False 
},
{
    'student_id': 2,
    'first_name':'John',
    'Last_name': 'Cena',
    'age': 45,
    'isMale': True
},
{
    'student_id': 3,
    'first_name':'Christiano',
    'Last_name': 'Ronaldo',
    'age': 34,
    'isMale': True 
},
{
    'student_id': 4,
    'first_name':'Jane',
    'Last_name': 'Doe',
    'age': 30,
    'isMale': False 
}, {
    'student_id': 5,
    'first_name':'Asamoah',
    'Last_name': 'Gyan',
    'age': 34,
    'isMale': True 
}
]

#Create new student record
@app.route('/students', methods=['POST'])
def create():
    error = False
    try: 
        student={
        "student_id": 6,
        "first_name":"Serena",
        "Last_name": "Williams",
        "age": 37,
        "isMale": False
        }
        students.append(student)
    except:
        error =True
        if error:
            abort(405)
    finally:
            return jsonify({
                "New student": students[-1],
                "message": "Successfully added new student"
                })
    

#Read all students
@app.route('/')
@app.route('/students')
def get_books():
        error = False
        if not error:
            return jsonify({
                "Students List":students,
                "Total number of students": len(students)
                })
        else:
            return jsonify({
                "error message":"Operation Unsuccessful"
                }, 422)


#Read particular student
@app.route('/students/<int:student_id>')
def get_student(student_id ):
    try: 
        return jsonify({
            'student Name':students[student_id],
            "info": f"{1} record out of {len(students)}"
        })
    except IndexError:
        abort(404)
    except:
        abort(405)



#Update student record
@app.route('/students/<int:student_id>', methods=['PATCH'])
def student_update(student_id):
    try:
        students[student_id]['Last_name']= 'Baby Jet Gyan'
        return jsonify({
                "success": True,
                'Student':students[student_id],
                "message": "Last name successfully updated."
            }) 
    except:
        abort(404) 
   

#Delete student record
@app.route('/students/<int:student_id>', methods= ['DELETE'])
def delete_student(student_id):
    try:
        if students[student_id] not in students:
            abort(404)
        else:
            students.remove(students[student_id])
            return jsonify({
                "success":True,
                "message": f"Student record successfully deleted"
                })
    except:
        abort(404)



#Error Handling
@app.errorhandler(400)
def bad_request(error):
    return (jsonify({
        'success': False,
        'error_code': 400,
        'error_message':'Bad Request'
    }), 400)



@app.errorhandler(404)
def resource_not_found(error):
    return (jsonify({
        'success': False,
        'error_code': 404,
        'error_message':'Resource not found'
    }), 404)
    

@app.errorhandler(405)
def unallowed_method(error):
    return (jsonify({
        'success': False,
        'error_code': 405,
        'error_message':'Method not allowed'
    }), 405)
    

@app.errorhandler(422)
def unprocessable(error):
    return (jsonify({
        'success': False,
        'error_code': 422,
        'error_message':'Request not processable'
    }), 422)
    



if __name__== '__main__':
    app.run(debug=True)

    