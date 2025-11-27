print("\n" * 50)
print("=" * 60)
print("    Jhames Rhonnielle T. Martin".center(60))
print("     BSIS 1A".center(60))
print("=" * 60)
print("\n")

print("starting na ung system", end="")
for i in range(15):
    print(".", end="", flush=True)
    import time
    time.sleep(0.1)
print("\n")

n = int(input("Enter number of students: "))
scores = []
print("\nEnter the scores one by one:")
for i in range(n):
    score = float(input(f"   Student {i+1}: "))
    scores.append(score)

print("\n" + "="*60)
print("All scores successfully recorded!".center(60))
print("="*60 + "\n")

while True:
    print("\n" * 50)
    print("=" * 60)
    print("         Jhames Rhonnielle T. Martin".center(60))
    print("                  BSIS 1A".center(60))
    print("=" * 60)
    print("\n            MAIN MENU")
    print("-" * 60)
    print("1. Display all scores")
    print("2. Count students who passed (≥75)")
    print("3. Show highest and lowest score")
    print("4. Search for a score")
    print("5. Insert new score")
    print("6. Delete a score")
    print("7. Show final list and EXIT")
    print("=" * 60)
    
    choice = input("\nSelect option (1-7): ")

    print("\nProcessing your request", end="")
    for i in range(10):
        print(".", end="", flush=True)
        import time
        time.sleep(0.08)
    print("\n")

    if choice == "1":
        print("2. All the scores")
        print("Scores:", end=" ")
        for s in scores:
            print(s, end="  ")
        print("\n")

    elif choice == "2":
        passed = 0
        for s in scores:
            if s >= 75:
                passed += 1
        print(f"3. Students who passed (≥75): {passed}\n")

    elif choice == "3":
        if scores:
            high = scores[0]
            low = scores[0]
            for s in scores:
                if s > high:
                    high = s
                if s < low:
                    low = s
            print(f"4. Highest score: {high}")
            print(f"   Lowest score : {low}\n")

    elif choice == "4":
        search = float(input("5. Enter score to search: "))
        found = False
        for s in scores:
            if s == search:
                found = True
                break
        if found:
            print(f"   {search} is FOUND!\n")
        else:
            print(f"   {search} is NOT found.\n")

    elif choice == "5":
        pos = int(input(f"6. Insert at position (0 to {len(scores)}): "))
        new = float(input("   Enter new score: "))
        scores.insert(pos, new)
        print("   Score inserted successfully!\n")

    elif choice == "6":
        delete = float(input("7. Enter score to delete: "))
        found = False
        for i in range(len(scores)):
            if scores[i] == delete:
                scores.pop(i)
                found = True
                break
        if found:
            print("   Score deleted!\n")
        else:
            print("   Score not found - nothing deleted.\n")

    elif choice == "7":
        print("\n" + "="*60)
        print("8. FINAL UPDATED LIST OF SCORES".center(60))
        print("="*60)
        print("Scores:", end=" ")
        for s in scores:
            print(s, end="  ")
        print("\n")
        print("="*60)
        print("Thank you! Program by Jhames Rhonnielle T. Martin".center(60))
        print("="*60)
        print("\nExiting in 3", end="")
        import time
        time.sleep(1)
        print(" 2", end="")
        time.sleep(1)
        print(" 1", end="")
        time.sleep(1)
        print("\n\nEnd")
        break

    input("Press Enter to continue...")
