import sqlite3

def run_crud_app():
    # 1. Connect to Database (creates file if not exists)
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    # 2. Create Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            position TEXT
        )
    """)

    # --- CRUD FUNCTIONS ---

    # INSERT (Create)
    def add_employee(emp_id, name, pos):
        cursor.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_id, name, pos))
        conn.commit()
        print(f"Record Inserted: {name}")

    # DISPLAY (Read)
    def show_employees():
        cursor.execute("SELECT * FROM employees")
        results = cursor.fetchall()
        print("\n--- Employee Records ---")
        for row in results:
            print(f"ID: {row[0]} | Name: {row[1]} | Position: {row[2]}")
        print("------------------------")

    # UPDATE (Update)
    def update_position(emp_id, new_pos):
        cursor.execute("UPDATE employees SET position = ? WHERE id = ?", (new_pos, emp_id))
        conn.commit()
        print(f"Record Updated: Employee {emp_id} is now {new_pos}")

    # DELETE (Delete)
    def remove_employee(emp_id):
        cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
        conn.commit()
        print(f"Record Deleted: Employee ID {emp_id}")

    # --- Execution Logic ---
    add_employee(101, "Alice", "Developer")
    add_employee(102, "Bob", "Designer")
    
    show_employees()  # Display initial records

    update_position(101, "Senior Developer")
    remove_employee(102)

    show_employees()  # Display after update and delete

    conn.close()

if __name__ == "__main__":
    run_crud_app()