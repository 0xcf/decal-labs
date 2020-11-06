class hacked::hacking {
    
    # Section 1: Install packages needed for the script
    # Packages to install: figlet, lolcat, jp2a
    # https://puppet.com/docs/puppet/6.19/types/package.html 

    # ** YOUR CODE HERE **





    # Section 2: Copy files to the right location
    # hack_everything should be in /usr/local/bin
    # pwned.jpg should be in $HOME (use full path to your homedir, /home/<your_username>)
    # Make sure file permissions let you read/run the script and image!
    # Make sure this *requires* the packages from Section 1, and ensure the script *requires* pwned.jpg
    # (i.e. Section 2 depends on Section 1, and the script requires pwned.jpg)
    # https://puppet.com/docs/puppet/6.19/types/file.html

    # ** YOUR CODE HERE **





    # Section 3: Use puppet cron module to have your script run periodically
    # Run hack_everything every 30 minutes and append its output to a file $HOME/hackzored.txt
    # Make sure to use full paths
    # Make sure this *requires* the files from Section 2
    # https://puppet.com/docs/puppet/6.19/types/cron.html

    # ** YOUR CODE HERE **



}
