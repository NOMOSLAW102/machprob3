import numpy as np

def array(z):
    x=z[:,0]
    y=z[:,1]
    for n in range(len(z)):
        fit=np.polyfit(x,y,n)
        val=np.polyval(fit,x)    
        alg=np.linalg.norm(y-val)    
        d=[n,alg]
        if n==0:        
            m=d
        elif m[1] >= d[1]:        
            z = d[0]
    p=np.polyfit(x,y,z)
    print('Best Coefficents: ',p)
    
z = input("Input an nx2 matrix for example: 'np.array([[2,3],[4,1]])'.\nType here!: ")          
array(eval(z))    

    