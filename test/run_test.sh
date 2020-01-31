#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <type>" >&2
  exit 1
fi

DIR=build_$1

cd $(dirname $0)
rm -rf $DIR
mkdir $DIR
cd $DIR

cmake .. \
  "-DCMAKE_C_FLAGS=--coverage" \
  "-DCMAKE_CXX_FLAGS=--coverage" \
  "-DCMAKE_MODULE_LINKER_FLAGS=--coverage"
cmake --build .
ctest -V .

mkdir coverage
COV=coverage/coverage.info
HTML=coverage/html
ROOT=$(realpath $(dirname $0))/src

lcov --rc lcov_branch_coverage=1 --directory ./ --capture --output-file $COV
lcov --rc lcov_branch_coverage=1 --extract $COV "${ROOT}/*" --output-file $COV
lcov --rc lcov_branch_coverage=1 --list $COV
genhtml --rc lcov_branch_coverage=1 --output-directory $HTML $COV
