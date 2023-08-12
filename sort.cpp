#include <iostream>
#include <vector>
#include <algorithm>

struct Person {
    int ID;
    std::string Name;
    int Age;
    int Salary;
};

bool compareBySalary(const Person &a, const Person &b) {
    return a.Salary<b.Salary;
}

int main() {
    int num;
    std::cin >> num;
    std::string temp;
    std::cin >> temp >> temp >> temp >> temp ;
    std::vector<Person> people(num);
    for (int i = 0; i < num; ++i) {
        std::cin >> people[i].ID >> people[i].Name >> people[i].Age >> people[i].Salary;
    }
    

    std::sort(people.begin(), people.end(), compareBySalary);

    for (const auto &person : people) {
        std::cout << person.ID << " " << person.Name << " " << person.Age << " " << person.Salary << "\n";
    }

    return 0;
}
