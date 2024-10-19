 def is_anagram(test, original):
    if len(test) != len(original): # თ ტესტი არუდრის ორიგინალს დააბრუნოს არასწორი
        return False

    joined = (test + original).lower()  #ვაპატარავებთ 

    for char in joined:
        if joined.count(char) % 2 != 0:
            return False