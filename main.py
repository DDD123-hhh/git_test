def display_menu():
    print("\n学生成绩管理系统")
    print("1. 录入学生成绩")
    print("2. 按姓名查询成绩")
    print("3. 按学号查询成绩")
    print("4. 按课程查询成绩")
    print("5. 统计课程成绩")
    print("6. 退出")

def add_student(students):
    name = input("请输入学生姓名: ")
    student_id = input("请输入学号: ")
    course = input("请输入课程名称: ")
    grade = float(input("请输入成绩: "))

    if grade < 0 or grade > 100:
        print("错误: 成绩必须在0到100之间")
        return

    for student in students:
        if student['student_id'] == student_id:
            print("错误: 学号已存在")
            return

    students.append({
        'name': name,
        'student_id': student_id,
        'course': course,
        'grade': grade
    })
    print("成绩录入成功!")

def query_by_name(students):
    name = input("请输入学生姓名: ")
    results = [student for student in students if student['name'] == name]
    if results:
        for result in results:
            print(result)
    else:
        print("未找到相关记录")

def query_by_student_id(students):
    student_id = input("请输入学号: ")
    results = [student for student in students if student['student_id'] == student_id]
    if results:
        for result in results:
            print(result)
    else:
        print("未找到相关记录")

def query_by_course(students):
    course = input("请输入课程名称: ")
    results = [student for student in students if student['course'] == course]
    if results:
        for result in results:
            print(result)
    else:
        print("未找到相关记录")

def get_course_statistics(students):
    course = input("请输入课程名称: ")
    grades = [student['grade'] for student in students if student['course'] == course]

    if not grades:
        print("未找到该课程的成绩记录")
        return

    average = sum(grades) / len(grades)
    max_grade = max(grades)
    min_grade = min(grades)

    print(f"课程: {course}")
    print(f"平均分: {average:.2f}")
    print(f"最高分: {max_grade}")
    print(f"最低分: {min_grade}")

def main():
    students = []
    while True:
        display_menu()
        choice = input("请输入选项: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            query_by_name(students)
        elif choice == '3':
            query_by_student_id(students)
        elif choice == '4':
            query_by_course(students)
        elif choice == '5':
            get_course_statistics(students)
        elif choice == '6':
            print("退出系统")
            break
        else:
            print("无效选项，请重新输入")

if __name__ == "__main__":
    main()
