class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def introduce(self):
        return f"{self.name}（{self.age}岁）成绩{self.score}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add(self, name, age, score):
        student = Student(name, age, score)
        self.students.append(student)
        print(f"已添加：{name}")

    def show_all(self):
        if not self.students:
            print("还没有学生")
            return
        print(f"共有 {len(self.students)} 名学生：")
        for s in self.students:
            print("  " + s.introduce())

    def find(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None

    def delete(self, name):
        s = self.find(name)
        if s:
            self.students.remove(s)
            print(f"已删除：{name}")
            return True
        print(f"没找到：{name}")
        return False

    def update_score(self, name, new_score):
        s = self.find(name)
        if s:
            s.score = new_score
            print(f"已把{name}的成绩改为{new_score}")
        else:
            print(f"没找到：{name}")


def main():
    manager = StudentManager()
    while True:
        print("\n===== 学生档案管理系统 =====")
        print("1. 添加学生")
        print("2. 显示全部")
        print("3. 查找学生")
        print("4. 删除学生")
        print("5. 修改成绩")
        print("0. 退出")
        choice = input("请选择：")

        if choice == "1":
            name = input("姓名：")
            age = int(input("年龄："))
            score = int(input("成绩："))
            manager.add(name, age, score)
        elif choice == "2":
            manager.show_all()
        elif choice == "3":
            name = input("要查找的姓名：")
            s = manager.find(name)
            if s:
                print("找到了：" + s.introduce())
            else:
                print(f"没找到：{name}")
        elif choice == "4":
            name = input("要删除的姓名：")
            manager.delete(name)
        elif choice == "5":
            name = input("要改成绩的姓名：")
            new_score = int(input("新成绩："))
            manager.update_score(name, new_score)
        elif choice == "0":
            print("再见！")
            break
        else:
            print("输入无效，请重新选择")


if __name__ == "__main__":
    main()
