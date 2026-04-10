#Chapter 3 practice
# Linhe Sun

def main():
    # practice 3-1
    friends = ['lijian huang', 'yulin niu', 'hua li', 'hanlin wang']
    print(friends[0].title())
    print(friends[1].title())
    print(friends[-2].title())
    print(friends[-1].title())

    # practice 3-2
    print(friends[0].title() + ", long time no see!")
    print(friends[1].title() + ", long time no see!")
    print(friends[-2].title() + ", long time no see!")
    print(friends[-1].title() + ", long time no see!")

    # practice 3-3
    travelmood = ['by bike', 'by foot', 'by bus', 'by metro', 'by taxi']
    print("I would like to go to work " + travelmood[0] + ".")
    print("I would like to go to work " + travelmood[1] + ".")
    print("I would like to go to work " + travelmood[2] + ".")
    print("I would like to go to work " + travelmood[-2] + ".")
    print("I would like to go to work " + travelmood[-1] + ".")

    print("\n")
    # practice 3-4
    invite = ['lijian huang', 'yulin niu', 'hua li', 'hanlin wang']
    print("I would like to invite " + invite[0].title() + " to dinner.")
    print("I would like to invite " + invite[1].title() + " to dinner.")
    print("I would like to invite " + invite[2].title() + " to dinner.")
    print("I would like to invite " + invite[3].title() + " to dinner.")

    # practice 3-5
    print(invite[0].title() + " cannot come.")
    invite[0] = "jiaxin luo"
    print("I would like to invite " + invite[0].title() + " to dinner.")
    print("I would like to invite " + invite[1].title() + " to dinner.")
    print("I would like to invite " + invite[2].title() + " to dinner.")
    print("I would like to invite " + invite[3].title() + " to dinner.")

    # practice 3-6
    print("Now I have found a larger table. I can invite more people!")
    invite.insert(0, 'qiaoxian li')
    invite.insert(2, 'xueqing fang')
    invite.append('lijun xu')
    # print(len(invite)) # 7
    for i in range(0, len(invite)):
        # print(i) #0-6
        print("I would like to invite " + invite[i].title() + " to dinner.")

    # practice 3-7
    print("The new table cannot be dilivered in time. I can invite only two persons!")
    while len(invite) > 2:
        poped_invite = invite.pop()
        print(poped_invite.title() + ", sorry I cannot invite you anymore.")

    for i in range(0, len(invite)):
        print(invite[i].title() + ", I'm glad to inform you that you are still invited.")

    del invite[0]
    del invite[0] # now the [1] become [0]
    print(invite)

    print("\n\n\n")
    # practice 3-8
    places = ['Tokyo', 'Chongqing', 'New York', 'Paris', 'London', 'Haifa']
    print(places)
    print(sorted(places))
    print(places)
    print(sorted(places, reverse = True))
    print(places)
    places.reverse()
    print(places)
    places.reverse()
    print(places)
    places.sort()
    print(places)
    places.sort(reverse = True)
    print(places)

    # practice 3-9
    invite = ['lijian huang', 'yulin niu', 'hua li', 'hanlin wang']
    invite.insert(0, 'qiaoxian li')
    invite.insert(2, 'xueqing fang')
    invite.append('lijun xu')
    print("I invited " + str(len(invite)) + " friends to dinner.")

    # practice 3-10
    rivers = ['Yellow River', 'Yangzi River', 'Huai River', 'Heilong River', 'Guo River']
    print(rivers)
    del rivers[0]
    print(rivers)
    rivers.append('Qinhuai River')
    print(rivers)
    poped_rivers = rivers.pop()
    print(rivers)
    print(sorted(rivers))
    rivers.reverse()
    print(rivers)
    rivers.sort()
    print(rivers)
    rivers.sort(reverse = True)
    print(rivers)

    # practice 3-11
    print(rivers[4])
    nations = []
    print(nations[-1])

if __name__ == "__main__":
    main()