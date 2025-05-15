# Problem Statement: Find the Average Marks of a Student

## Overview

The provided code stub will read in a dictionary containing key/value pairs of `name: [marks]` for a list of students. Your task is to print the average of the marks array for the student name provided in the query, showing **2 places after the decimal**.

---

## Input Format

- The first line contains the integer **n**, the number of students' records.
- The next **n** lines contain the student name followed by the space-separated marks obtained by the student.
- The final line contains **query_name**, the name of the student whose average marks need to be calculated.

---

## Constraints

- The number of students will be between **2** and **10**.
- Each student's marks will contain exactly **3** values.
- All marks are floating point numbers between **0** and **100**.

---

## Output Format

Print one line: The average of the marks obtained by the particular student, **correct to 2 decimal places**.

---

## Sample Input 0

```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

### Sample Output 0

```
56.00
```

---

## Sample Input 1

```
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
```

### Sample Output 1

```
26.50
```

---

## Explanation

- In **Sample Input 0**, marks for Malika are `[52, 56, 60]`. Their average is `(52 + 56 + 60) / 3 = 56.00`.
- In **Sample Input 1**, marks for Harsh are `[25, 26.5, 28]`. Their average is `(25 + 26.5 + 28) / 3 = 26.50`.

Your program should read the student data into a dictionary, calculate the average for the `query_name`, and print it formatted to two decimal places.
