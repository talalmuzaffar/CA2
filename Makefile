.PHONY: test install

test:
	@echo "Running tests..."
	@pytest test.py

install:
    @echo "Installing requirements..."
    @pip3 install -r requirements.txt