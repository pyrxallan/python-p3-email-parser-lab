import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        if not self.email_string or not isinstance(self.email_string, str):
            return []
        
        # Split by commas and/or spaces
        tokens = re.split(r'[,\s]+', self.email_string)
        
        # Email regex pattern - matches basic email format
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Filter valid emails and remove duplicates
        emails = []
        seen = set()
        for token in tokens:
            token = token.strip()
            if token and re.match(email_pattern, token):
                if token not in seen:
                    emails.append(token)
                    seen.add(token)
        
        # Sort alphabetically
        return sorted(emails)

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
