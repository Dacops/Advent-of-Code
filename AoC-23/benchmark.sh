#!/bin/sh

set -e

test -d $1 || (echo "Pass day directory as argument" && exit 1)

cd $1

# Assuming your Makefile has targets: all, 1, 2, and clear
make all

hyperfine "make 1 && make 2" --warmup 1000 --shell "/bin/sh"

# Optionally, clean up after running the benchmarks
make clear
