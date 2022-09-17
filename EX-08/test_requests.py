# 1.  5 студентов с наибольшим средним баллом по всем предметам.

"""SELECT students.name, AVG(student_marks.mark) AS average_mark
FROM students
JOIN student_marks ON students.id = student_marks.student_id
GROUP BY students.name
ORDER BY average_mark DESC
LIMIT 6;"""
'''
    select s.name, round(avg(m.mark), 2) as avg_mark
    from student_marks m
    left join students s on s.id = m.student_id 
    group by s.id 
    order by avg_mark desc 
    limit 5;
'''


# 2. 1 студент с наивысшим средним баллом по одному предмету.

"""
    SELECT subj.name, s.name, ROUND(AVG(m.mark),2) AS average_mark
    FROM student_marks m
    LEFT JOIN students s ON s.id = m.student_id 
    LEFT JOIN subjects subj ON subj.id = m.subject_id 
    WHERE subj.id = 2
    GROUP BY s.id, subj.id
    ORDER BY average_mark DESC
    LIMIT 1;
"""