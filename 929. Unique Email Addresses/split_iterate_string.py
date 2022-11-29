class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        unique_emails = set()
        
        for email in emails:
            edited_email = ""
            email = email.split('@')
            for c in email[0]:
                if c == '+':
                    break
                if c != '.':
                    edited_email += c
            edited_email = edited_email + '@' + email[1]
            unique_emails.add(edited_email)
        
        return len(unique_emails)
    