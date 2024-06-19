class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        #total number of words
        #check whether it is a multiple of maxwidth
        #if less -> next multiple of maxwidth
        #spaces = multiple - total words
        #check word by word and add spaces
        #or
        def add_spaces(words, maxWidth, is_last_line):
            if len(words) == 1 or is_last_line:
             # If there's only one word or it's the last line, left-justify
                line = ' '.join(words)
                return line + ' ' * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - sum(len(word) for word in words)
                space_slots = len(words) - 1
                even_spaces = total_spaces // space_slots
                extra_spaces = total_spaces % space_slots
            
                line = words[0]
                for i in range(1, len(words)):
                    spaces_to_add = even_spaces + (1 if i <= extra_spaces else 0)
                    line += ' ' * spaces_to_add + words[i]
                return line
    
        res, current_line, current_length = [], [], 0
        for word in words:
            if current_length + len(current_line) + len(word) > maxWidth:
                res.append(add_spaces(current_line, maxWidth, is_last_line=False))
                current_line, current_length = [], 0
            current_line.append(word)
            current_length += len(word)
    
        res.append(add_spaces(current_line, maxWidth, is_last_line=True))
        return res