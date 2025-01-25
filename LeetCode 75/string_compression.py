class Solution:
    def compress(self, chars):
        write = 0  # Pointer to write the compressed characters
        read = 0  # Pointer to read the characters
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count the number of occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write

sol = Solution()
sol.compress(["a","a","b","b","c","c","c"])
