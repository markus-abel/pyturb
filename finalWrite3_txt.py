def write_resultst(t, meanX, meanY, meanZ, m2X, m2Y, m2Z, m3X, m3Y, m3Z, m4X, m4Y, m4Z):

  finalResultst = open("Finalt.txt", "w")

  finalResultst.write("Time:")
  finalResultst.write(" ")
  finalResultst.write("MeanX:")
  finalResultst.write(" ")
  finalResultst.write("MeanY:")
  finalResultst.write(" ")
  finalResultst.write("MeanZ:")
  finalResultst.write(" ")
  finalResultst.write("Moment2X:")
  finalResultst.write(" ")
  finalResultst.write("Moment2Y:")
  finalResultst.write(" ")
  finalResultst.write("Moment2Z:")
  finalResultst.write(" ")
  finalResultst.write("Moment3X:")
  finalResultst.write(" ")
  finalResultst.write("Moment3Y:")
  finalResultst.write(" ")
  finalResultst.write("Moment3Z:")
  finalResultst.write(" ")
  finalResultst.write("Moment4X:")
  finalResultst.write(" ")
  finalResultst.write("Moment4Y:")
  finalResultst.write(" ")
  finalResultst.write("Moment4Z:")
  finalResultst.write("\n")
  
  i = 0
  while i < 100:
  
    finalResultst.write(str(t[i]))
    finalResultst.write(" ")
    finalResultst.write(str(meanX[i]))
    finalResultst.write(" ")
    finalResultst.write(str(meanY[i]))
    finalResultst.write(" ")
    finalResultst.write(str(meanZ[i]))
    finalResultst.write(" ")
    finalResultst.write(str(m2X[i]))
    finalResultst.write(" ")
    finalResultst.write(str(m2Y[i]))
    finalResultst.write(" ")
    finalResultst.write(str(m2Z[i]))
    finalResultst.write(" ")
    finalResultst.write(str(m3X[i]))
    finalResultst.write(" ")
    finalResultst.write(str(m3Y[i]))
    finalResultst.write(" ")
    finalResultst.write(str(m3Z[i]))
    finalResultst.write(" ")
    finalResultst.write(str(m4X[i]))
    finalResultst.write(" ")
    finalResultst.write(str(m4Y[i]))
    finalResultst.write(" ")
    finalResultst.write(str(m4Z[i]))
    finalResultst.write("\n")

    i = i + 1

  finalResultst.close()

