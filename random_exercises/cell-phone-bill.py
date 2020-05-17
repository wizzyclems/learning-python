The program should take in two integer command-line arguments—
one for the number of peak minutes used, and one for the number
of weekend and night minutes used.

■■ Each customer pays $29.95 a month, which includes 400 peak minutes
and 750 weekend and night minutes.

■■ The price for going over the allotted time is $.40/minute for both
peak and weekend/night calls.


peak_minutes_used = raw_input("Enter Number of peak Minutes Used  : ")
num_weekend_night_mins_used = input("Enter Number of Weekend and Nights Minutes Used  : ")

monthly_pay = 29.95
standard_peak = 400
standard_weekend_night_mins = 750

cost_per_extra_min = 0.40


