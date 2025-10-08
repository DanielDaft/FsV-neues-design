#!/usr/bin/env python3
"""
Direct test of German Driving School PWA functionality
This script tests the PWA directly without browser automation redirects
"""

import requests
import re
from bs4 import BeautifulSoup

def test_pwa_accessibility():
    """Test if the PWA is accessible and contains expected content"""
    try:
        print("=== TESTING GERMAN DRIVING SCHOOL PWA ACCESSIBILITY ===")
        
        # Test direct access to localhost:8080
        response = requests.get("http://localhost:8080", timeout=10)
        print(f"✅ HTTP Status: {response.status_code}")
        
        if response.status_code == 200:
            content = response.text
            print(f"📄 Content length: {len(content)} characters")
            
            # Check for German Driving School PWA markers
            if "Deutsche Fahrschul-App" in content:
                print("✅ German Driving School PWA detected!")
                
                # Parse HTML to check for key elements
                soup = BeautifulSoup(content, 'html.parser')
                
                # Check for class selection elements
                class_cards = soup.find_all(string=re.compile(r"class-card|selectClass"))
                print(f"🔍 Found {len(class_cards)} class-related elements")
                
                # Check for card view functionality
                card_view_elements = soup.find_all(string=re.compile(r"switchToCardView|cardViewBtn|renderCardCircles"))
                print(f"🔍 Found {len(card_view_elements)} card view elements")
                
                # Check for circle functionality
                circle_elements = soup.find_all(string=re.compile(r"ue-circle|quarter-circle|ps-circle|add-circle-btn"))
                print(f"🔍 Found {len(circle_elements)} circle-related elements")
                
                # Check for specific functions mentioned in the issue
                functions_to_check = [
                    "renderCardCircles",
                    "switchToCardView", 
                    "toggleProgressItemCard",
                    "addCategoryUECircle",
                    "addCategoryQuarterCircle",
                    "toggleBlueCircle"
                ]
                
                print("\n=== CHECKING SPECIFIC FUNCTIONS ===")
                for func in functions_to_check:
                    if func in content:
                        print(f"✅ Function '{func}' found in code")
                    else:
                        print(f"❌ Function '{func}' NOT found in code")
                
                # Check for CSS classes related to circles
                css_classes = [
                    ".ue-circle",
                    ".quarter-circle", 
                    ".ps-circle",
                    ".add-circle-btn",
                    ".card-circles"
                ]
                
                print("\n=== CHECKING CSS CLASSES ===")
                for css_class in css_classes:
                    if css_class in content:
                        print(f"✅ CSS class '{css_class}' found")
                    else:
                        print(f"❌ CSS class '{css_class}' NOT found")
                
                return True
            else:
                print("❌ This doesn't appear to be the German Driving School PWA")
                print(f"📄 Content preview: {content[:200]}...")
                return False
        else:
            print(f"❌ HTTP request failed with status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")
        return False

def analyze_card_view_implementation():
    """Analyze the card view implementation in the HTML file"""
    try:
        print("\n=== ANALYZING CARD VIEW IMPLEMENTATION ===")
        
        with open("/app/index.html", "r", encoding="utf-8") as f:
            content = f.read()
        
        # Find renderCardCircles function
        render_card_circles_match = re.search(r'function renderCardCircles\(([^}]+)\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', content, re.DOTALL)
        if render_card_circles_match:
            print("✅ renderCardCircles function found")
            func_content = render_card_circles_match.group(0)
            
            # Check for UE circles implementation
            if "ue-circle" in func_content and "index + 1" in func_content:
                print("✅ UE circles with numbers implementation found")
            else:
                print("❌ UE circles with numbers implementation missing")
            
            # Check for quarter circles implementation  
            if "quarter-circle" in func_content and "getFillLevelClass" in func_content:
                print("✅ Quarter circles implementation found")
            else:
                print("❌ Quarter circles implementation missing")
                
            # Check for PS circles implementation
            if "blue-filled" in func_content or "ps-circle" in func_content:
                print("✅ PS circles implementation found")
            else:
                print("❌ PS circles implementation missing")
                
        else:
            print("❌ renderCardCircles function NOT found")
        
        # Check switchToCardView function
        switch_card_view_match = re.search(r'function switchToCardView\(\)[^}]*\{[^}]*\}', content)
        if switch_card_view_match:
            print("✅ switchToCardView function found")
            func_content = switch_card_view_match.group(0)
            
            if "cardView" in func_content and "display" in func_content:
                print("✅ Card view toggle functionality implemented")
            else:
                print("❌ Card view toggle functionality missing")
        else:
            print("❌ switchToCardView function NOT found")
            
        return True
        
    except Exception as e:
        print(f"❌ Analysis failed with error: {str(e)}")
        return False

if __name__ == "__main__":
    # Test PWA accessibility
    pwa_accessible = test_pwa_accessibility()
    
    # Analyze implementation
    implementation_ok = analyze_card_view_implementation()
    
    print(f"\n=== SUMMARY ===")
    print(f"PWA Accessible: {'✅' if pwa_accessible else '❌'}")
    print(f"Implementation Analysis: {'✅' if implementation_ok else '❌'}")