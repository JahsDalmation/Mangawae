# Mangawae

  Mangawae is a simple python based program that can search, download and view manga!

# Installation

  # Dependancies
  
    - curl
    - img2pdf
    - Python 3 (or newer)
    - atril (pdf viewer) 
  
  # Steps
  
    # Optional
      This step is not reccomended for new linux users.
    !!! If you do this step you MUST, where applicable, adjust the following commands       !!!
    !!! If you do not understand, enter: cd      into a terminal and continue at # Required !!!
    
    - First start by moving into the directory you wish to install Mangawae into.
        On linux/bsd this would be:
          cd /path/to/directory
        Note:
          This step is optional. If ignored, Mangawae will more than likely be
            placed into the $HOME directory.

    # Required  
    - Clone the Mangawae repo.
        To do this use git clone:
          git clone https://github.com/JahsDalmation/Mangawae.git
          
    - Add a simple alias to your shells config file.
        !!! If unsure, enter:    cd && ls -1a       !!!
        !!! Look for a .bashrc or .zshrc file       !!!
        
      For .bashrc :
        echo 'alias Mangawae="cd $HOME/Mangawae/ && python Mangawae.py && cd"' >> $HOME/.bashrc
        
      For .zshrc :
        echo 'alias Mangawae="cd $HOME/Mangawae/ && python Mangawae.py && cd"' >> $HOME/.zshrc
        
# Usage
    
    Mangawae
