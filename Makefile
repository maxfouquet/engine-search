build:
	docker build -t engine-search .

run:
    docker run -p 5001:5000 -d engine-search