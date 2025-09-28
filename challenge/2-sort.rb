#!/usr/bin/env ruby
# Correct implementation: sort numeric args ascending and print each on a line.

# Keep only pure integers (e.g., -9, 0, 12), ignore non-numeric args.
nums = ARGV.select { |a| a.match?(/\A-?\d+\z/) }.map!(&:to_i)

# Sort ascending and print each on its own line.
nums.sort.each { |n| puts n }
