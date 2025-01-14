
def get_book_content():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def number_words(text):
    return (len(text.split()))

#Is element in a dictionary -> Ture | False
def is_element_in_dictionary(element, dictionary):
    for key, val in dictionary.items():
        if element == key :
            return True 
    return False

def number_character(text):
    char_count_dictionary = {}
    for index in range(0, len(text)):
        character = text[index].lower()
        if(character.isalpha()):
            if(is_element_in_dictionary(character, char_count_dictionary)):
                char_count_dictionary[character] += 1
            else:
                char_count_dictionary[character] = 1
    
    #To sort dictionary elements based on value
    char_count_dictionary = dict(sorted(char_count_dictionary.items(), key=lambda x:x[1], reverse=True))

    return char_count_dictionary

frankenstein_content = get_book_content()
frankenstein_number_of_words = number_words(frankenstein_content)
frankenstein_character_counter = number_character(frankenstein_content)

print("--- Begin report of books/frankenstein.txt ---")
print('%d words found in the document \n' % frankenstein_number_of_words)

for key, val in frankenstein_character_counter.items():
    print('The \'%s\' character was found %d times ' % (key, val))

print('--- End report ---')

