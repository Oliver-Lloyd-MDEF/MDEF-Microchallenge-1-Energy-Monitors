Here you will find al the documentation for the first Microchallenge of the MDEF program 2023 - 2024 undertaken by Carlotta Hylkema and Oliver Lloyd :D 

### Discovering our interests
We have been collaborating in the past month and already had talked about our shared interest in energy and the perception of this. With this challenge we decided to take a quick look at our interests and shared goals during the projects. 

![image](https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147051108/7624acf2-746c-4f88-81b0-3a2cfb269d26)

It quicjly became clear that we wanted to continue and use these microchallenges to further our research into energy. The focus was to create a series of software/hardware that allow people to take control of their energy consumption and gain insight into their lifes. The overlying goal of our projects is to **"create a system that empowers/enables people to understand and (potentially) reduce their energy consumption footprint without reducing their quality of life".**

### Ideating on first Challenge

Within this challenge there were still a lot of unknowns in what we exactly wanted to achieve. We decided to brainstorm and ideate on both the final product and the main function.

![Screenshot 2024-02-16 101435](https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147051108/88e30bc9-9468-4d94-b105-00adb115a045)

Finally as we talked and discussed we realized that the main task for the first challenge would be to connect to an existing energy monitor and use that data to create easy ways for people to comprehend visual data but also in the trend of what if you could have a conversation with your house. For this particular challenge we decided to focus on connecting with an existing TAPO smartplug and collecting and visualizing that data in a fun and informative way. The main goal was "An open source developed household electricity consumption meter based on arduino, that can display consumption in a visual way and allow people to interact with and understand consumption in a collaborative way. "An open source developed household electricity consumption meter based on arduino, that can display consumption in a visual way and allow people to interact with and understand consumption in a collaborative way."

### Developping the software

The first step for us on the journey of this project was understanding the whole system we wanted to build and which part was essential for this challenge. We drew a diagram of all the part and then discussed which worked for the current themes and timeframe. The diagram shown below is the whole system and we decided to focus on the top part for now and leave the AI interaction for another challenge. 
![+ (2)](https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147051108/4b3b25f8-20cc-4264-aa22-7575a6036186)


After the design of the overall system was udnerstood we set out to develop the various parts of the system. The first thing we did was decide on how we could plan the coming days and which thigns we need to code and design. THe majority of our time was spent coding and troubleshooting. 

https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147051108/d559d898-63ff-43e6-9fdb-b9c481195c02

**The main tasks we completed were:**
- Connecting the TAPO Plug to the Python script
- Sending information from plug to the NodeRed
- Creating a visualization based on data from plug using P5js
- Creating an online dashboard from NodeRed

**Main issues we ran into:**
- Raspberry Pi connection as main brain, the problem here was that after we shut down the Pi once it was set up it stopped working. We tried multiple things to get it fixed but as it wasnt working at the moment for this challenge we decided to shift focus and run the programs off one laptop for now. The idea behind this is that if we can use one laptop using websocket and POST to send messages to different interfaces once the Pi is up and running we will be able to shift the current systems to the Pi computer.
  
- Using Mosquitto MQTT. The idea at the start was to use websocket and POST to test the code and the connections before shifting to MQTT, however when we tried to alter the codes and get the libraries running we ran into the problem that it didn't want to connect through the IP adress. We feel that this might have to do with the firewalls and security measures on our laptops so in the future we want to see what would happen if we change the main system to the Pi and then the 
