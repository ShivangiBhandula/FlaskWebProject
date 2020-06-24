# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

###- *Analyze costs, scalability, availability, and workflow*
### For more details follow the documentation on the docs.microsoft.com

The main focus is the project rotates around the deployment and running of the web app, Here the app service is better than the VM as it works on PaaS rather than IaaS that helps in quickly build, deploy and scale web apps and APIs with built-in CI/CD integration and zero-downtime deployments but the efficiency and ease comes with a higher cost than an Virtual Machine. the great thing with built in CI/CD is the deployment is effortless and fast.

### Assess app changes that would change your decision.


*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

the initial steps are cloning the github repository and ammending the TODO list and commiting to the repository. The next sept continued with the creation of resource group and resources and filling up of credential in config.py comitting to the github repository once all the depencies are filled with the app registeration. Create the App Services and deploy with the CI/CD intergration with github and voila it's done. VM would have been a better option if there's a need for frequent modifications and changes in your web server environment with a lot of features. however for correctly configuring and maintaining VM requires more time and not required for this project.

To sum up:

Web Apps:		Provides High Agility anf Ease of Management
			Provides Medium Control and Support for Legacy Apps

Virtual Machine:	Provides High Control and Support for Legacy Apps
			Provides Low Agility and Ease of Management