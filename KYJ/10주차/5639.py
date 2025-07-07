import sys
sys.setrecursionlimit(10 ** 6)

preorder = []
while True:
    try :
        preorder.append(int(sys.stdin.readline()))
    except:   #''일때 발생
        break 



def postorder(start, end):
    if start>=end:
        return
    
    root = preorder[start]

    right=start+1
    while right < end and preorder[right]<root:
        right=right+1
    
    postorder(start+1,right)

    postorder(right,end)

    print(root)

postorder(0,len(preorder))



