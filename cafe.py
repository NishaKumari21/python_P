a="""Welcome to our restaurant,Here's the menu:
(1)COFFEE:RS 45
(2)PASTA :RS 30
(3)PIZZA :RS 300
(4)NOODLES:RS 180
(5)CUPCAKE:RS 50
(6)CHOCO PIE:RS 80"""
print(a)
choice=int(input("enter your choice:"))
opt="""options are---------
TYPE 1>>COFFEE:RS 45
TYPE 2>>PASTA :RS 30
TYPE 3>>PIZZA :RS 300
TYPE 4>>NOODLES:RS 180
TYPE 5>>CUPCAKE:RS 50
TYPE 6>>CHOCO PIE:RS 80 """
print(choice)
ordered_total=0
if choice==1:
    print("THANKS FOR YOUR ORDER!")
    q=("Do you want some other order too?\n TYPE (1)FOR YES AND (0) FOR NO")
    print(q)
    if q==1:
        print("Tell me your other order sir/maam:",ordered_total+)
        ans=str(input("Tell me your other order sir/maam:"))
        print(ans)
    elif q==0:
        print("OKAY.................THANKING YOU!..................")