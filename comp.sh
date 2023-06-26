#!/usr/bin/env bash

cppFlags="g++ -std=c++20 main.cpp -o app"
execApp="./app"

$cppFlags
sleep 1s
$execApp

