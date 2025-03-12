import subprocess
import docker
import os

def run_code(code, language):
    client = docker.from_env()
    lang_images = {"python": "python:3.9", "cpp": "gcc:latest", "java": "openjdk:11"}
    if language not in lang_images:
        return "Unsupported language"

    image = lang_images[language]
    filename = f"/tmp/code.{language}"
    with open(filename, "w") as f:
        f.write(code)

    try:
        container = client.containers.run(
            image, f"python {filename}" if language == "python" else f"g++ {filename} -o /tmp/a.out && /tmp/a.out",
            remove=True, mem_limit="256m", stdout=True, stderr=True
        )
        return container
    except Exception as e:
        return str(e)
