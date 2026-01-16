import base64
from bs4 import BeautifulSoup

def parse_message(msg):
    payload = msg['payload']
    headers = payload.get('headers', [])
    
    data = {
        'from': '',
        'subject': '',
        'date': '',
        'content': ''
    }

    for header in headers:
        name = header.get('name').lower()
        if name == 'from':
            data['from'] = header.get('value')
        elif name == 'subject':
            data['subject'] = header.get('value')
        elif name == 'date':
            data['date'] = header.get('value')

    def get_body(payload):
        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/plain':
                    return part['body'].get('data', '')
                elif part['mimeType'] == 'text/html':
                    return part['body'].get('data', '')
        else:
            return payload.get('body', {}).get('data', '')
        return ''

    body_data = get_body(payload)

    if body_data:
        decoded_bytes = base64.urlsafe_b64decode(body_data)
        raw_content = decoded_bytes.decode('utf-8', errors='ignore')
        
        if "<html" in raw_content.lower():
            soup = BeautifulSoup(raw_content, "html.parser")
            for script_or_style in soup(["script", "style"]):
                script_or_style.decompose()
            data['content'] = soup.get_text(separator=' ', strip=True)
        else:
            data['content'] = raw_content

    return data