while True:
    answer = input("Would you like to play the Adventure Game? (yes/no) ")
    if answer.lower().strip() == "yes":
        answer = input(
            "You have wandered  into  one of the untamed forests of Western Washington. You find yourrself at a crossroads. Do you wish to go left or right? ").lower().strip()
        if answer == "right":
            answer = input("You stumble into an insane ax-wielding goat-man creature. Fight or Flight?")
            if answer == "fight" or "Fight":
                print("Thank God, you have come prepared. Your Glock 9mm beats rusty goat-axe.")
                answer = input(
                    "After enjoying some tasty mutton stew, you decide to get going. Go home or go to the left at the crossroads?")
                if answer == "home" or "Home":
                    answer = input(
                        "You go home and spend the rest of your life dying a painful death from Hoof-and-Mouth disease. Game over")
                else:
                    print("You traverse the path of beauty. You drink the pure silence and read the Signs engraved within nature. You see a majestic buck sip from the pristine waters of a brook. An arrow head erupts from your neck as a hunters arrow hits the wrong target. You die. Should have stayed home and watched netflix. Game over ")

            else:
                print("You make a run for it. The combination of the goat being a track and field champion from his college days plus you tripping over a tree root like an idiot results in a rusty axe between your shoulder blades. You lose")
        elif answer == "left" or "Left":
            print("You traverse the path of beauty. You drink the pure silence and read the Signs engraved within nature. You see a majestic buck sip from the pristine waters of a brook. An arrow head erupts from your neck as a hunters arrow hits the wrong target. You die. Should have stayed home and watched netflix. Game over")

        else:
            print("Reading comprehension skills not quite where they need to be, it seems. You lose")
    else:
        print("I'm sorry to hear that.")
        break