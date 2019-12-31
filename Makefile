help:
	@echo "    run-cmdline"
	@echo "        Run the bot in the command line."
	@echo "    train"
	@echo "        Train a combined Rasa NLU and Core model."

train:
	rasa train 

run_actions:
	rasa run actions

run-cmdline:
	rasa shell