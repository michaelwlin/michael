"""
***************************************************************************
Filename:      unisex.py
Author:        Michael Lin
Date:          2021.02.21
Modifications: Michael Lin - 2021.02.21
Description:   This module reads a file in a specific format:
            1) Prints all the names that are both boy and girl names
***************************************************************************
"""
boys = []
girls = []
file = open("babynames.txt")
for line in file:
    tempMixed = ""
    tempBoy = ""
    tempGirl = ""
    for char in line:
        if char.isalpha():
            tempMixed += char
    tempBoy+=tempMixed[0]
    counter = 1
    for char in tempMixed[1:]:
        if char.isupper():
            break
        else:
            tempBoy += char
            counter+=1
    for char in tempMixed[counter:]:
        tempGirl += char
    boys.append(tempBoy)
    girls.append(tempGirl)
counter = 0
for name in boys:
    if name in girls:
        counter += 1
        print(str(counter) + ". " + name)

"""
TEST CASE #1
babynames.txt
(Contains 1000 pairs of Boy & Girl names)

Output: 
1. Jayden
2. Logan
3. Ryan
4. Dylan
5. Jordan
6. Angel
7. Cameron
8. Blake
9. Bentley
10. Parker
11. Hayden
12. Jaden
13. Micah
14. Kayden
15. Riley
16. Rylan
17. Peyton
18. Sawyer
19. Jaiden
20. Avery
21. Kai
22. Charlie
23. Alexis
24. Zion
25. Elliot
26. Skyler
27. Quinn
28. Amari
29. Rowan
30. Dakota
31. Taylor
32. Ali
33. Emerson
34. Phoenix
35. Payton
36. Casey
37. River
38. Armani
39. Finley
40. Justice
41. Skylar
42. Morgan
43. Reese
44. London
45. Rory
46. Kendall
47. Harper
48. Ariel
49. Harley
50. Jordyn
51. Jessie
52. Emery
53. Tatum
54. Rylee
55. Teagan
56. Jaylin
57. Jamie
58. Camryn
59. Eden
60. Sage
61. Lyric
62. Kamryn
63. Jaidyn
64. Reagan
65. Sidney
66. Leighton
"""



