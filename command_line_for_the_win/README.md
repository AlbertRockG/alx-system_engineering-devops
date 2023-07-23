# Command line for the win

## Background Context

CMD CHALLENGE is an engaging game that tests your Bash skills. The entire game is played via the command line, and the questions progressively become more challenging. It serves as excellent practice to enhance your command line proficiency!

## Steps to Use SFTP Command-Line Tool

To transfer your completed level screenshots to the sandbox environment, follow these steps:

1. **Take the Screenshots:**

   Take screenshots of the completed levels, and save them inside the directory `/root/alx-system_engineering-devops/command_line_for_the_win/` on your local machine.

2. **Open Terminal or Command Prompt:**

   Open a terminal or command prompt on your local machine. This is where you will execute the SFTP commands.

3. **Connect to Sandbox Environment:**

   Use the SFTP command to establish a connection to the sandbox environment. Replace `hostname`, `username`, and `password` with the provided credentials for the sandbox environment.

   ```
   sftp username@hostname
   ```
   Note: You may encounter a security warning when connecting for the first time. Type `yes` to continue connecting.

4. **Navigate to Destination Directory:**

   Once connected to the sandbox environment, navigate to the destination directory where you want to upload the screenshots. In this case, use the following command to navigate to the specified directory:

   ```
   cd /root/alx-system_engineering-devops/command_line_for_the_win/
   ```

5. **Upload Screenshots:**

   Use the `put` command to upload the screenshots from your local machine to the sandbox environment.

   ```
   put /path/to/local/screenshots/*.png
   ```
   Replace `/path/to/local/screenshots/` with the actual path to the folder containing your screenshots. The `*.png` wildcard will upload all PNG files in that folder. Adjust the wildcard pattern if your screenshots have a different extension.

6. **Confirm Transfer:**

   After executing the `put` command, the SFTP tool will begin transferring the screenshots to the sandbox environment. Confirm that the transfer was successful by checking the sandbox directory for the uploaded screenshots.

7. **Push to GitHub:**

   Once the screenshots are successfully transferred to the sandbox environment, proceed to commit and push the screenshots to your GitHub repository, adhering to the initial requirements.

## Note

The screenshots of the completed levels should be stored inside the directory `/root/alx-system_engineering-devops/command_line_for_the_win/`.

Have fun mastering the CMD CHALLENGE and improving your command line skills! Happy coding!