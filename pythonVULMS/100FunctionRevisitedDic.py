
    # In here arguments are recieved as a dictionary by the function
# All dictionary methods are avaliable to process the args.
        # Inlcuding keys(), values() and items() etc
def Myfunction(**Args):
    print(f"\nThis function includes {Args =}\n ")
    print(f"{type(Args) =}    {len(Args) =}")
    print(f"{Myfunction =}  {type(Myfunction) =}")

Myfunction(Roll_No=531,Department="CS",Name="Sohail")

