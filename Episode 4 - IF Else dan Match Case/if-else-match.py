nilai = 85

if nilai > 90:
    print("A")
elif nilai > 90:
    print("B")
elif nilai > 90:
    print("C")
else:
    print("D")



menu = "sate"

match menu:
    case "sate":
        print("Kamu suka sate")
    case "bakso":
        print("Kamu suka sate")
    case _: #default
        print("Kamu tidak suka makan")


        
