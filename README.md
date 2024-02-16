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

![+ (2)](https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147051108/372b4e67-da85-48e5-985e-317f4e65b7a2)

After the design of the overall system was udnerstood we set out to develop the various parts of the system. The first thing we did was decide on how we could plan the coming days and which thigns we need to code and design. THe majority of our time was spent coding and troubleshooting. 

https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147051108/d559d898-63ff-43e6-9fdb-b9c481195c02

**The main tasks we completed were:**

- Connecting the TAPO Plug to the Python script
- Sending information from plug to the NodeRed
- Creating a visualization based on data from plug using P5js
- Creating an online dashboard from NodeRed

**Main issues we ran into:**

- Raspberry Pi connection as main brain, the problem here was that after we shut down the Pi once it was set up it stopped working. We tried multiple things to get it fixed but as it wasnt working at the moment for this challenge we decided to shift focus and run the programs off one laptop for now. The idea behind this is that if we can use one laptop using websocket and POST to send messages to different interfaces once the Pi is up and running we will be able to shift the current systems to the Pi computer.
  ![IMG-20240216-WA0005](https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147051108/7173b2a2-cddc-4a8e-b9f8-44c9870418cf)
  
- Using Mosquitto MQTT. The idea at the start was to use websocket and POST to test the code and the connections before shifting to MQTT, however when we tried to alter the codes and get the libraries running we ran into the problem that it didn't want to connect through the IP adress. We feel that this might have to do with the firewalls and security measures on our laptops so in the future we want to see what would happen if we change the main system to the Pi and then test the current code and see afterwards if we could shift.

- Using NodeRed to send data to P5js. This is something we really though would be easy to do but as we coded further we realized that websocket node didn't work with P5js as it was not considered secure. As we also could not figure out MQTT this meant it wasn't possible to connect directly through Nodered and for the moment we used two different python scripts running at the same time.

### Final Result
**Connecting to Tapo:**

The first step and first result we realized was connecting to the TAPO plug via python code and reading the data. This was essential for all further steps and the code that reads this data is shared above called MeasurerTapo. This is already a fun tool if you want to create your own little dashboard of energy and need to grab the data from the device as currently you can only access the data in a closed system of the app.

**Printed Case Pi:**

At the beginning of the challenge we also realized that while this would be mostly software development we wanted to use the 3d printers in some way. We noticed that the Raspberry Pi that we wanted to use was very unprotected at the moment and therefore decided to print a snapfit case to protect all the hardware. This design can be found above and the final printed case is seen below. 
![Term 2 - Frame 2](https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147051108/6c1f384e-97b7-43f9-b3f5-40dccf836d9c)

**Visual Representation:**

The visual representation of our data was designed using P5.js. We created a code that can be found above in the file Visual Representation. It is made to run off P5js but can also be used directly on websites if needed. First the python code connects to the tapo plug and then uses websocket to send the value of todays energy to the P5js script. Here the energy is then mapped and converted into an amount of particles that need to be added. With this in mind the busier the drawing the more energy that is being consumed at that given moment. 

![image](https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147051108/140c7e0e-f6f4-43a9-af5e-58078e831214)

**Dashboard:**

The dashboard is still at the beginning stages of development but for now we have managed to connect our incoming data to a dashboard using NodeRed. The current state of our dashboard is seen below. If you want to create your own nodered the code that we used for our flow is shared above. This includes a small part that is focussed on the beginning steps of using a chatbot to talk to us based on the energy usage.

![WhatsApp Image 2024-02-16 at 12 34 13_856bacb5](https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147051108/6f2cbd90-a71b-411f-9870-66dae587cc19)

### Thinking Further

**Connection to Telegram**

A key point for the future of our design was to create a messaging services that would eventually become an AI and learn from a persons energy habits and start a conversation with that person. The first step we decided to try out was to get a very basic telegram bot to send a message based on our usage. We got to the point that we had a bot that could send a person a chat message if we injected the message. Currently we are still trying to determine how we could grab the relevant data and prompt messages based on that. 
![WhatsApp Image 2024-02-16 at 12 52 08_92e3ca76](https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147051108/a73ca4f1-297a-446c-88c8-86aecf50127e)
![Dan the energy man](https://github.com/Oliver-Lloyd-MDEF/MDEF-Microchallenge-1-Energy-Monitors/assets/147057296/0b78bf99-f094-4c97-ab83-7db4e9d5a7a3)


**Physical Device**

The physical device is part of our personal goal to create opensourced energy monitors that people could make at home if they want that can be used in a non-intrusive and easy manner. The goal is that instead of having many plugs in all sockets there would be a devices that can clamp onto a wire in the distributor box and that way all energy could be measured. With this in mind we have started to research potential solutions and necessary technology. We have found many helpful tools that we could use and are excited to try and develop this aspect further. 
