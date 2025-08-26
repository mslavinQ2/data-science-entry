-- Table to store user sessions
CREATE TABLE sessions (
    session_id INT AUTOINCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    login_time TIMESTAMP,
    logout_time TIMESTAMP
);
