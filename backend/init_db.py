#!/usr/bin/env python3
"""
Initialize the database tables manually.
Run this before starting the server if tables are not created.
"""
import sys
sys.path.insert(0, '/Users/ibmsayem/CS_846_vibecoding/backend')

from app.models import database, user, post

# Create all tables
database.Base.metadata.create_all(bind=database.engine)
print("✓ Database tables created successfully!")
print("✓ Users table ready")
print("✓ Posts table ready")
print("✓ Likes table ready")
