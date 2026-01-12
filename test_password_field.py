"""
Quick test to verify the password field rename works correctly
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from database import DatabaseManager

def test_password_field():
    print("="*60)
    print("Testing password field rename")
    print("="*60)
    
    db = DatabaseManager()
    
    # Test 1: Create a test user
    print("\n[Test 1] Creating test user...")
    test_user = {
        "nombre_completo": "Test User",
        "cedula": "9999999",
        "correo_electronico": "test@test.com",
        "telefono": "3001234567",
        "password": "TestPassword123",
        "fecha_registro": "2026-01-12 10:00:00"
    }
    
    # Clean up first
    users = db._load_users()
    if "9999999" in users:
        del users["9999999"]
        db._save_users(users)
    
    success, message = db.create_user(test_user.copy())
    if success:
        print(f"[PASS] User created: {message}")
    else:
        print(f"[FAIL] Failed to create user: {message}")
        return False
    
    # Test 2: Verify the field is named 'password' in JSON
    print("\n[Test 2] Verifying JSON structure...")
    users = db._load_users()
    user_data = users.get("9999999")
    
    if user_data and "password" in user_data:
        print("[PASS] Field 'password' exists in JSON")
    else:
        print("[FAIL] Field 'password' not found in JSON")
        print(f"Available fields: {list(user_data.keys()) if user_data else 'None'}")
        return False
    
    if "contraseña" in user_data:
        print("[FAIL] Old field 'contraseña' still exists!")
        return False
    else:
        print("[PASS] Old field 'contraseña' removed")
    
    # Test 3: Verify login works
    print("\n[Test 3] Testing login...")
    user = db.verify_user("9999999", "TestPassword123")
    
    if user:
        print(f"[PASS] Login successful for: {user['nombre_completo']}")
    else:
        print("[FAIL] Login failed!")
        return False
    
    # Clean up
    print("\n[Cleanup] Removing test user...")
    users = db._load_users()
    if "9999999" in users:
        del users["9999999"]
        db._save_users(users)
        print("[OK] Test user removed")
    
    return True

if __name__ == "__main__":
    print("\nPASSWORD FIELD RENAME TEST\n")
    
    if test_password_field():
        print("\n" + "="*60)
        print("ALL TESTS PASSED!")
        print("="*60)
        sys.exit(0)
    else:
        print("\n" + "="*60)
        print("TESTS FAILED!")
        print("="*60)
        sys.exit(1)
