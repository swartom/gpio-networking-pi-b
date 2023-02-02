# gpio-networking-pi-b
Code for a CompSoc Workshop, two pis communicating concurrently via gpio pins as an introduction to networking from fundamentals. A partially modified Idea given to me by [moddedTechnic](https://github.com/orgs/LUCompSoc/people/moddedTechnic).

# The Pitch
Two Pi's are connected via full duplex. Each Pi has 3 controllable LED lights. Each reciver connection has an LED in Paralell so that the Student can see the data traveling across the network.
The Student is going to create two circuits (Diagram Available in the Images). I've written/I am writing some python code that abstracts the circuit connection stuff a little, and allows them to focus
on writing a protocol to communicate between the devices.

# Challenge Sections

## 1 - Simplex Connection
The Student will build a principal and an agent node, the principal will broadcast a number between 0 and 7 build a way to communicate between the two, a protocol.
The Student will get a basic example of the system, they will be incoraged to create a reusable solution.

## 2 - Return Message
The Student will continue to use a principal and agent model but with using the full duplex transmission allows the user to circuit switch, communicating back with the origin of the one-way numbers to return the speed at which it should send the next connection.

## 3 - Packet Switching
Using the full duplex connection, the student will build a set of two headers, allowing for two different protocols to be used, one made to control the speed of the program, one for the number.

> the purpose of this is to develop an understanding of networks, connections within networks & how packets work.

# Supporting Resources
- The Python wrapper should be loaded onto a Raspberry OS image along with some CompSoc Branding, this is flashed onto two different SD cards. Docs for the Wrapper is included in the package.
- This project was/will be trialed prior to it being ran. Thanks to [moddedTechnic](https://github.com/orgs/LUCompSoc/people/moddedTechnic) for volunteering.
- The Powerpoints are located in `/Powerpoints`.
