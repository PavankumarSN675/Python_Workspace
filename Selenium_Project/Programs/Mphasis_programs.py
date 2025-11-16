def get_vowels_count(input):
    counter = 0
    for i in range(0, len(input)):
        if input[i] == 'a' or input[i] == 'e' or input[i] == 'i' or input[i] == 'o' or input[i] == 'u':
            counter = counter + 1

    return counter


print(get_vowels_count("pavankumar"))

"""
// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
        String input = "pavankumar";
        int vowels_count = 0;
        for(int i=0;i<=input.length()-1;i++)
        {
          if(input.charAt(i) == 'a' || input.charAt(i) == 'e' ||
             input.charAt(i) == 'i' || input.charAt(i) == 'o' ||
             input.charAt(i) == 'u');
             {
                 System.out.println(input.charAt(i));
                 vowels_count = vowels_count + 1;
             }
        }
        System.out.println(vowels_count);
    }
} 
"""