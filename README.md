# base

**Update** 
Jan 31, 2021 - This readme is still in the works

This repository is maintained by fourfridays. We fork this repo for our clients as a starting point for their Wagtail websites. Here are some feature sets already enabled and setup for you:

* Standard Page Template
    * Hero Images
    * Image Grid
    * Single/Two/Three/Four column layouts
        * Heading Block
        * Paragraph Block
        * Image Block
        * Button Block
        * Image Grid Block
        * Document Block
        * Embed Block
        * Icon Block
        * Table
        * RAW HTML
* Article
    * Create various types or Articles for blogs, news, tutorials, etc.
    * Tagging
    * Categories
    * Authors
    * Commenting
        * enable commenting option per Article
        * Authenticated comments via Google and Twitter Sign-in options
        * Moderation in Wagtail admin. Admin approves each comment before its published on website. Admin is notified for each comment submitted
* Navigation
    * Mark which pages are list on the navigation
    * Ability to show select sub-pages on navigation
    * Sub-pages on navigation are limited to one level below parent, meaning you can show sub-sub pages on the navigation
* Third party email provider setup
    * Define your own email provider api
* Sitemaps
* Sentry Logging

To demo the repository and all its options:
1. Fork this repository
2. Setup free account on divio.com
    * Custom Project
    * Your forked repo URL

Templates are very basic and more or less very alpha starting points. They would need to be customized and designed to your needs. The site is built-on Bootstrap 5.1.3 framework.

We use gruntjs as our javascript task runner.

## How to Apply Updates
Please **fork** this repository on Github. When we release updates to this repo you can apply those updates as well by:
* Go to your forked repo on GitHub
* Click Pull Requests -> New Pull Request
* Click compare across forks
* Select your forked repo as the base repo and fourfridays-org/base repo as the head
* Create pull request
* Merge Pull Request


