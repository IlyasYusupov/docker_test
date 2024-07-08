import subprocess
import os
import time

def compile_tex_to_pdf(tex_file):


    # result = subprocess.run(
    #     ["/usr/bin/xvfb-run", "--auto-servernum", "--server-args=-screen 0 1024x768x16", "lualatex", f"{tex_file}"],
    #     cwd=os.getcwd(),
    #     stdout=subprocess.PIPE,
    #     stderr=subprocess.PIPE,
    #     text=True,
    # )
    #while True:
    print("Hello")
if __name__ == "__main__":
    compile_tex_to_pdf('test.tex')