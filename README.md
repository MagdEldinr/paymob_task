# Paymob task

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-task">About The task</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#deployment">Deployment</a></li>
  </ol>
</details>

<!-- ABOUT THE Task -->

## About The Task

- We have 1 data about medicines with the follow schema
  - One of them is KEY and another is Values.
- We are aiming to find all similar values of a selected key and the percentage of these similarities (text-matching).

- To Do: - User must select the key, once the user clicks search you will view all similar values for that key text which have more than 50% of matching percentage. - First View - Create simple interface that contains drop-down list with all keys from the file and a search button. - Second View - Create simple table to list all of the results for example
  Key | Values | Matching Percentage
  :------------ | :-------------| :-------------|
  Key 1 | Value 250 | 88.8 % |
  | Value 300 | 51 % |

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- Python == 3.8
- Django == 3.2.13
- Django Rest framework == 3.13.1
- SQLite

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

- python3.7.\*
  ```
    download and install from https://www.python.org/downloads/
  ```
- Pull docker image
  ```
    docker pull magdeldinr/paymob-task:latest
  ```

### Installation

1. Create a virtual envirnoment

```
   python3 -m venv venv
```

2. Add required environment variables
3. Run docker image

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- TESTING -->

## Testing

### How To Run Test Cases

```sh
python manage.py test
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Deployment -->

## Deployment

1. App is deploy on Heroku & you can check using this [link](https://serene-springs-42525.herokuapp.com/)
