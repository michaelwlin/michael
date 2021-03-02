"""
***************************************************************************
Filename:      reverse_lines.py
Author:        Michael Lin
Date:          2021.02.21
Modifications: Michael Lin - 2021.02.21
Description:   This module takes reads each line in a file:
            1) Reverses the lines in the file (first line would be last and last would be first)
            2) Writes them to another file
***************************************************************************
"""
temp = []
file = open("stand_by_your_man.txt")
for line in file:
    temp.append(line)
file.close()
temp[len(temp)-1] += "\n"

print(temp)
new_file = open("output.txt", "x")
for line in reversed(temp):
    new_file.write(line)
new_file.close()
print("Please check 'output.txt' for your result.")

"""
TEST CASE #1
stand_by_your_man.txt
***************
Sometimes it's hard to be a woman
Givin' all your love to just one man
You'll have bad times, and he'll have good times
Doin' things that you don't understand
But if you love him, you'll forgive him
Even though he's hard to understand
And if you love him, oh be proud of him
'Cause after all, he's just a man
Stand by your man
Give him two arms to cling to
And somethin' warm to come to
When nights are cold and lonely
Stand by your man
And show the world you love him
Keep givin' all the love you can
Stand by your man
Stand by your man
And show the world you love him
Keep givin' all the love you can
Stand by your man


output.txt
*********************
Stand by your man
Keep givin' all the love you can
And show the world you love him
Stand by your man
Stand by your man
Keep givin' all the love you can
And show the world you love him
Stand by your man
When nights are cold and lonely
And somethin' warm to come to
Give him two arms to cling to
Stand by your man
'Cause after all, he's just a man
And if you love him, oh be proud of him
Even though he's hard to understand
But if you love him, you'll forgive him
Doin' things that you don't understand
You'll have bad times, and he'll have good times
Givin' all your love to just one man
Sometimes it's hard to be a woman

"""
