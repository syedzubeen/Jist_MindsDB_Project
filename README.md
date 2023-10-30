# JIST

<div style="text-align: center;">
<table>
  <tr>
    <td align="center"><img src="https://github.com/syedzubeen/Jist_MindsDB_Project/assets/14253061/555946f3-297a-40ad-89ab-9e380731d121" height="50" width="180" alt="Logo 1"></td>
    <td align="center"><img src="https://github.com/syedzubeen/Jist_MindsDB_Project/assets/14253061/df9c32b0-3e90-4d04-bc7c-40891530d49f" height="50" width="210" alt="Logo 2"></td>
    <td align="center"><img src="https://github.com/syedzubeen/Jist_MindsDB_Project/assets/14253061/141bc89d-58b7-4a48-8431-c8ed5d48681b" height="50" width="375" alt="Logo 3"></td>
  </tr>
</table>
</div><br><br>

JIST is a web application that utilizes [MindsDB](https://www.mindsdb.com/) and [OpenAI](https://openai.com) to generate concise and informative summaries of research papers. It is designed to help users quickly grasp the key insights and findings from research papers without the need to read the entire document. <br>

![mindsdb-summary](https://github.com/syedzubeen/Jist_MindsDB_Project/assets/14253061/00efbf2c-6e59-4265-ba8b-c291f6bdbc0c)


## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Paper Summarization**: Automatically generates summaries of research papers.
- **User-Friendly Interface**: A user-friendly web interface powered by Flask.
- **Easy to Deploy**: Set up and run the application on your own server.

## Getting Started

To get started with the JIST, follow these instructions:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/syedzubeen/Jist_MindsDB_Project.git

Follow these steps to get Ripped up and running on your local machine:
   
2. **Create a Virtual Environment:**
     ```sh
     python -m venv venv
     Linux: source venv/bin/activate
     Windows: venv\Scripts\activate

3. **Install Dependencies:**
      ```sh
      pip install requests, asyncio

4. **Create an env_vars.txt file in the app directory with the following content:**
   ```sh
   USERNAME=<MindsDB Cloud Username>
   PASSWORD=<MindsDB Cloud Password>
   
5. **Run the Application:**
   ```sh
   flask run
   
6. **Access the Application:**

   Open your web browser and navigate to http://localhost:5000 to access Jist.
   
## Usage

- Upload your research paper by choosing the appropriate file.
- Click on Summarise to generate the summary for the requested paper.


## Contributing
We welcome contributions from the community. If you would like to contribute to this project, please follow these steps:

- Fork the repository on GitHub.
- Create a new branch with a descriptive name for your feature or bug fix.
- Make your changes and commit them with clear and concise commit messages.
- Push your changes to your fork on GitHub.
- Submit a pull request to the main repository's main branch.

## License
This project is licensed under the MIT License. You can find more details in the LICENSE file.
