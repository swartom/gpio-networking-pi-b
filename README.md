# gpio-networking-pi-b
Code for a CompSoc Workshop, two pis communicating concurrently via gpio pins as an introduction to networking from fundamentals. A partially modified Idea given to me by [moddedTechnic](https://github.com/orgs/LUCompSoc/people/moddedTechnic).

# The Pitch
Two Pi's are connected via full duplex. Each Pi has 3 controllable LED lights. Each reciver connection has an LED in Paralell so that the Student can see the data traveling across the network.
The Student is going to create two circuits (Diagram Available in the Images). I've written/I am writing some python code that abstracts the circuit connection stuff a little, and allows them to focus
on writing a protocol to communicate between the devices.

# Challenges
1) The Student should be able to write a protocol that, given a random number between 0 and 7, that number should be displayed on the other pi (simplex connection).
2) The Student should then make it so that both pis send this request to each other waiting between for a return request (half Duplex).
3) The Student should then implement a full duplex connection between them, they'll need to create a buffer to store the information comming in (it wont be big enough!).
3) The Student should then implement data throttling on a duplex connection with one line for each i.e. throttling and data (cicuit switching).
4) The Student should implement a basic packet switching system through the creation of their own headers, allowing for concurrent communication about both the speed and the Result.

> the purpose of this is to develop an understanding of networks, connections within networks & how packets work.
