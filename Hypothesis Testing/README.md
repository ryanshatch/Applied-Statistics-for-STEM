<h1><bold><div style="text-align: center"> Project Two: Hypothesis Testing </div><bold></h1>

<!-- ### This notebook contains the step-by-step directions for Project Two. It is very important to run through the steps in order. Some steps depend on the outputs of earlier steps. Once you have completed the steps in this notebook, be sure to write your summary report.  -->

### **You are a data analyst for a basketball team and have access to a large set of historical data that you can use to analyze performance patterns.**

#### The coach of the team and your management have requested that you perform several hypothesis tests to statistically validate claims about your team's performance. 

#### This analysis will provide evidence for these claims and help make key decisions to improve the performance of the team. You will use the Python programming language to perform the statistical analyses and then prepare a report of your findings for the team’s management. Since the managers are not data analysts, you will need to interpret your findings and describe their practical implications. 


<code>There are four important variables in the data set that you will study in Project Two.</code> 

## 

| <div style="text-align: left"> Variable </div>  |   <div style="text-align: left"> What does it represent? </div> |
| -- | --  |
| <div style="text-align: left"> pts </div> | <div style="text-align: left"> Points scored by the team in a game </div> |
| <div style="text-align: left"> elo_n </div> | <div style="text-align: left"> A measure of relative skill level of the team in the league </div> |
| <div style="text-align: left"> year_id </div> | <div style="text-align: left"> Year when the team played the games </div> |
| <div style="text-align: left"> fran_id </div> | <div style="text-align: left"> Name of the NBA team </div> |

## 

### The ELO rating, represented by the variable **elo_n**, is used as a measure of the relative skill of a team. 

#### This measure is inferred based on the final score of a game, the game location, and the outcome of the game relative to the probability of that outcome. The higher the number, the higher the relative skill of a team.

<code>In addition to studying data on your own team, your management has also assigned you a second team so that you can compare its performance with your own team's.</code> 

##

| <div style="text-align: left"> Team </div>  |   <div style="text-align: left"> What does it represent </div> |
| -- | --  |
| <div style="text-align: left"> Your Team </div> | <div style="text-align: left"> This is the team that has hired you as an analyst. This is the team that you will pick below. See Step 2.</div> |
| <div style="text-align: left"> Assigned Team </div> | <div style="text-align: left"> This is the team that the management has assigned to you to compare against your team. See Step 1. </div> |
#
<!-- <br> -->
<hr>
<!-- Reminder: It may be beneficial to review the summary report template for Project Two prior to starting this Python script. That will give you an idea of the questions you will need to answer with the outputs of this script. -->

<!-- **--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------** -->

<!-- ### Getting started
There are various things you can do to quickly and efficiently configure your Codio Box to your exact requirements. 

### GUI Applications and the Virtual Desktop 
The Virtual Desktop allows you auto develop GUI based applications using any programming language. You can install a Virtual Desktop in your Box. You can then start the desktop and view it within the Codio IDE or in a new browser tab.

[Virtual Desktop documentation](https://codio.com/docs/ide/boxes/installsw/gui/)


### Command line access and the Terminal window
All Codio Boxes provide sudo level privileges to the underlying Ubuntu server. This means you can install and configure any component you like. You access the terminal from the **Tools->Terminal** menu item.

### Debugger
The Codio IDE comes with a powerful visual debugger. Currently we support Python, Java, C, C++ and NodeJS. Other languages can be added on request.

[Debugger documentation](https://codio.com/docs/ide/features/debugging/)


### Content authoring and assessments
Codio comes with a very powerful content authoring tool, Codio Guides. Guides is also where you create all forms of auto-graded assessments. 

- [Guides documentation](https://codio.com/docs/content/authoring/overview/)
- [Assessments documentation](https://codio.com/docs/content/authoring/assessments/)

### Templating Box configurations and projects
Codio offers two very powerful templating options so you can create new projects from those templates with just a couple of clicks. **Stacks** allow you to create snapshots of the Box’s underlying software configuration. You can then create new projects from a Stack avoiding having to configure anew each time you start a new project. **Starter Packs** allow you to template an entire project, including workspace code.

- [Stacks documentation](https://codio.com/docs/project/stacks/)
- [Starter Packs documentation](https://codio.com/docs/project/packs/)

### Install software
You can always install software onto your Box using the command line. However, Codio offers a shortcut for commonly installed components that can be accessed from the **Tools->Install Software** menu.

We can easily add new items to the Install Software screen, so feel free to submit requests.

[Install Software documentation](https://codio.com/docs/ide/boxes/installsw/box-parts/) -->