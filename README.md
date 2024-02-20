# DemoDataGen
This is a sample application that shows how you can use GPT to generate demo data.

## Inputs
There are two input files, `sys_prompt.txt` and `user_prompt.txt` that are feed into
the GPT chat API.  `sys_prompt.txt` contains generic instructions for how to generate
demo data, while `user_prompt.txt` contains the specification of the data to generate.

## Notes

The specification can be a CSV dump of a few rows of pre-existing data. Even if that data is
not high quality, GPT can use that to generate better looking, more complete data.  You might
also get away with a more complicated format (if you want to provide hints and restrictions
on the data to be generated); that might require updating the system prompt to describe your
format.

I've provided a sample user_prompt.txt file to give you an idea of what an input might look like.

The code is set to generate 10 sample rows, but you can easily change that.

To generate 10 sample rows costs about 6 cents with GPT-4.  GPT-3.5 tends to have problems in
its generation: thus I prefer GPT-4, but perhaps more prompt work could fix those.  It doesn't seem
worthwhile, though, given how cheap GPT-4 is, unless you need high volumes of data.  The code prints
the tokens consumed both on the input (prompt) and output so that you can see how much it's costing to
generate your demo data (using the current pricing from OpenAI).

Finally, since most LLMs offer very similar APIs to OpenAI, you could switch this to using some
other vendor's API with minimal effort.
