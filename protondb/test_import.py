#!/usr/bin/env python3
"""
Test script to verify ProtonDB plugin can be imported correctly
"""

import sys
import os
from pathlib import Path

# Add the plugin directory to the path
plugin_dir = Path(__file__).parent
sys.path.insert(0, str(plugin_dir))

def test_basic_import():
    """Test basic Python imports"""
    try:
        import json
        import time
        import requests
        from urllib.parse import quote_plus
        from pathlib import Path
        print("✅ Basic imports successful")
        return True
    except ImportError as e:
        print(f"❌ Basic import failed: {e}")
        return False

def test_albert_import():
    """Test Albert module import"""
    try:
        import albert
        print("✅ Albert module imported successfully")
        
        # Check what attributes are available
        attrs = [attr for attr in dir(albert) if not attr.startswith('_')]
        print(f"Available Albert attributes: {attrs}")
        
        # Check for required classes
        required_classes = ['PluginInstance', 'TriggerQueryHandler', 'Query', 'StandardItem', 'Action']
        missing_classes = []
        
        for cls in required_classes:
            if hasattr(albert, cls):
                print(f"✅ {cls} available")
            else:
                print(f"❌ {cls} missing")
                missing_classes.append(cls)
        
        if missing_classes:
            print(f"Missing required classes: {missing_classes}")
            return False
        
        return True
        
    except ImportError as e:
        print(f"❌ Albert import failed: {e}")
        return False

def test_plugin_import():
    """Test importing the ProtonDB plugin"""
    try:
        # Import the plugin module
        import __init__ as protondb_plugin
        print("✅ ProtonDB plugin module imported successfully")
        
        # Check metadata
        required_metadata = ['md_iid', 'md_version', 'md_name', 'md_description']
        for meta in required_metadata:
            if hasattr(protondb_plugin, meta):
                value = getattr(protondb_plugin, meta)
                print(f"✅ {meta}: {value}")
            else:
                print(f"❌ Missing metadata: {meta}")
        
        # Check if Plugin class exists
        if hasattr(protondb_plugin, 'Plugin'):
            plugin_class = protondb_plugin.Plugin
            print(f"✅ Plugin class found: {plugin_class}")
            
            # Check class inheritance
            bases = plugin_class.__bases__
            print(f"Plugin class bases: {bases}")
            
        else:
            print("❌ Plugin class not found")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Plugin import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_plugin_instantiation():
    """Test creating an instance of the plugin"""
    try:
        # This might fail if Albert context is not available
        import __init__ as protondb_plugin
        
        print("Attempting to create plugin instance...")
        plugin = protondb_plugin.Plugin()
        print("✅ Plugin instance created successfully")
        
        # Test basic methods
        if hasattr(plugin, 'defaultTrigger'):
            trigger = plugin.defaultTrigger()
            print(f"✅ Default trigger: '{trigger}'")
        
        if hasattr(plugin, 'synopsis'):
            synopsis = plugin.synopsis("test")
            print(f"✅ Synopsis: '{synopsis}'")
        
        return True
        
    except Exception as e:
        print(f"❌ Plugin instantiation failed: {e}")
        print("This is expected if Albert context is not available")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("ProtonDB Plugin Import Test")
    print("=" * 40)
    
    tests = [
        ("Basic Imports", test_basic_import),
        ("Albert Import", test_albert_import),
        ("Plugin Import", test_plugin_import),
        ("Plugin Instantiation", test_plugin_instantiation),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "=" * 40)
    print("TEST SUMMARY")
    print("=" * 40)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("⚠️  Some tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())