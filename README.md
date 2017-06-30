# codebooks
CS textbook IDE and notes marketplace integration

## Repo Organization
The repo is organized as follows, with expansions to follow with further 
implementations of modules:
	- Image subsectioning
	- Subimage to code
	- Code to executable environment
	- Code interaction (front end-user facing)

## Image Subsectioning
Reponsible for determining regions in the image that correspond to code
segments. There will be extensions to allow for multiple on-screen
code blocks, although initial implementations will focus on detecting
single blocks of code accurately when in-screen. The final outproduct
of this module will be a sub-image that can then be passed through OCR

## Subimage OCR
Given the subimage partition, determine the code that is on-screen. This
will also involve removing unnecessary mark-up that is detected on
screen, i.e. the >>> that is typically representative of a Python REPL
environment or the $ representative of a newline in Bash.

## To Executable Environment
Given the code text, determine which language is being analyzed. In
some ambiguous cases, i.e. if the entirety of the code is 
'print("Hello World"),' then the code could equivalently correspond to
Ruby or Python, we will prompt the user with both options or default
to the more popular option, based on the user's preferences. This will
then be loaded into an appropriate interactive environment, i.e. if it is
a piece of C code, the environment will load the function, import all the
necessary packages, and possibly call the function in the main() function
if necessary

## Code Interaction
There will be extensions to allow for a better user experience once the
code is detected and exported to the environment, i.e. we will need to
ensure that the code syncs with desktop for minimizing friction on
development. We will also have a git-like "repo" system in place for
textbooks for pulling other people's code, if they make it publicly
available, thus catering to a code textbook community.