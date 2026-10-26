
CREATE DATABASE IF NOT EXISTS dmai_nlp;
USE dmai_nlp;

CREATE TABLE IF NOT EXISTS Students (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Department VARCHAR(50) NOT NULL,
    Semester INT NOT NULL,
    Marks DECIMAL(5,2) NOT NULL,
    City VARCHAR(50) NOT NULL,
    Attendance DECIMAL(5,2) DEFAULT NULL
);

INSERT IGNORE INTO Students
(Student_ID, Name, Department, Semester, Marks, City, Attendance)
VALUES
(101, 'Aarav Sharma', 'AI', 3, 85.50, 'Delhi', 85.00),
(102, 'Riya Verma', 'CSE', 3, 92.00, 'Noida', 92.00),
(103, 'Kabir Singh', 'AI', 2, 76.00, 'Delhi', 68.00),
(104, 'Ananya Gupta', 'CSE', 4, 88.00, 'Ghaziabad', 88.00),
(105, 'Arjun Mehta', 'ECE', 3, 67.50, 'Jaipur', 72.00),
(106, 'Priya Sharma', 'AI', 4, 95.00, 'Noida', 95.00),
(107, 'Rahul Kumar', 'CSE', 2, 72.00, 'Lucknow', 70.00),
(108, 'Sneha Kapoor', 'ECE', 4, 81.00, 'Delhi', 81.00),
(109, 'Dev Malhotra', 'AI', 3, 89.00, 'Jaipur', 89.00),
(110, 'Isha Jain', 'CSE', 4, 78.50, 'Noida', 74.00),
(111, 'Aditya Verma', 'AI', 3, 82.00, 'Mumbai', 82.00),
(112, 'Meera Shah', 'CSE', 4, 91.00, 'Pune', 91.00),
(113, 'Rohan Patel', 'ECE', 2, 74.00, 'Ahmedabad', 74.00),
(114, 'Ishita Rao', 'AI', 3, 87.50, 'Hyderabad', 87.50),
(115, 'Karan Malhotra', 'CSE', 4, 79.00, 'Chandigarh', 79.00),
(116, 'Simran Kaur', 'ECE', 3, 84.00, 'Amritsar', 84.00),
(117, 'Vivek Joshi', 'AI', 2, 93.00, 'Bengaluru', 93.00),
(118, 'Pooja Nair', 'CSE', 3, 68.50, 'Kochi', 68.50),
(119, 'Manav Bansal', 'ECE', 4, 89.00, 'Indore', 89.00),
(120, 'Tanya Das', 'AI', 4, 96.00, 'Kolkata', 96.00),
(121, 'Ananya Mishra', 'AI', 3, 88.50, 'Bhopal', 88.50),
(122, 'Rishabh Sinha', 'CSE', 4, 76.00, 'Patna', 76.00),
(123, 'Kavya Iyer', 'ECE', 2, 91.50, 'Chennai', 91.50),
(124, 'Siddharth Roy', 'AI', 4, 83.00, 'Bhubaneswar', 83.00),
(125, 'Neha Kulkarni', 'CSE', 3, 94.00, 'Nagpur', 94.00),
(126, 'Yash Thakur', 'ECE', 4, 71.50, 'Dehradun', 71.50),
(127, 'Aditi Menon', 'AI', 2, 86.00, 'Thiruvananthapuram', 86.00),
(128, 'Harsh Vardhan', 'CSE', 3, 79.50, 'Varanasi', 79.50),
(129, 'Diya Chawla', 'ECE', 4, 97.00, 'Surat', 97.00),
(130, 'Mohit Agarwal', 'AI', 3, 65.00, 'Ranchi', 65.00);
