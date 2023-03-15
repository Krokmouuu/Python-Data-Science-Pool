ft_list = ["Hello", "tata!"] # A list is a collection of ordered data that can be changed
ft_tuple = ("Hello", "toto") # A tuple is a collection of ordered data that cannot be changed
ft_set = {"Hello", "tutu!"} # A set is a collection of unordered data
ft_dict = {"Hello" : "titi!"} # A dict is a collection of unordered data with a key value pair

ft_list.remove(ft_list[1]) # Remove the case 1 of the tab
ft_list.append("World!") # Add at the end of the tab 
ft_tuple = ("Hello", "France!") # Redefinition of the tuple
ft_set.discard("tutu!") # Remove the case "tutu!" of the set
ft_set.add("Nice!") # Add at the end of the set
ft_dict.popitem() # Remove the last case of the dict
ft_dict.update({"Hello" : "42Nice!"}) # Adding a key value pair

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)