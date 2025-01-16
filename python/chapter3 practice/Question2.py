letter='''Dear <|Name|>
            You are selected!
            <|Date|>'''


print(letter.replace("<|Name|>","dev") .replace("<|Date|>","16 january 2025"))