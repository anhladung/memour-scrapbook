CREATE TABLE IF NOT EXISTS orders (
    order_code TEXT PRIMARY KEY,
    phone TEXT NOT NULL,
    payload TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_orders_phone ON orders(phone);
CREATE INDEX IF NOT EXISTS idx_orders_created_at ON orders(created_at DESC);
