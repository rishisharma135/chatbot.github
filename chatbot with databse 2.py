import sqlite3

# Function to create a connection to the SQLite database
def create_connection():
    conn = sqlite3.connect('school_info.db')
    return conn

# Function to create a table to store school info
def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS school_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

# Function to insert initial data into the table
def insert_initial_data():
    conn = create_connection()
    c = conn.cursor()
    questions_and_answers = [
        ("school name", "Edify School"),
        ("school location", "Edify School & junior college is located at Khasra no 50, Kharir, Kamptee road, Nagpur."),
        ("school facilities", "Our school has a library, science lab, computer lab, swimming pool, and a sports field."),
        ("admission process", "To apply for admission, please visit our website or contact the school office."),
        ("courses offered", "We offer courses from Grade 1 to 12 in which we have PCM, PCB, and PCMB in science."),
        ("contact info", "You can contact us at 8380000741 or email us at info@edifyschoolnagpur.com."),
        ("principal", "The Principal of our school is Smita Dev Ma'am"),
        ("created by", "I was created by 12th students to help in their project"),
        ("purpose of", "It can help you to know more about our school"),
    ]
    c.executemany("INSERT INTO school_info (question, answer) VALUES (?, ?)", questions_and_answers)
    conn.commit()
    conn.close()

# Function to insert a new question-answer pair into the database
def insert_question(question, answer):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO school_info (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()
    print(f"Question '{question}' added successfully.")

# Function to get a response from the database
def get_response(user_input):
    conn = create_connection()
    c = conn.cursor()

    c.execute("SELECT answer FROM school_info WHERE question LIKE ?", ('%' + user_input + '%',))
    result = c.fetchone()

    if result:
        return result[0]  # Return the answer from the database
    else:
        return "I'm sorry, I didn't understand that."

    conn.close()

# Main function to interact with the user
def main():
    print("Welcome to the School Chatbot! Type 'bye' to exit.")
    create_table()  # Create the table if it doesn't exist
    # Uncomment the next line to insert initial data (run once)
    # insert_initial_data()

    while True:
        user_input = input("You: ").lower()  # Prompt the user for input
        
        # If the user asks to add a new question, we insert it into the database
        if user_input.startswith("add question"):
            # Prompt the user for a question and its answer
            new_question = input("Enter the new question: ")
            new_answer = input("Enter the answer for the new question: ")

            # Insert the new question-answer pair into the database
            insert_question(new_question, new_answer)
            continue  # Skip the rest of the loop and go back to the main menu
        
        # Get the chatbot's response
        response = get_response(user_input)  
        print("Chatbot:", response)  # Print the response

        if user_input in ["bye", "exit", "quit"]:
            break

if __name__ == "__main__":
    main()
