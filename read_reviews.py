from bs4 import BeautifulSoup
import re

def extract_cons(html_content):
    try:
        # Create BeautifulSoup object with a more lenient parser
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        
        # Find all paragraphs with cons content, using a more flexible approach
        cons_paragraphs = []
        
        # Try multiple approaches to find cons content
        # Method 1: Using data-testid
        cons_paragraphs.extend(soup.find_all('p', {'data-testid': 'cons-content'}))
        
        # Method 2: Looking for paragraphs containing "Cons:"
        for p in soup.find_all('p'):
            if 'Cons:' in p.get_text():
                cons_paragraphs.append(p)
        
        # Extract and clean the cons text
        cons_list = []
        for p in cons_paragraphs:
            # Get the text content
            text = p.get_text(strip=True)
            # Remove "Cons:" prefix and clean up whitespace
            text = re.sub(r'^Cons:\s*', '', text)
            text = re.sub(r'Cons:\s*', '', text)  # Remove "Cons:" anywhere in the text
            text = ' '.join(text.split())
            if text:  # Only add non-empty strings
                cons_list.append(text)
        
        return cons_list
            
    except Exception as e:
        print(f"An error occurred while parsing: {str(e)}")
        return []

# Read the file content
try:
    with open('reviews.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    cons = extract_cons(html_content)
    
    # Write results
    with open('cons_output.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(cons))
    
    print(f"Found and extracted {len(cons)} cons")
    
except Exception as e:
    print(f"An error occurred while reading/writing files: {str(e)}")