-- Add a new column for subscription date
ALTER TABLE subscribers ADD COLUMN subscription_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- Verify the table structure
DESCRIBE subscribers;
