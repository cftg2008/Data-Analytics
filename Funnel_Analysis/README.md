# Funnel_Analysis <h1>

### Overview <h3>
In this project, we are going to analyze the customer funnel of Metrocar, a ride-sharing app, to determine areas for enhancement and optimization. Through funnel analysis, we will provide recommendations based on the insights derived from the data.

### Dataset structure <h3>

The data for this dataset was generated specifically for this project. And it is inspired by publicly available datasets for Uber/Lyft. Metrocar stores its data in a PostgreSQL database with five main tables:
* App_downloads - contains information about app downloads
* Signups - contains information about new user signups
* Ride_requests - contains information about rides
* Transactions - contains information about financial transactions based on completed rides
* Reviews - contains information about driver reviews once rides are completed

The task is to use SQL Window functions like lag() and first_value() to set up and run a customer funnel analysis. The resulting data will help us to gain insights to answer those questions raised by the stakeholders.
[Link to Dashboard - Metrocar Story](https://public.tableau.com/views/First_16885084758340/FunnelAnalysis?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)
