import os
import json
import pathlib as pl
import numpy as np

NOISE_MUS = [0.0, 0.0]
NOISE_SIGMAS = [5.0, 10.0]


def main():
    print(list(os.environ.keys()))
    input_path = pl.Path(os.environ["INPUT_FOLDER"])
    output_path = pl.Path(os.environ["OUTPUT_FOLDER"])

    input_file_path = input_path / "input.json"
    output_file_path = output_path / "output.json"

    input = json.loads(input_file_path.read_text())

    output = model(input)

    output_file_path.write_text(json.dumps(output))


def model(input, mus=NOISE_MUS, sigmas=NOISE_SIGMAS):
    output = {}

    noise0 = np.random.normal(mus[0], sigmas[0])
    noise1 = np.random.normal(mus[1], sigmas[1])
    output["Y0"] = input["X0"] + input["X1"] + noise0
    output["Y1"] = input["X2"] + noise1
    return output


if __name__ == "__main__":
    main()
