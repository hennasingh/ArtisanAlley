# Artisan Alley

Artisan Alley is a directory of local arts and crafts market in Ireland. The site is built using Django, Python, and Postgres database for the portfolio project 4 of Code Institute's Full Stack Development Diploma.

## User Experience - UX

### Skeleton

The wireframes for mobile and desktop were created using Balsamiq. These were the original ideas but they changed as I learned and progressed in the actual development of the website. Some of the features will be implemented in future versions.

#### Home Page - Artists

![Artists](./assets/readme-images/artistsPage.png)

#### Artworks - Art Listings

![Art Listings](./assets/readme-images/artListingsPage.png)

#### Artist Profile

![Artist Profile](./assets/readme-images/artistProfilePage.png)

#### Signup

![Signup](./assets/readme-images/signupPage.png)

#### Log In

![Log In](./assets/readme-images/loginPage.png)

## User Interface - Surface

### Typography

### Colors

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
