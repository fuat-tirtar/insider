import time
import requests
import subprocess
import docker

def check_grid_health():
    try:
        # Check Selenium Hub health
        hub_health = requests.get("http://localhost:4444/status").json()
        if hub_health.get("value", {}).get("ready") == True:
            print("Selenium Hub is ready!")
        else:
            print("Selenium Hub is not ready.")
            return False
        
        # Check Selenium Nodes health (example for chrome nodes)
        node_health = requests.get("http://localhost:4444/grid/api/proxy?id=http://chrome:5555").json()
        if node_health.get("success") == True:
            print("Chrome Node is ready!")
        else:
            print("Chrome Node is not ready.")
            return False
        
        # Add checks for other nodes if needed

        return True

    except Exception as e:
        print(f"Exception occurred while checking grid health: {str(e)}")
        return False

def start_selenium_grid(node_count):
    try:
        # Docker client initialization
        client = docker.from_env()

        # Starting Selenium Hub
        hub_container = client.containers.run("selenium/hub:4.21.0",
                                              detach=True,
                                              ports={"4444": "4444"},
                                              name="selenium-hub")

        print(f"Selenium Hub container started with ID: {hub_container.id}")

        # Starting Chrome nodes based on node_count
        for i in range(node_count):
            node_container = client.containers.run("selenium/node-chrome:4.21.0",
                                                   detach=True,
                                                   environment={
                                                       "SE_EVENT_BUS_HOST": "selenium-hub",
                                                       "SE_EVENT_BUS_PUBLISH_PORT": "4442",
                                                       "SE_EVENT_BUS_SUBSCRIBE_PORT": "4443"
                                                   },
                                                   volumes={"/dev/shm": {"bind": "/dev/shm", "mode": "rw"}},
                                                   ports={"5900": f"5900{i}"},
                                                   name=f"chrome-node-{i}")
            print(f"Chrome Node {i+1} container started with ID: {node_container.id}")

        # Wait a few seconds for nodes to register with Hub
        time.sleep(10)

    except Exception as e:
        print(f"Exception occurred while starting Selenium Grid: {str(e)}")

def run_tests():
    try:
        # Running tests using Docker-compose
        subprocess.run(["docker-compose", "up", "--scale", f"chrome-node={node_count}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running tests: {e}")

if __name__ == "__main__":
    node_count = 2  # Set the number of nodes you want to start (1 to 5)

    # Check Selenium Grid health
    if check_grid_health():
        print("Selenium Grid is healthy.")

        # Start Selenium Grid with specified node count
        start_selenium_grid(node_count)

        # Run tests
        run_tests()
    else:
        print("Selenium Grid is not healthy. Exiting...")
