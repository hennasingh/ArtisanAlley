# Artisan Alley - Connect with Artists in Ireland

Artisan Alley is a directory of local arts and crafts market in Ireland. The site is built using Django, Python, and Postgres database for the portfolio project 4 of Code Institute's Full Stack Development Diploma.

### Responsive Image

Live Link: https://artisanalley-11b7201d6523.herokuapp.com/

## User Experience - UX

### Strategy

I have always loved arts and crafts and often wanted to combine my love for both arts and technology to create something helpful and meaningful. On my research I found out, there is no common platform where one can find out all kinds of artisans available in Ireland. I attended two exhibitions Art Source and Gifted that happened last year on different times where I discovered amazing crafts available Ireland. Hence the inspiration to create a platform to search for these artists.

#### User Stories

All user stories can be found in the linked [Github project](https://github.com/users/hennasingh/projects/6).

### Scope

This was a sprint work till the last day. I had a highlevel plan for my project, but it evolved as and when I discovered possibilities of Django and my desire to understand more features. I did divert from my initial original plan based on time and my knowledge but I am proud of what I accomplished.

Overall, this site aims to develope an online directory of all kinds of artists available in Ireland. The platform provides features for user registeration, authentication, artworks creation, profile management, and messaging. More details in the features section.

- Artworks Page - This page lists all the artworks posted by registered artists on the website.
- Artists Page - The page lists all artists registered on the website.
- Login/Register - To post artworks you are required to register on the site

### Skeleton

The wireframes for mobile and desktop were created using Balsamiq. These were the original ideas but they changed as I learned and progressed in the actual development of the website. Some of the features will be implemented in future versions.

<details>
<summary>Home Page - Artists</summary>

![Artists](./assets/readme-images/artistsPage.png)

</details>

<details>

<summary>Artworks - Art Listings</summary>

![Art Listings](./assets/readme-images/artListingsPage.png)

</details>

<details>
<summary>Artist Profile</summary>

![Artist Profile](./assets/readme-images/artistProfilePage.png)

</details>

<details>
<summary>Signup</summary>

![Signup](./assets/readme-images/signupPage.png)

</details>

<details>
<summary>Log In</summary>

![Log In](./assets/readme-images/loginPage.png)

</details>

## User Interface - Surface

### Typography

### Colors

Color scheme suggestions were taken from Coolers on uploading an image from Freepick.

<details>
<summary>Color Palette </summary>

![Color Palette](./assets/readme-images/colorPallete.png)

</details>

### Database Schema

![entity relationship diagram](./assets/readme-images/erdSQL.png)

#### Models

1. Allauth User Model

The User model is part of Django Allauth. The model comes with predefined fields such as username, email, name, password, and more. This model is used for user authentication, and hence changes to this model are not advised. The User model has a one to one relationship with the Profile model.

2. Profile Model

This is a custom model to manage the Artist profile details. Django signals are used to reflect the changes between the User and Profile models. For example, if a user profile is deleted, user also gets deleted from the User model.

3. Artworks or ArtListing Model

The artwork model has one to many relationship with the profile Model as a profile can have multiple artworks. It is connected using profile_id Foreign Key.

4. Favorites Model

This model stores favorites for each profile. It is connected via Foreign Key profile_id and artwork_id to Profile and Artwork models respectively. #

5. Tag Model

This model stores tags an artist can add to its artwork.

#### Resources

https://www.youtube.com/watch?v=ynToND_xOAM - Django Widget Tweaks
