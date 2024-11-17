modules :
	- pyperclip : this mosule used to copie text to the clipboard.

Variables:
	Constantes:
		- SYMBOLS : every possible symbol that can be encrypted/decrypted
	NonConstantes:
		- response : assign the input of the user to this variable.
		- mode : this will define if the user want to (encrypt/decrypt) .
		- maxkey : the max integre that will be used to (e/d)
		- key : (integre) contain the key after change his type to integre.
		- message : contain the message to be encrypt or decrypt(uppercase)
		- encrypted : contain the encrypted message
		- decrypted : contain the decrypted message.
		- symbol : take value from SYMBOLS.
		- num : contain the number of symbol in SYMBOLS.

Functions:
	Methodes:
		- pyperclip.copy(message) # copy message to clipboard(you can past it
						any where you want).
		- pyperclip.past(message) # past message to a specified variable.
		- string.lower() # Translate the whole strig into appercase characters.
		- string.format(stringReplace) : replace curly brakets {} inside string with 
						the content of stringReplace.
		- string.find(substring)  # used to find substring within a string(it returns 
						the positon of the first character in substring
						and it start count from 0, if not match substring
						it returns -1.

Exceptions:
	- To avoid ImportError if the Module 'pyperclip' is not installed. Even if 
	pyperclip package is not installed, you can also run the program and copy/past
	the encrypted/decrypted message manually.

Loops:
	-  while : Keep asking until the user enters a valid value.
	-  for : to loop through strings.