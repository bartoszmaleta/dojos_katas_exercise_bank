# It's bonus time in the big city! The fatcats are rubbing their paws in anticipation... but who is going to make the most money?

# Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.

# If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not 
# make enough money and must receive only his stated salary.

# Return the total figure the individual will receive as a string prefixed 
# with "£" (= "\u00A3", JS, Go, and Java), "$" (C#, C++, Ruby, Clojure, Elixir, PHP and Python, Haskell, Lua) or "¥" (Rust).


def bonus_time(salary, bonus):
    dollar_sign = "$"    
        
    if bonus is True:
        salary = salary * 10
        salary = str(salary)
        salary = dollar_sign + salary
        return salary
    elif bonus is False:
        salary = str(salary)
        salary = dollar_sign + salary
        return salary