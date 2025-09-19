import re

def detect_social_engineering(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation

    # Comprehensive social engineering patterns
    patterns = {
        # Urgency & pressure tactics
        "Urgent action required": r"\burgent action required\b",
        "Act now": r"\bact now\b",
        "Immediate response needed": r"\bimmediate response needed\b",
        "Limited time offer": r"\blimited time offer\b",
        "Final notice": r"\bfinal notice\b",
        "Deadline approaching": r"\bdeadline approaching\b",
        "Only a few spots left": r"\bonly a few spots left\b",
        "Respond before it's too late": r"\brespond before it's too late\b",
        "Your account will be deleted": r"\byour account will be deleted\b",

        # Security threats / impersonation
        "Account suspended": r"\byour account (has been )?suspended\b",
        "Account locked": r"\byour account (has been )?locked\b",
        "Unusual activity": r"\bwe noticed unusual activity\b",
        "Unauthorized login attempt": r"\bunauthorized login attempt\b",
        "Device infected": r"\byour device has been infected\b",
        "Legal action": r"\blegal action will be taken\b",
        "Security alert": r"\bsecurity alert\b",

        # Financial manipulation
        "Pay immediately": r"\bpay immediately\b",
        "Update billing info": r"\bupdate your billing info\b",
        "Transaction pending": r"\byour transaction is pending\b",
        "Send payment": r"\bsend payment now\b",
        "Refund eligibility": r"\byou are eligible for a refund\b",
        "Financial opportunity": r"\bfinancial opportunity\b",
        "Limited cashback": r"\blimited time cashback\b",

        # Fake identity / authority
        "From your bank": r"\bfrom your bank\b",
        "From your CEO": r"\bfrom your ceo\b",
        "From IT department": r"\bfrom your it department\b",
        "Government notice": r"\bgovernment notice\b",
        "Police/FBI request": r"\b(police|fbi|irs) request\b",
        "Official message": r"\bofficial message from\b",
        "Internal use only": r"\binternal use only\b",
        "Do not share": r"\bdo not share this message\b",

        # Free rewards & manipulation
        "You have won": r"\byou have won\b",
        "Claim your reward": r"\bclaim your reward\b",
        "Get a free": r"\bget a free\b",
        "Win a prize": r"\byou won (the car|a prize)\b",
        "Win money": r"\bwin money now\b",
        "Lucky draw": r"\blucky draw winner\b",
        "Click to win": r"\bclick here to (win|claim)\b",

        # Phishing and credential theft
        "Document attached": r"\bimportant document attached\b",
        "Confirm identity": r"\bconfirm your identity\b",
        "Reset password": r"\breset your password\b",
        "Click to reset": r"\bclick (here|on the link) to reset\b",
        "Verify account": r"\bverify your account\b",
        "Enter OTP": r"\benter your otp\b",
        "Login link": r"\bclick here to log in\b",
        "Download attachment": r"\bdownload attachment\b",
        "Open the file immediately": r"\bopen the file immediately\b",
        "Secure link": r"\bclick this secure link\b",
        "Attached invoice": r"\battached invoice\b",

        # Social manipulation & fraud
        "Don't tell anyone": r"\bdont tell anyone\b",
        "Urgent favor": r"\bi need a favor urgently\b",
        "Help me": r"\bi'm in trouble help me\b",
        "Impersonation": r"\bits me your friend\b",
        "Send OTP": r"\bi lost my phone please send otp\b",

        # Manipulative language / curiosity
        "Check this out": r"\bcheck this out\b",
        "Don’t miss this": r"\bdont miss this\b",
        "Shocking news": r"\bshocking news about you\b",
        "You won’t believe": r"\byou wont believe what happened\b",
        "Click below": r"\bclick the link below\b",
        "Blow your mind": r"\bthis will blow your mind\b",
        "Hidden truth": r"\bhidden truth revealed\b",
        "Secret info": r"\bsecret information\b",
        "Just for you": r"\bthis message is just for you\b",
    }

    # Find all matching pattern labels
    matched_flags = [label for label, pattern in patterns.items() if re.search(pattern, text)]
    return matched_flags
