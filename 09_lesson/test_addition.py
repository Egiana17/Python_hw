def test_insert_and_delete_and_update(db_connection):
    repo = TeacherTable()
    initial_count = repo.get_count(db_connection)
    teacher_email = "new@gmail.com"
    new_teacher_email = "Updated@gmail.com"

    # Добавление
    repo.insert_teacher(db_connection, teacher_email)
    assert repo.get_count(db_connection) == initial_count + 1
    