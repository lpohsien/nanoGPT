import numpy as np
import tiktoken
import os


def print_token(token):
    token = token.decode("utf-8")
    if token == "\n":
        return "<br>\n"
    else:
        return "<" + token + ">"


if __name__ == "__main__":

    INPUT_FILE = "data/shakespeare/train.bin"
    OUTPUT_FILE = "data/train_tokens.txt"

    data_bin = np.fromfile(INPUT_FILE, dtype=np.uint16)

    encoder = tiktoken.get_encoding("gpt2")
    databytes = encoder.decode_tokens_bytes(data_bin.tolist())
    token_separated_text = list(f"{print_token(token)}" for token in databytes)

    if os.path.exists(OUTPUT_FILE):
        print(f"Removing existing file {OUTPUT_FILE}")
        os.remove(OUTPUT_FILE)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("".join(token_separated_text))
