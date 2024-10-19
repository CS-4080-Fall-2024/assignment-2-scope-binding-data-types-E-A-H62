"""References: https://medium.com/@ekollie324/how-to-build-a-rubiks-cube-in-python-c3bd19cbcd73
    Based on the pseudocode from the repository, I had a good idea of where to start implementing this Rubik's cube.
    However, I was more than a little confused about how exactly to implement the rotations of the cube.
    Using the reference helped give me a hint about one of the simpler ways to rotate a face of the cube.
    From there, I just had to translate the way I visualized rotating a face into Python code.
"""
# import kociemba # (library to help solve rubik's cubes)

class Cube:

    # init method initializes cube data structure
    def __init__(self, size):
        # initializes size of cube
        self.size = size
        # initializes face values of each side of cube as 2D array of string elements
        # 'F' represents tiles originally starting in the front face
        # 'B' represents tiles originally starting in the back face
        # 'L' represents tiles originally starting in the left face
        # 'R' represents tiles originally starting in the right face
        # 'U' represents tiles originally starting in the up/top face
        # 'D' represents tiles originally starting in the down/bottom face
        self.cube = {
            "front" : [['F' for i in range(size)] for i in range(size)],
            "back" : [['B' for i in range(size)] for i in range(size)],
            "left" : [['L' for i in range(size)] for i in range(size)],
            "right" : [['R' for i in range(size)] for i in range(size)],
            "up" : [['U' for i in range(size)] for i in range(size)],
            "down" : [['D' for i in range(size)] for i in range(size)]
        }

    # method to rotate a face in the clockwise direction
    def rotateFaceCW(self, face):
        # traverses each row of 2D array
        for i in range(self.size):
            # traverses each col of array
            for j in range(i, self.size):
                # swaps values in a way similar to transposing elements in a matrix
                # helps rotate images by 90 degrees
                self.cube[face][i][j], self.cube[face][j][i] = self.cube[face][j][i], self.cube[face][i][j]
        # reverses rows of rotated elements in face so rotation reflects correct order
        for i in range(self.size):
            self.cube[face][i].reverse()

    # method to rotate top face by 90 degrees clockwise
    # considers changes to adjacent faces
    def rotateUpCW(self):
        # calls method to rotate top face
        self.rotateFaceCW("up")
        # initializes temp row to hold values in front face
        tempRow = self.cube["front"][0]
        # first row of right face becomes first row of front face
        self.cube["front"][0] = self.cube["right"][0]
        # first row of back face becomes first row of right face
        self.cube["right"][0] = self.cube["back"][0]
        # first row of left face becomes back row of front face
        self.cube["back"][0] = self.cube["left"][0]
        # first row of (origina) face becomes first row of left face
        self.cube["left"][0] = tempRow

    # method to rotate bottom face by 90 degrees clockwise
    # considers changes to adjacent faces
    def rotateDownCW(self):
        # calls method to rotate bottom face
        self.rotateFaceCW("down")
        # initializes temp row to hold values of front face
        initial = self.cube["front"][-1]
        # last row of left face becomes last row of front face
        self.cube["front"][-1] = self.cube["left"][-1]
        # last row of back face becomes last row of left face
        self.cube["left"][-1] = self.cube["back"][-1]
        # last row of right face becomes last row of back face
        self.cube["back"][-1] = self.cube["right"][-1]
        # last row of (original) front face becomes last row of right face
        self.cube["right"][-1] = initial

    # method to rotate right face by 90 degrees clockwise
    # considers changes to adjacent faces
    def rotateRightCW(self):
        # calls method to rotate right face
        self.rotateFaceCW("right")
        # variables holds size (sidelength) of cube
        size = self.size
        # initializes temp array to hold values of top face's last col
        tempCol = [self.cube["up"][i][-1] for i in range(size)]
        # for loop to iterate through each row in col
        for i in range(size):
            # last col of front face becomes last col of top face
            self.cube["up"][i][-1] = self.cube["front"][i][-1]
            # last col of bottom face becomes last col of front face
            self.cube["front"][i][-1] = self.cube["down"][i][-1]
            # first col of back face becomes last col of bottom face
            self.cube["down"][i][-1] = self.cube["back"][size-1-i][0]
            # (original) last col of top face becomes first col of back face
            self.cube["back"][size-1-i][0] = tempCol[i]

    # method to rotate left face by 90 degrees clockwise
    # considers changes to adjacent faces
    def rotateLeftCW(self):
        # calls method to rotate left face
        self.rotateFaceCW("left")
        # variables holds size (sidelength) of cube
        size = self.size
        # initializes temp array to hold values of top face's first col
        tempCol = [self.cube["up"][i][0] for i in range(size)]
        # for loop to iterate through each row in col
        for i in range(size):
            # last col of back face becomes first col of top face
            self.cube["up"][i][0] = self.cube["back"][size-1-i][-1]
            # first col of bottom face becomes last col of back face
            self.cube["back"][size-1-i][-1] = self.cube["down"][i][0]
            # first col of front face becomes first col of bottom face
            self.cube["down"][i][0] = self.cube["front"][i][0]
            # (original) first col of top face becomes first col of front face
            self.cube["front"][i][0] = tempCol[i]

    # method to rotate front face by 90 degrees clockwise
    # considers changes to adjacent faces
    def rotateFrontCW(self):
        # calls method to rotate front face
        self.rotateFaceCW("front")
        # variables holds size (sidelength) of cube
        size = self.size
        # initializes temp array to hold values of top face's last row
        tempRow = [self.cube["up"][-1][i] for i in range(size)]
        # for loop to iterate through each col or row changed by rotation
        for i in range(size):
            # last col of left face becomes last row of top face
            self.cube["up"][-1][i] = self.cube["left"][i][-1]
            # first row of bottom face becomes last row of left face
            self.cube["left"][i][-1] = self.cube["down"][0][i]
            # first col of right face becomes first row of bottom face
            self.cube["down"][0][i] = self.cube["right"][i][0]
            # (original) last row of top face becomes first col of right face
            self.cube["right"][i][0] = tempRow[i]

    # method to rotate back face by 90 degrees clockwise
    # considers changes to adjacent faces
    def rotateBackCW(self):
        # calls method to rotate back face
        self.rotateFaceCW("back")
        # variables holds size (sidelength) of cube
        size = self.size
        # initializes temp array to hold values of top face's first row
        tempRow = [self.cube["up"][0][i] for i in range(size)]
        # for loop to iterate through each col or row changed by rotation
        for i in range(size):
            # last col of right face becomes first row of top face
            self.cube["up"][0][i] = self.cube["right"][i][-1]
            # last row of bottom face becomes last col of right face
            self.cube["right"][i][-1] = self.cube["down"][-1][i]
            # first col of left face becomes first row of bottom face
            self.cube["down"][0][i] = self.cube["left"][i][0]
            # (original) first row of top face becomes first col of left face
            self.cube["left"][i][0] = tempRow[i]

    # method to rotate a face in the counterclockwise direction
    def rotateFaceCCW(self, face):
        size = len(self.cube[face])
        # traverses each row of 2D array
        for i in range(size):
            # traverses each col of array
            for j in range(i, size):
                # swaps values in a way similar to transposing elements in a matrix
                # helps rotate images by 90 degrees counterclockwise
                self.cube[face][i][j], self.cube[face][j][i] = self.cube[face][j][i], self.cube[face][i][j]
        # reverses rows of rotated elements in face so rotation reflects correct order
        self.cube[face].reverse()

    # method to rotate top face by 90 degrees counterclockwise
    # considers changes to adjacent faces
    def rotateUpCCW(self):
        # calls method to rotate top face
        self.rotateFaceCCW("up")
        # initializes temp row to hold values in front face
        tempRow = self.cube["front"][0]
        # first row of left face becomes first row of front face
        self.cube["front"][0] = self.cube["left"][0]
        # first row of back face becomes first row of left face
        self.cube["left"][0] = self.cube["back"][0]
        # first row of right face becomes back row of front face
        self.cube["back"][0] = self.cube["right"][0]
        # first row of (origina) face becomes first row of right face
        self.cube["right"][0] = tempRow

    # method to rotate bottom face by 90 degrees counterclockwise
    # considers changes to adjacent faces
    def rotateDownCCW(self):
        # calls method to rotate top face
        self.rotateFaceCCW("down")
        # initializes temp row to hold values in front face
        tempRow = self.cube["front"][-1]
        # last row of right face becomes last row of front face
        self.cube["front"][-1] = self.cube["right"][-1]
        # last row of back face becomes last right of front face
        self.cube["right"][-1] = self.cube["back"][-1]
        # last row of left face becomes last row of back face
        self.cube["back"][-1] = self.cube["left"][-1]
        # last row of (original) right face becomes last row of left face
        self.cube["left"][-1] = tempRow

    # method to rotate right face by 90 degrees counterclockwise
    # considers changes to adjacent faces
    def rotateRightCCW(self):
        # calls method to rotate face
        self.rotateFaceCCW("right")
        # variables holds size (sidelength) of cube
        size = self.size
        # initializes temp array to hold values of front face's last col
        tempCol = [self.cube["front"][i][-1] for i in range(size)]
        # for loop to iterate through each row in col
        for i in range(size):
            # last col of top face becomes last col of front face
            self.cube["front"][i][-1] = self.cube["up"][i][-1]
            # first col of back face becomes last col of top face
            self.cube["up"][i][-1] = self.cube["back"][2 - i][0]
            # last col of bottom face becomes first col col of back face
            self.cube["back"][2 - i][0] = self.cube["down"][i][-1]
            # last col of (original) front face becomes last col of bottom face
            self.cube["down"][i][-1] = tempCol[i]

    # method to rotate left face by 90 degrees counterclockwise
    # considers changes to adjacent faces
    def rotateLeftCCW(self):
        # calls method to rotate left face
        self.rotateFaceCCW("left")
        # variables holds size (sidelength) of cube
        size = self.size
        # initializes temp array to hold values of top face's first col
        tempCol = [self.cube["front"][i][0] for i in range(size)]
        # for loop to traverse through each row in col
        for i in range(size):
            # first col of bottom face becomes first col of front face
            self.cube["front"][i][0] = self.cube["down"][i][0]
            # last col of back face becomes first col of bottom face
            self.cube["down"][i][0] = self.cube["back"][2 - i][-1]
            # first col of top face becomes last col of back face
            self.cube["back"][2 - i][-1] = self.cube["up"][i][0]
            # first col of (original) front face becomes first col of top face
            self.cube["up"][i][0] = tempCol[i]

    # method to rotate front face by 90 degrees counterclockwise
    # considers changes to adjacent faces
    def rotateFrontCCW(self):
        # calls method to rotate front face
        self.rotateFaceCCW("front")
        # variable holds size (sidelength) of cube
        size = self.size
        # initializes temp array to hold values of top face's first row
        tempRow = [self.cube["up"][-1][i] for i in range(size)]
        # for loop to iterate through each col or row changed by rotation
        for i in range(size):
            # first col of right face becomes last row of top face
            self.cube["up"][-1][i] = self.cube["right"][i][0]
            # first row of bottom face becomes first col of right face
            self.cube["right"][i][0] = self.cube["down"][0][i]
            # last col of left face becomes first row of bottom face
            self.cube["down"][0][i] = self.cube["left"][i][-1]
            # (original) last row of top face becomes last col of left face
            self.cube["left"][i][-1] = tempRow[i]

    # method to rotate back face by 90 degrees counterclockwise
    # considers changes to adjacent faces
    def rotateBackCCW(self):
        # calls method to rotate back face
        self.rotateFaceCCW("back")
        # variable holds size (sidelength) of cube
        size = self.size
        # initializes temp array to hold values of top face's first row
        tempRow = [self.cube["up"][0][i] for i in range(size)]
        # for loop to iterate through each col or row changed by rotation
        for i in range(size):
            # first col of left face becomes first row of top face
            self.cube["up"][0][i] = self.cube["left"][i][0]
            # first row of bottom face becomes first col of left face
            self.cube["left"][i][0] = self.cube["down"][0][i]
            # last col of right face becomes first row of bottom face
            self.cube["down"][0][i] = self.cube["right"][i][-1]
            # (original) first row of top face becomes last col of right face
            self.cube["right"][i][-1] = tempRow[i]

    # method to solve randomly rotated Rubik's cube
    # utilizes the kociemba library (has to be installed) to solve a cube
    """def to_kociemba_string(self):
        result = ''
        for face in ["up", "left", "front", "right", "back", "down"]:
            for row in self.cube[face]:
                for square in row:
                    result += square
        return result

    def solveCube(self):
        try:
            state = self.to_kociemba_string()
            solution = kociemba.solve(state)
            print("Solution found:", solution)
            return solution
        except Exception as e:
            print("Error solving the cube:", e)
            return None"""

    def printCube(self):
        # traverses each face in the cube
        for face in self.cube:
            # prints out which cube face is displayed
            print(f"{face}:")
            # prints out cube row-by-row 
            for row in self.cube[face]:
                print(row)
            print()

# creates new 3x3 Rubik's cube
rubixC = Cube(3)

# rotates Rubik's cube
rubixC.rotateFrontCW()
rubixC.rotateBackCW()
rubixC.rotateLeftCW()
rubixC.rotateRightCW()
rubixC.rotateUpCW()
rubixC.rotateDownCW()

# prints scrambled cube
print("Scrambled cube:")
rubixC.printCube()

# code to print solved Rubik's cube (if solve method functions)
"""print("Solved cube:")
rubixC.solveCube()
rubixC.printCube()"""
