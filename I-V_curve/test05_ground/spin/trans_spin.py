
#######################################################################non_spin
def non_spin():
    
    print('TS.Volatge','\t','Current')
    
    vol_list=[]
    cur_list=[]
    
    for k in range (0,num_point): 
        yy=tmp_list1[k]
        zz=tmp_list3[k]
        dir_path = os.path.abspath("%s" %yy)
        os.chdir("%s" %dir_path)
        
        os.system("cp ./**.TRANS_Left-Right ./siesta_trans")
        #print("What is the TS.Volatge value in your calculation? Please enter that in only number.")
        Voltage = zz
        
        f1 = open("./siesta_trans", "r")
        
        for i in range(0,3):
            line = f1.readline()
        
        TMP_list1 = []
        TMP_list2 = []
        TMP_list3 = []
        x = 0
        
        while True:
            a = f1.readline().rstrip('\n')
            b = " ".join(a.split())
            c = b.split(' ')
            if not a: break
            x = x+1
            TMP_list1.append(c)
        
        for i in range (0,x):
            TMP_list2 = list(map(float,TMP_list1[i]))
            TMP_list3.append(TMP_list2)
        
        k = 8.617343e-5
        T = 300
        VL = Voltage/2
        VR = -1*Voltage/2
        dE = TMP_list3[1][0]-TMP_list3[0][0]
    
    #    print("dE: %lf" %dE)
    
        for i in range (0,x):
            energy = TMP_list3[i][0]
            Dfd = (1/(1+math.exp((energy-VL)/(k*T))))-(1/(1+math.exp((energy-VR)/(k*T))))
            if Dfd < 1e-16:
                if Dfd > -1e-16:
                    Dfd = 0
            TMP_list3[i].append(Dfd)
        
        I = 0
        for i in range (0,x):
            I = I+(TMP_list3[i][1]*TMP_list3[i][2]*dE)
        
        TMP_list1 = [0 for _ in range (-1)]
        TMP_list2 = [0 for _ in range (-1)]
    
        I = I*38.7
    
        for i in range (0,x):
            TMP_list2 = list(map(str,TMP_list3[i]))
            TMP_list1.append(TMP_list2)
        
        V = str(f'{Voltage: .6f}')
        J = str(f'{I: .6f}')
    
        vol_list.append(V)
        cur_list.append(J)
    
    
        f1.close()
        
        os.system("rm ./siesta_trans")
    
        print('%lf' %zz,'\t','%lf' %I)
        
        os.chdir("%s" %base_path)

    #######################################################################print program state
    
    #os.system("find . -type f -name 'current' -exec cat {} + > V-I")
    print('##############################')
    print('post-progress done. write the V-I file')
    
    #######################################################################make plot file
    
    f3 = open("./V-I", "w")
    #f3.write('Voltage')
    #f3.write('\t')
    #f3.write('Current')
    #f3.write('\n')
    for i in range (0,num_point):
        f3.write(vol_list[i])
        f3.write('\t')
        f3.write(cur_list[i])
        f3.write('\n')
    f3.close()
#######################################################################non_spin-fin



non_spin()

os.system("rm ./list")

print('Program done. Plz check the V-I file')
