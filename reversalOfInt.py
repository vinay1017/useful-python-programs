class reversal(object):

    def reverseInt(x):
        """
        Desc: A simple integer reversal program. Done for a practice problem on LeetCode. A number ending with 0
        shouldn't be reversed to have the 0 at all in front and a number with a leading negative sign should not have
        the negative sign at all if reversed.
        """
        if "0" in str(x):
            y = str(x)[::-1]
            y = y.replace("0", "")
            y = "-" + y

            if "-" in str(x):
                y = y.replace("-", "")
                y = "-" + y

        elif "-" in str(x):
            y = str(x)[::-1][0:5]
            y = y.replace("-", "")
            y = "-" + y
        else:
            y = str(x)[::-1]

        return y

    def reverseString(s):
        ## work in progress
        return s

print(reversal.reverseInt(123))
print(reversal.reverseInt(-123))
print(reversal.reverseInt(-1200000))


