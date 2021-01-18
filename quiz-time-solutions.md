# Quiz Time!

Start your interactive Python session and try to find
answers to the following questions.

All answers are one-liners.

Tip: If you are unsure, use `help(TYPE)` to get an
     overview of all available methods.

Have fun!


## Questions on Lists

Given the list:

    lst = [1, 5, 2, 10, 50]

1. How can I get the position of the element `10`?

   Solution: `lst.index(50)`

2. How can I get the last item?

   Solution: `lst[-1]`

3. How can I get every 2nd element?

   Solution: `lst[::2]`

4. How can I add an element `6` at the beginning of the list?

   Solution: `lst.insert(0, 6)`

5. How can I reverse the list?

   * Solution 1: `lst[::-1]`
   * Solution 2: `list(reversed(lst))`

6. How can I add an element `42` at the end of the list?

   * Solution 1: `lst.append(42)`
   * Solution 2: `lst += [42]`


### Questions on Dicts

Given the dict:

    dct = dict(name="Tux",
               place="Greenland",
               friends=["Wilber", "Geeko"])

1. How can I get the value of the key `name`?

   Solution: `dct["name"]`

2. How can I get the value of the missing key `foo` *without*
   getting an error?

   Solution: `dct.get("foo")`

3. How do I add the new friend "Konqui" to the friends list?

   Solution: `dct["friends"].append("Konqui")`

4. How do I get all keys?

   Solution: `dct.keys()`

5. How do I get all values?

   Solution: `dct.values()`

6. How do I get keys *and* values together?

   Solution: `dct.items()`
  
7. How can I remove the key `friends`?

   * Solution 1: `del dct["friends"]`
   * Solution 2: `dct.pop("friends")`

8. How can I merge a second dict with
   `d2 = dict(name="Penguin", age=40)` into `dct`?

   * Solution 1: `dct.update(d2)`
   * Solution 2: `dct = {**dct, **d2}`


### Questions on Strings

Given the string:

    s = "The quick brown dog jumps over the lazy dog."

1. How many times occurs the letter `o` in the string?

   Solution 1: `s.count("o")`

2. How can I get every 2nd letter of the string?

   Solution: `s[::2]`

3. How can I reverse the string?

   (see https://www.journaldev.com/23647/python-reverse-string for timing)
   * Solution 1: `s[::-1]`
   * Solution 2: `''.join(reversed(s))`

4. How can you substitute the substring "dog" with "bat" one time?

   Solution 1: `s.find("dog", "bat", 1)`
   Solution 2: `s.replace("dog", "bat", 1)`

5. How can you cut the string into a list of words?

   Solution: `s.split(" ")`

6. How can I get the 2nd last word (=`lazy`)?

   Solution: `s.split(" ")[-2]`
