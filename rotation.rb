#!/usr/bin/env ruby

capital_alphabet = ("A".."Z").to_a
lowercase_alphabet = ("a".."z").to_a
number = ("0".."9").to_a

cipher_text = "96a_abL_?b04c?0Cbc50C_E_C03c4<HcC5DN"

(1..25).each do |i|
  puts "he2023{#{
    cipher_text.dup
      .tr(capital_alphabet.join, capital_alphabet.rotate(i).join)
      # .tr(lowercase_alphabet.join, lowercase_alphabet.rotate(i).join)
      .tr(number.join, number.rotate(i).join)
  }}"
end

# ABCaDEcFGBHIBhgbH