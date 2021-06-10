# Pi Trebuchet
Elisabeth Scharf and Abigail Paquette - Engineering 4 Repo & Documentation

[Trello Board](https://trello.com/b/15McbNyB/engineering-4-project)

[Calendar](https://jamboard.google.com/d/1JnHUE4IZWikT05Q0Ya0kpPUMJIv1QDpOZKAwVSAdiaQ/edit?usp=sharing) 

[Onshape Document](https://cvilleschools.onshape.com/documents/231c459fbc6840d3f00a1b9f/w/e7df1ab6ccf7a00b59ac0257/e/ae8347c1ef2b746ac703c727)


## Table of Contents

[Preliminary Brainstorming](https://github.com/Apaquet37/PiTrebuchet/blob/main/README.md#Brainstorming)

[Planning](https://github.com/Apaquet37/PiTrebuchet/blob/main/README.md#planning)

[Prototyping and Initial Designs](https://github.com/Apaquet37/PiTrebuchet/blob/main/README.md#prototyping-and-initial-designs)

[Schedule and Milestones](https://github.com/Apaquet37/PiTrebuchet/blob/main/README.md#schedule-and-milestones-see-trello-board-for-more-specific-tasks)

[Code](https://github.com/Apaquet37/PiTrebuchet/blob/main/README.md#code)

## Brainstorming
For Engineering 4, we have to create a project that uses the raspberry pi in some way. The typical project is pi in the sky, where you find some way to launch or levitate your pi into the sky, but we are not being held to those constraints this year. Here are some of the initial ideas we thought about:
```
- Launch pi into air and take measurements/pictures 
- Infrared power outage people sensor 
- Launch pi on a rocket and track and create a graphic of its motion
    - User interface 
    - Picture button
    - Math and data
- Vertical panorama
```
And here are some of the materials we have at our disposal:
```
Sensors/sources of input we have:
- Camera 
- Barometric pressure, altimeter, temperature
- Accelerometer and magnetometer
- Infrared 
```
We decided we like the Pi in the Sky idea, and defined the problem as having two broad possible solutions:
```
Two ideas:
1. Pi is launched externally and there is a user interface that displays and saves data/photos
2. Pi somehow keeps itself up and user interface functions as a controller
```
We liked option number two, and fleshed that out even more:
```
Ways to get pi in the air:
- Rocket
    - Combustible engine
    - Pressure powered (water, stomp)
- Catapult
    - Trebuchet
```
Before deciding to delve into the world of trebuchets.


## Planning

**Goal:** Create the most automated whipper trebuchet possible. [What is a whipper trebuchet?](https://www.youtube.com/watch?v=-gn2RGPqe_A&t=793s)

**Overview:**

How does a whipper trebuchet work?

Parts of a trebuchet

<img src="Media/PartsOfTrebuchet.png" width="500">

Launch process

<img src="Media/LaunchProcess.png" width="500">


Tasks usually completed by a human:

- Put in place the counterweight
- Load the sling with the projectile
- Set the launch angle 
- Pull the release pin 

Tasks we would like automate:

- Setting the launch angle 

<img src="Media/TrebuchetRelease.png" width="500">

- Pulling the release pin
  - Remote launch user interface
  - Pi's Flask webpage 
- Maybe:
  - Changing the weight in the counterweight

Constraints:

- It will be extremely difficult to reset the string on the trebuchet because the string will get caught
- Both emptying and refilling the counterweight would be extremely challenging
  - We have figured out how to lift marbles (which would be the weights) from the base of the treubuchet to the counterweight arm
  - The challenge is creating a container that can swing around without launching marbles, but be easily accessible for us to empty and refill according to the appropriate weight for the desired launch distance

<img src="Media/Marble%20Lift%20Mechanism.png" width="500">

**Vision/Description:** We are going to launch an object using a trebuchet we have designed. We will create a user interface that allows the user to input two main pieces of data: how far the trebuchet is from the target, and relatively how much force with which they would like for the projectile to hit the target. The Pi does the calculation and changes the launch angle to help acheive the desired outcome. Once the launch has been optimized, the user can press a button that will tell the Pi to release a pin and launch the object. The object whips around and flies through the air to hit the target. Then the Pi resets the launch angle and lets the user know that the trebuchet is ready to be reset. 

## Prototyping and Initial Designs
<img src="Media/cadTrebuchet.png" width="500"> <img src="Media/marbleProto2.GIF" width="500"> <img src="Media/trebuchetProto3.GIF" width="500"> <img src="Media/marbleMovingDrawing.png" width="500"> <img src="Media/planningJamboard.png" width="500"> <img src="Media/marbleRunScreenshot.png" width="500">

**User Interface**

<img src="Media/LaunchFlow.png" width="500">

**Release Pin Mechanism Ideas:**

<img src="Media/MechanicalSystemForReleasePin.png" width="500">

[Possible Release Pin Mechanism (3:06 to 3:40) ](https://www.youtube.com/watch?v=BVnrD9m3nSI&t=185s)


**Engineering Process:**
- [x] Identify problem or goal 
- [x] Identify resources and constraints
- [x] Brainstorm ideas
- [x] Pick a solution
- [x] Develop an initial design (pencil and paper, CAD, etc.)
- [x] Construct a prototype
- [x] Test your design
- [ ] Refine/optimize your design
- [ ] Present finished product 


## Schedule and Milestones (See Trello board for more specific tasks)

**Initial Calendar** 

<img src="Media/marchCalendar.png" width="700"> <img src="Media/AprilCalendar.png" width="700"> <img src="Media/mayCalendar.png" width="700">

**Milestones**

|Week|Elisabeth's Task|   Abby's Task   |Accomplished|Plans to catch up (if needed)|
|----|----------------|-----------------|------------|-----------------------------|
|March 8-12|Submit proposal and design parts for release pin|Submit proposal and finish pi assignments from beginning of year|Our proposal was submitted midweek, and we are starting to work in earnest on our project. The parts for the release pin mechanism were submitted Friday, and Abby will complete her pi assignments over the weekend.|Do pi assignments over the weekend.|
|March 15-19|Design release pin mechanism|Code release pin mechanism servo|One iteration of the release pin mechanism has been designed and lasercut, but scale was a bit off and testing still has to be done. The code for the servo has been started, but it also still needs to be worked on.|We are just going to continue to work hard and make sure to utilize time outside of class.|
|March 22-26|Build the trebuchet base|Research the math and physics behind the launch, work with the equations to optimize launch by changing release angle|The base went through several conceptual iterations, but we ended up going with a lasercut one comprised of two triangles that were connected by a u-shaped channel (made of bent acrylic) that would hold the Pi. The two biggest challenges with this (which continued into future weeks) were creating a two-piece axle to connect the tops of the triangles and learning how to design in 2D for something that would later be 3 dimensional.|
|March 29 - April 2|Begin work on the sling|Implement launch optimization in code (with release pin servo) and code launch servo|
|Spring Break| N/A | N/A |
|April 12-16|Design and assemble counterweight|Start working on flask user interface|
|April 19-23|Continue on counterweight and sling work|Add physical mechanisms into user interface, test and troubleshoot user interface|
|April 26-30|Designing and building the launch pin system|Testing, troubleshooting, and revising|
|May 3-7|Testing, troubleshooting, and revising|Testing, troubleshooting, and revising|
|May 10-14|Testing, troubleshooting, and revising|Testing, troubleshooting, and revising|
|May 17-21|Finalize everything and finish documentation|Finalize everything and finish documentation|


## Documentation: ## 

**Little lessons along the way**

E: In the midst of trying to sort through some mates to find an error, I realized that things would be so much easier if I had named my mates. 
Making that change has been helpful and has allowed me to troubleshoot more easily, especially as I add more and more pieces and more and more mates. 

<img src="Media/NamingMates.png" width="300">

E: Another tip for Onshape organization is to create folders to organize your part studios and assemblies within a single document. As we added more and more parts, it became challenging to scroll and find each particular part. I ended up with six folders and some sub-folders that told me where to go when looking for specific parts related to the different mechanisms on the trebuchet. 

<img src="Media/FolderPhoto.png" width="600">

Challenges we faced:
- Using the sheet metal tool to simulate bent acrylic
  - Learning how to do that in Onshape
  - Getting help from Dr. Shields
  - Editing the model
- Using a heat gun to bend acrylic 
  - Abby's experience doing that for the first time
  - Using a wooden block as a mold
- Designing an axle to stablize the arm
  - **Design challenge:** we had to be able to put the arm onto the axle, but also make sure that once it was on it would not shift from side to side. 
  - **Thought Process:** We only wanted rotational movement in one plane, but couldn't think how to effectively create walls on each side of the arm that would go on after the arm. We decided that the best plan would be to create a two-piece axle that would connect in the middle after the arm was already on. 
  - **Two-piece design solution:** The product was a two-piece axle where each side connected to one of the triangular walls and had a cone shape on the other end (specially designed to limit support material - just for you Dr. Shields!). The plan was to slide the arm onto a little part that stuck out from one of the sides and then to attach the two parts with deeply countersunk screws. 
  - **Revisions:** Creating a headless screw
  - Friction reduction: sanding and dry lubrication with graphite 
- Designing a mechanized moving pin
  - Finding a design
  - Replicating it in Onshape
  - Assembling it all in Onshape
  - Scale for dxf files... (lesson learned)
  - Current photos
- Correlating the servo values (-1 to 1) with the release pin angles (0-180deg) and omega (rad)
  - Protractor photo
  - Screenshot of the graph to find the relationship
- All the math... 
  - Energy & kinematics
  - New formula for omega
  - Adjustments to the new omega formula


##### Design #####

There were a few distinct aspects of the design:
1. PiHolder
2. Custom Axle
3. Arm
4. Release Pin Mechanism 

** 1. PiHolder ** 

The PiHolder presented a unique challenge because we planned on lasercutting the design first and then bending the acrylic afterwards. 

<img src="Media/ArmDesign.png" width="300">
<img src="Media/AxleCAD.png" width="300">
<img src="Media/FullAssembly.png" width="300">
<img src="Media/PiHolderDesign.png" width="300">
<img src="Media/RevolutionDiagram.png" width="300">
<img src="Media/NamingMates.png" width="300">
<img src="Media/Whiteboard1.jpg" width="300">
<img src="Media/Protractor.jpg" width="300">
<img src="Media/AngleMeasurements.JPG" width="300">

<img src="Media/ArmRotation.png" width="300">
<img src="Media/CustomBatteryHolder.png" width="300">
<img src="Media/DrawingTemplate.png" width="300">
<img src="Media/FullArmAssembly.png" width="300">
<img src="Media/FullAxle.png" width="300">
<img src="Media/FullTrebuchet.png" width="300">
<img src="Media/PiHolderPart.png" width="300">
<img src="Media/ScrewConnection.png" width="300">
<img src="Media/SheetMetalSketch.png" width="300">
<img src="Media/SheetMetalTest.png" width="300">


## Code
The goals of our code at the start of this project:
- A user puts the mass of a projectile and the desired distance they want their projectile to travel into a Flask user interface
- From that data, as well as other data and mathematical equations, the pi determines at what angle the release pin of the sling should be at
- Based on that angle generated (theta) a servo attached to the pin moves
- From there, a launch button will appear on the user interface, and when the user presses “launch” a second servo starts the launch
- Finally, the code would need processes at the end to reset the servos so they are ready for another launch
- <img src="Media/jamboard1.png" width="400">

Currently, at the end of the school year, the code is almost finished, but not quite done. All of the logic has been figured out, as well as the servo control, but everything hasn’t been put together and the Flask user interface is not up and running. In this repository there are multiple different programs and files that all do different things, but all the code is commented so it should be pretty easy to look through. 

Brief descriptions of important files:
- [angleTest.py](angleTest.py)
    - This code allows a user to type in a number between -1 and 1, and a servo will rotate to a corresponding angle. Then, the servo resets and another angle can be           entered.
    - <img src="Media/angleTest.png" width="300">
- [math.py](math.py)
    - This code is full of all the math and physics work we have done for this project. It takes the mass of the projectile and the distance the user wants it to launch       to calculate the angle the release pin of the sling needs to be at. 
    - <img src="Media/mathPic.png" width="300">
    - <img src="Media/mathReplit.png" width="300">
- [servoCode.py](servoCode.py)
    - This was a programming breakthrough with the servos where I figured out how to control them simply, but very effectively. The use of gpiozero in this code greatly       reduces the jitter in the servos and makes them rotate smoothly.
    - [An extremely helpful resource in coding the servos.](https://gpiozero.readthedocs.io/en/stable/api_output.html#servo)
    - <img src="Media/servoCode.GIF" width="300">
    - <img src="Media/servoError.png" width="300"> It's important to make sure the pigpio daemon is running.
- [buttonTest.py](buttonTest.py)
    - This is still very preliminary code, but it was just working with getting the press of a button to make a servo move, combined with the input capabilities and           control of angleTest.
    - <img src="Media/buttonTest.png" width="300">
- [servo.py](servo.py) and [servoTest.py](servoTest.py)
    - Both of these files just play around with moving servos.
    - <img src="Media/servo.GIF" width="300">
    - <img src="Media/servoTest.GIF" width="300">
- [Flask](Flask)
    - While not a ton was accomplished on the user interface, there was some progress.
    - With [app.py](app.py), a button appears that can be clicked to make both servos rotate once. This file still needs some logic work, because the servos rotate once       and then don’t move back, and the button can’t be used multiple times.
    - There is also some start on a form that would accept the values the user needs to input.
    - More extensive Flask work is done here, credit to Benji Paquette: (https://github.com/Bhenry4/PiTrebuchet)
    - <img src="Media/flaskServoClick.GIF" width="300">
    - <img src="Media/servoFlask.png" width="300">
    - <img src="Media/servoFlaskButton.png" width="300">

A picture of the wiring for the pi where most of the code was being developed and tested.

<img src="Media/projectWiring.JPG" width="500">


## Math and Physics
<img src="Media/jamboard2.png" width="300">
<img src="Media/jamboard3.png" width="300">
<img src="Media/shieldsMath.png" width="300">
<img src="Media/sratchpaper1.jpg" width="300">
<img src="Media/scratchpaper2.jpg" width="300">
<img src="Media/scratchpaper3.jpg" width="300">
<img src="Media/scratchpaper4.jpg" width="300">
<img src="Media/physics1.png" width="300">
<img src="Media/physics2.png" width="300">
<img src="Media/desmos1.png" width="300">
<img src="Media/desmos2.png" width="300">
<img src="Media/desmos3.png" width="300">
<img src="Media/desmosPoints.png" width="300">
<img src="Media/desmosSliderspng" width="300">
