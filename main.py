#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Justin Zhu
# CLI Tool for creating dependency graphs
import os
import argparse
import sound

argparser = argparse.ArgumentParser(description='Get Sound Recording')

argparser.add_argument("-o", "--output", help="saved file output name, make sure to include .wav extension")

argparser.add_argument("-t", "--time", help="maximum time you want program to run in seconds")

args = argparser.parse_args()

sound.main(args.output, time)

