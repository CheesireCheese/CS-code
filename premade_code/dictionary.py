def create_student_info():
    student_info = {
        "name": "Alice",
        "age": 25,
        "grade": "A",
        "subject": "Math",
    }
    student_info["age"] = 26
    student_info["city"] = "New York"
    return student_info


def main():
    student_info = create_student_info()
    print("Name", student_info["name"])
    print("updated student info", student_info)


if __name__ == "__main__":
    main()