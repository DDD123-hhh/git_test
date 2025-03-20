def add_students:
    name=input("请输入学生姓名：")
    student_id=input("请输入学号：")
    course=input("请输入课程名称：")
    grade=float(input("请输入成绩："))
    if grade <0 or grade >100:
        print("错误：成绩必须在0到100之间")
        return
    for student in students:
        if student['student_id']==student_id:
            print("错误：学号已存在")
            return
        students.append({
            'name':name,
            'student_id':student_id,
            'course':course,
            'grade':grade
            })
        print("成绩录入成功！")
                
