import random;

def check1():
    if(list1[0] == 'X' and list1[1] == 'X' and list1[2] == 'X'):
        print "Player 1 is Winner";
        return 1;
    elif(list1[3] == 'X' and list1[4]=='X' and list1[5]=='X'):
        print "Player 1 is Winner";
        return 1;
    elif(list1[6]=='X' and list1[7]=='X' and list1[8]=='X'):
        print "Player 1 is Winner";
        return 1;
    elif(list1[0]=='X' and list1[3]=='X' and list1[6]=='X'):
        print "Player 1 is Winner";
        return 1;
    elif(list1[1]=='X' and list1[4]=='X' and list1[7]=='X'):
        print "Player 1 is Winner";
        return 1;
    elif(list1[2]=='X' and list1[5]=='X' and list1[8]=='X'):
        print "Player 1 is Winner";
        return 1;
    elif(list1[0]=='X' and list1[4]=='X' and list1[8]=='X'):
        print "Player 1 is Winner";
        return 1;
    elif(list1[2]=='X' and list1[4]=='X' and list1[6]=='X'):
        print "Player 1 is Winner";
        return 1;
    else:
        return 0;

def check2():
    if(list1[0]=='O' and list1[1]=='O' and list1[2]=='O'):
        print "Computer is Winner";
        return 1;
    elif(list1[3]=='O' and list1[4]=='O' and list1[5]=='O'):
        print "Computer is Winner";
        return 1;
    elif(list1[6]=='O' and list1[7]=='O' and list1[8]=='O'):
        print "Computer is Winner";
        return 1;
    elif(list1[0]=='O' and list1[3]=='O' and list1[6]=='O'):
        print "Computer is Winner";
        return 1;
    elif(list1[1]=='O' and list1[4]=='O' and list1[7]=='O'):
        print "Computer is Winner";
        return 1;
    elif(list1[2]=='O' and list1[5]=='O' and list1[8]=='O'):
        print "Computer is Winner";
        return 1;
    elif(list1[0]=='O' and list1[4]=='O' and list1[8]=='O'):
        print "Computer is Winner";
        return 1;
    elif(list1[2]=='O' and list1[4]=='O' and list1[6]=='O'):
        print "Computer is Winner";
        return 1;
    else:
        return 0;


def show():
    print list1[0:3],"\n\n",list1[3:6],"\n\n",list1[6:9];

n=0;
ch='y';
while(ch == 'y' or ch == 'Y'):
    list1=['-','-','-','-','-','-','-','-','-'];
    print list1[0:3],"\n\n",list1[3:6],"\n\n",list1[6:9];
    fill=1
    for i in range(1,10):
        if((i % 2) == 0):
            while(fill):
                c=random.randint(1,9);
                if(list1[c-1] == '-'):
                    list1[c-1]='O';
                    break;
                else:
                    continue;
            show();
            if(i >= 4):
                n=check2();
                if(n == 1):
                    break;
                        
            
            
        else:
            fill=1
            print "Player 1 Chance: Enter position: ";
            while(fill):
                c=int(raw_input());
                if(list1[c-1] == '-'):
                    list1[c-1]='X';
                    break;
                else:
                    print "Try Again!"
                    continue;
            #show();
            if(i >= 4):
                n=check1();
                if(n == 1):
                    break;
    print "GAME OVER!!!!";
    print "------------------------------------------------------------------------";
    ch=raw_input("Do u want to continue?");
    

