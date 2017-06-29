#!/usr/bin/env elixir

defmodule Sim do

  def sim(index, limit, limit), do: {limit, limit - index}

  def sim(index, size, limit) do
    add = rem(index+div(size+1,2) - 1,  size) + 1
    size = size + 1
    index =
      if (index > add) do
        index
      else
        rem(size + index - 1, size)
      end
    sim(index, size, limit)
  end

  def calculate(input) do
    sim(0, 1, input)
  end
end

input = 3005290
result = Sim.calculate(input)
IO.inspect result
