CREATE TABLE word_history (
    id SERIAL PRIMARY KEY,
    word VARCHAR(255) NOT NULL,
    details JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
