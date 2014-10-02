<<<<<<< HEAD
<<<<<<< HEAD
License:
 /*
    deasis-todolist: To-do list that manages and emails items in the list.
    Copyright (C) 2014  Kevin De Asis deasis@ualberta.ca

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

============================================================


  This assignment investigates the impact of error detection and error correction encoding,
on the thoroughput of a possibly unreliable communications channel. Investigation of the topic of this assignment
 was done through the use of a simulation program, which was modeled to imitate the conditions
of passing bits through an error prone channel. In short, we are looking at the successful delivery of a message
and the time associated with it, and how it is affected by error correction/detection algorithms. 
However, it is important to note that there are some assumptions made when running the simulator. Some of the assumptions 
made are based on the constraints imposed by the specification for the model, which are bits will have identical and
independent probability of having an error. This suggests that instances of burst errors are removed from the simulation, wherein
the probbability of a bit in error can also be dependent on other bits. The bits in the simulator are not
actually generated, instead bits are statistically represented by a random number generator, to represent error,
bits are in error when they overcome a constant variable that is  a probability representing the threshold for bit error.

	Hamming's Single-Bit Error Correction was used as the error detection scheme for this topic.
The actual scheme was not implemented in this assignment, but instead its nature was observed by being abstracted
in terms of implementation. So, instead of creating instances of data messages in bits and encoding it for HSBC
we use statistics to analyze the properties of what happens in the process of transmitting data with HSBC schema.
Some of the constraints created in the simulator was initialized by the user, which are
the feedback time, number of blocks per frame, the size of the frame, probability that a bit is in error, the length of the
simulation, and the number of trials; In each run of the program these constraints are assumed to be
constant.

	The significane of this topic is to research the impact of error correction/control schema, specifically
the HSBC, on the reliability of the algorithm in terms of accuracy and performance. This impact is observed through
different reliability of communication channels from high channel noise to low channel noise, wherein 
error may have been introduced during transmission. The simulation looks at the weight of the accuracy 
of error correction versus the weight of error detection, with respect to performance. The test results are shown
below, which includes comments and observations about the tests.

=======
CMPUT333A1

This is assignment 1. 
>>>>>>> 36d1969a43685db4af1fc3bc883de1ae5c72bdc9
=======
CMPUT 313 Assignment 1 ..
>>>>>>> 6f38e6dc7cbd2923905f61dc9731985e1863371c
