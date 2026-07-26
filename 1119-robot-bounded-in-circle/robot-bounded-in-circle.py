class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        i =0
        pos =[0,0,1]
        while i != len(instructions):
            direc = pos[-1]
            if instructions[i] =='G':
                if direc>0:
                    pos[abs(direc)-1] +=1
                else:
                    pos[abs(direc)-1] -=1
            elif instructions[i] =='R':
                if abs(direc) == 1:
                    pos[-1] = (-2)*pos[-1]
                else:
                    pos[-1] = int(pos[-1]/2)
            else:
                if abs(direc) == 1:
                    pos[-1] = (2)*pos[-1]
                else:
                    pos[-1] = -int(pos[-1]/2)
            i+=1
        if pos == [0,0,1]:
            return True
        elif pos[-1] != 1:
            return True
        else:
            return False

                


